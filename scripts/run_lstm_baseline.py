#!/usr/bin/env python3
"""
Run LSTM Baseline Model for DO Prediction
Automates data loading, processing, training, and evaluation
"""

import sys
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
import json
import pickle
from datetime import datetime

# Deep learning
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models, callbacks
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Import from our package
sys.path.insert(0, str(Path(__file__).parent.parent))
from imta_analytics.data import load_toa5_file

# Set random seeds
np.random.seed(42)
tf.random.set_seed(42)
warnings.filterwarnings('ignore')

print("="*70)
print("LSTM BASELINE MODEL FOR DISSOLVED OXYGEN PREDICTION")
print("="*70)
print(f"\nTensorFlow version: {tf.__version__}")
print(f"GPU Available: {len(tf.config.list_physical_devices('GPU')) > 0}")

# ============================================================================
# 1. DATA LOADING AND PROCESSING
# ============================================================================

print("\n" + "="*70)
print("STEP 1: DATA LOADING AND PROCESSING")
print("="*70)

# Define paths
DATA_DIR = Path('data')
RAW_DIR = DATA_DIR / 'aquafort-buoy-station'
PROCESSED_DIR = DATA_DIR / 'processed'
MODELS_DIR = Path('models')
RESULTS_DIR = Path('results')

# Create directories
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
MODELS_DIR.mkdir(parents=True, exist_ok=True)
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

# Load EXO2 data
EXO2_FILE = RAW_DIR / 'UNH-G2000B_EXO2SumData.dat'
print(f"\nLoading data from: {EXO2_FILE}")

df, metadata, units = load_toa5_file(EXO2_FILE)

print(f"✓ Data loaded successfully")
print(f"  Shape: {df.shape}")
print(f"  Date range: {df['TIMESTAMP'].min()} to {df['TIMESTAMP'].max()}")
print(f"  Duration: {df['TIMESTAMP'].max() - df['TIMESTAMP'].min()}")

# Select relevant features
feature_cols = [
    'EXO2Temp',      # Temperature
    'EXO2Salinity',  # Salinity
    'EXO2pH',        # pH
    'EXO2Chlor',     # Chlorophyll
    'EXO2Turb',      # Turbidity
    'EXO2Depth',     # Depth
]

target_col = 'EXO2DO'  # Dissolved oxygen (% saturation)

# Create working dataframe
df_work = df[['TIMESTAMP'] + feature_cols + [target_col]].copy()
df_work = df_work.set_index('TIMESTAMP').sort_index()

print(f"\nInitial data: {len(df_work)} records")
print(f"Missing values: {df_work.isnull().sum().sum()} ({df_work.isnull().sum().sum()/df_work.size*100:.2f}%)")

# Drop rows with missing values
df_clean = df_work.dropna()
print(f"After dropping NaN: {len(df_clean)} records")

# Apply physical bounds filtering to remove outliers and sensor errors
print("\nApplying physical bounds filtering...")
PHYSICAL_BOUNDS = {
    'EXO2DO': (60, 140),        # % saturation - normal range for aquaculture
    'EXO2Temp': (0, 35),        # °C - realistic water temperature range
    'EXO2Salinity': (0, 40),    # psu - saltwater range
    'EXO2pH': (6.5, 9.5),       # pH - typical aquaculture range
    'EXO2Chlor': (0, 100),      # RFU - chlorophyll range
    'EXO2Turb': (0, 100),       # FNU - turbidity range
    'EXO2Depth': (0, 20),       # m - sensor depth range
}

initial_count = len(df_clean)
for col, (min_val, max_val) in PHYSICAL_BOUNDS.items():
    if col in df_clean.columns:
        before = len(df_clean)
        df_clean = df_clean[(df_clean[col] >= min_val) & (df_clean[col] <= max_val)]
        removed = before - len(df_clean)
        if removed > 0:
            print(f"  {col}: removed {removed} outliers (valid range: {min_val}-{max_val})")

total_removed = initial_count - len(df_clean)
print(f"✓ Physical bounds filtering complete")
print(f"  Total outliers removed: {total_removed} ({total_removed/initial_count*100:.2f}%)")
print(f"  Clean data: {len(df_clean)} records")

# ============================================================================
# 2. FEATURE ENGINEERING
# ============================================================================

print("\n" + "="*70)
print("STEP 2: FEATURE ENGINEERING")
print("="*70)

df_features = df_clean.copy()

# Temporal features (circular encoding)
hour = df_features.index.hour
df_features['hour_sin'] = np.sin(2 * np.pi * hour / 24)
df_features['hour_cos'] = np.cos(2 * np.pi * hour / 24)

day_of_year = df_features.index.dayofyear
df_features['doy_sin'] = np.sin(2 * np.pi * day_of_year / 365)
df_features['doy_cos'] = np.cos(2 * np.pi * day_of_year / 365)

print("✓ Created temporal features (hour, day-of-year)")

# Lag features
n_lags = 12
for lag in range(1, n_lags + 1):
    df_features[f'DO_lag_{lag}'] = df_features[target_col].shift(lag)

print(f"✓ Created {n_lags} lag features (3 hours history)")

# Drop rows with NaN from lagging
df_features = df_features.dropna()
print(f"✓ Final dataset: {len(df_features)} samples, {df_features.shape[1]} features")

# Save processed data
feather_path = PROCESSED_DIR / 'exo2_data.feather'
df_clean.to_feather(feather_path)
print(f"✓ Saved processed data: {feather_path}")

# ============================================================================
# 3. TRAIN/TEST SPLIT
# ============================================================================

print("\n" + "="*70)
print("STEP 3: TRAIN/TEST SPLIT")
print("="*70)

# Chronological split: 80% train, 20% test
split_idx = int(len(df_features) * 0.8)

train_data = df_features.iloc[:split_idx]
test_data = df_features.iloc[split_idx:]

print(f"Training:   {len(train_data):5d} samples ({len(train_data)/len(df_features)*100:.1f}%)")
print(f"            {train_data.index[0]} to {train_data.index[-1]}")
print(f"Testing:    {len(test_data):5d} samples ({len(test_data)/len(df_features)*100:.1f}%)")
print(f"            {test_data.index[0]} to {test_data.index[-1]}")

# Separate features and target
X_train = train_data.drop(columns=[target_col])
y_train = train_data[target_col]

X_test = test_data.drop(columns=[target_col])
y_test = test_data[target_col]

# ============================================================================
# 4. NORMALIZATION
# ============================================================================

print("\n" + "="*70)
print("STEP 4: FEATURE NORMALIZATION")
print("="*70)

# Initialize scalers
scaler_X = MinMaxScaler(feature_range=(0, 1))
scaler_y = MinMaxScaler(feature_range=(0, 1))

# Fit on training data ONLY
X_train_scaled = scaler_X.fit_transform(X_train)
y_train_scaled = scaler_y.fit_transform(y_train.values.reshape(-1, 1))

# Transform test data
X_test_scaled = scaler_X.transform(X_test)
y_test_scaled = scaler_y.transform(y_test.values.reshape(-1, 1))

# Reshape for LSTM: (samples, timesteps, features)
X_train_lstm = X_train_scaled.reshape((X_train_scaled.shape[0], 1, X_train_scaled.shape[1]))
X_test_lstm = X_test_scaled.reshape((X_test_scaled.shape[0], 1, X_test_scaled.shape[1]))

print(f"✓ Features normalized to [0, 1]")
print(f"✓ Reshaped for LSTM:")
print(f"  X_train: {X_train_lstm.shape} (samples, timesteps, features)")
print(f"  X_test:  {X_test_lstm.shape}")

# ============================================================================
# 5. BUILD LSTM MODEL
# ============================================================================

print("\n" + "="*70)
print("STEP 5: BUILD LSTM MODEL")
print("="*70)

# Model configuration
LSTM_UNITS = 64
DROPOUT_RATE = 0.001
LEARNING_RATE = 0.01

model = models.Sequential([
    layers.LSTM(
        units=LSTM_UNITS,
        activation='elu',
        input_shape=(X_train_lstm.shape[1], X_train_lstm.shape[2]),
        return_sequences=False,
        name='lstm_layer'
    ),
    layers.Dropout(rate=DROPOUT_RATE, name='dropout_layer'),
    layers.Dense(units=1, activation='linear', name='output_layer')
])

optimizer = keras.optimizers.Adam(learning_rate=LEARNING_RATE)
model.compile(optimizer=optimizer, loss='mse', metrics=['mae', 'mse'])

print("✓ LSTM model created")
print(f"  LSTM units: {LSTM_UNITS}")
print(f"  Dropout: {DROPOUT_RATE}")
print(f"  Learning rate: {LEARNING_RATE}")
model.summary()

# ============================================================================
# 6. TRAIN MODEL
# ============================================================================

print("\n" + "="*70)
print("STEP 6: TRAIN MODEL")
print("="*70)

# Training parameters
EPOCHS = 100
BATCH_SIZE = 64
VALIDATION_SPLIT = 0.2

# Callbacks
early_stopping = callbacks.EarlyStopping(
    monitor='val_loss',
    patience=15,
    restore_best_weights=True,
    verbose=1
)

reduce_lr = callbacks.ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.5,
    patience=5,
    min_lr=0.0001,
    verbose=1
)

print(f"Training configuration:")
print(f"  Epochs: {EPOCHS}")
print(f"  Batch size: {BATCH_SIZE}")
print(f"  Validation split: {VALIDATION_SPLIT*100:.0f}%")
print(f"\nStarting training...\n")

history = model.fit(
    X_train_lstm,
    y_train_scaled,
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    validation_split=VALIDATION_SPLIT,
    callbacks=[early_stopping, reduce_lr],
    verbose=1
)

print("\n✓ Training completed!")

# ============================================================================
# 7. GENERATE PREDICTIONS
# ============================================================================

print("\n" + "="*70)
print("STEP 7: GENERATE PREDICTIONS")
print("="*70)

# Generate predictions
y_train_pred_scaled = model.predict(X_train_lstm, verbose=0)
y_test_pred_scaled = model.predict(X_test_lstm, verbose=0)

# Inverse transform to original scale
y_train_pred = scaler_y.inverse_transform(y_train_pred_scaled).flatten()
y_test_pred = scaler_y.inverse_transform(y_test_pred_scaled).flatten()

y_train_true = y_train.values
y_test_true = y_test.values

print(f"✓ Predictions generated")
print(f"  Train predictions: {y_train_pred.shape}")
print(f"  Test predictions:  {y_test_pred.shape}")

# ============================================================================
# 8. EVALUATE PERFORMANCE
# ============================================================================

print("\n" + "="*70)
print("STEP 8: PERFORMANCE EVALUATION")
print("="*70)

# Calculate metrics
train_r2 = r2_score(y_train_true, y_train_pred)
train_mae = mean_absolute_error(y_train_true, y_train_pred)
train_rmse = np.sqrt(mean_squared_error(y_train_true, y_train_pred))

test_r2 = r2_score(y_test_true, y_test_pred)
test_mae = mean_absolute_error(y_test_true, y_test_pred)
test_rmse = np.sqrt(mean_squared_error(y_test_true, y_test_pred))

# Display results
print("\n" + "="*70)
print("MODEL PERFORMANCE SUMMARY")
print("="*70)
print("\nTRAINING SET:")
print(f"  R² Score:  {train_r2:.4f}")
print(f"  MAE:       {train_mae:.4f} % saturation")
print(f"  RMSE:      {train_rmse:.4f} % saturation")

print("\nTEST SET:")
print(f"  R² Score:  {test_r2:.4f}")
print(f"  MAE:       {test_mae:.4f} % saturation")
print(f"  RMSE:      {test_rmse:.4f} % saturation")

print("\nLITERATURE BENCHMARKS:")
print(f"  Target R²:   > 0.85 (Baseline)")
print(f"  Expected R²: 0.90-0.93 (Strong LSTM)")
print(f"  Target MAE:  < 6% saturation")
print(f"  Target RMSE: < 10% saturation")

print("\nPERFORMANCE ASSESSMENT:")
if test_r2 >= 0.90:
    print("  ✓ EXCELLENT: Meets literature benchmark (R² ≥ 0.90)")
elif test_r2 >= 0.85:
    print("  ✓ GOOD: Meets baseline target (R² ≥ 0.85)")
else:
    print(f"  [Warning] NEEDS IMPROVEMENT: R² = {test_r2:.4f} < 0.85")

print("="*70)

# ============================================================================
# 9. SAVE MODEL AND RESULTS
# ============================================================================

print("\n" + "="*70)
print("STEP 9: SAVE MODEL AND RESULTS")
print("="*70)

# Save model
model_path = MODELS_DIR / 'lstm_baseline_do.keras'
model.save(model_path)
print(f"✓ Model saved: {model_path}")

# Save scalers
with open(MODELS_DIR / 'scaler_X.pkl', 'wb') as f:
    pickle.dump(scaler_X, f)
with open(MODELS_DIR / 'scaler_y.pkl', 'wb') as f:
    pickle.dump(scaler_y, f)
print(f"✓ Scalers saved")

# Save model info
model_info = {
    'model_type': 'LSTM Baseline',
    'created_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'architecture': {
        'lstm_units': LSTM_UNITS,
        'dropout_rate': DROPOUT_RATE,
        'learning_rate': LEARNING_RATE,
        'activation': 'elu',
        'optimizer': 'adam',
        'loss': 'mse'
    },
    'training': {
        'epochs_completed': len(history.history['loss']),
        'batch_size': BATCH_SIZE,
        'validation_split': VALIDATION_SPLIT,
        'early_stopping_patience': 15
    },
    'data': {
        'total_samples': len(df_features),
        'train_samples': len(train_data),
        'test_samples': len(test_data),
        'n_features': X_train_lstm.shape[2],
        'features': list(X_train.columns),
        'target': target_col,
        'n_lags': n_lags
    },
    'performance': {
        'train': {
            'r2': float(train_r2),
            'mae': float(train_mae),
            'rmse': float(train_rmse)
        },
        'test': {
            'r2': float(test_r2),
            'mae': float(test_mae),
            'rmse': float(test_rmse)
        }
    }
}

with open(MODELS_DIR / 'lstm_baseline_do_info.json', 'w') as f:
    json.dump(model_info, f, indent=2)
print(f"✓ Model info saved")

# Save training history
history_df = pd.DataFrame(history.history)
history_df.to_csv(MODELS_DIR / 'lstm_baseline_do_history.csv', index=False)
print(f"✓ Training history saved")

# Save predictions for analysis
results_df = pd.DataFrame({
    'timestamp': test_data.index,
    'actual_DO': y_test_true,
    'predicted_DO': y_test_pred,
    'residual': y_test_true - y_test_pred,
    'abs_error': np.abs(y_test_true - y_test_pred)
})
results_df.to_csv(RESULTS_DIR / 'lstm_predictions_test.csv', index=False)
print(f"✓ Predictions saved: results/lstm_predictions_test.csv")

# ============================================================================
# 10. GENERATE VISUALIZATIONS
# ============================================================================

print("\n" + "="*70)
print("STEP 10: GENERATE VISUALIZATIONS")
print("="*70)

# Set style
plt.style.use('seaborn-v0_8-whitegrid')

# Create comprehensive visualization
fig = plt.figure(figsize=(16, 12))
gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)

# 1. Training history - Loss
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(history.history['loss'], label='Training Loss', linewidth=2)
ax1.plot(history.history['val_loss'], label='Validation Loss', linewidth=2)
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Loss (MSE)')
ax1.set_title('Model Loss During Training', fontweight='bold')
ax1.legend()
ax1.grid(True, alpha=0.3)

# 2. Training history - MAE
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(history.history['mae'], label='Training MAE', linewidth=2)
ax2.plot(history.history['val_mae'], label='Validation MAE', linewidth=2)
ax2.set_xlabel('Epoch')
ax2.set_ylabel('MAE')
ax2.set_title('Model MAE During Training', fontweight='bold')
ax2.legend()
ax2.grid(True, alpha=0.3)

# 3. Time series - Test set predictions
ax3 = fig.add_subplot(gs[1, :])
test_times = test_data.index
ax3.plot(test_times, y_test_true, label='Actual DO', alpha=0.7, linewidth=1.5)
ax3.plot(test_times, y_test_pred, label='Predicted DO', alpha=0.7, linewidth=1.5)
ax3.set_xlabel('Time')
ax3.set_ylabel('DO (% saturation)')
ax3.set_title(f'Test Set: Actual vs Predicted DO (R² = {test_r2:.4f})', fontsize=12, fontweight='bold')
ax3.legend()
ax3.grid(True, alpha=0.3)

# 4. Scatter plot - Test predictions
ax4 = fig.add_subplot(gs[2, 0])
ax4.scatter(y_test_true, y_test_pred, alpha=0.3, s=20, color='orange')
min_val = min(y_test_true.min(), y_test_pred.min())
max_val = max(y_test_true.max(), y_test_pred.max())
ax4.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Perfect prediction')
ax4.set_xlabel('Actual DO (% saturation)')
ax4.set_ylabel('Predicted DO (% saturation)')
ax4.set_title(f'Test Set: Predictions vs Actual\\nR² = {test_r2:.4f}, MAE = {test_mae:.4f}', fontweight='bold')
ax4.legend()
ax4.grid(True, alpha=0.3)
ax4.set_aspect('equal', adjustable='box')

# 5. Residual plot
ax5 = fig.add_subplot(gs[2, 1])
residuals = y_test_true - y_test_pred
ax5.scatter(y_test_pred, residuals, alpha=0.3, s=20, color='orange')
ax5.axhline(y=0, color='r', linestyle='--', linewidth=2)
ax5.set_xlabel('Predicted DO (% saturation)')
ax5.set_ylabel('Residuals')
ax5.set_title('Test Set: Residual Plot', fontweight='bold')
ax5.grid(True, alpha=0.3)

plt.suptitle('LSTM Baseline Model: Dissolved Oxygen Prediction Performance',
             fontsize=14, fontweight='bold', y=0.995)

plot_path = RESULTS_DIR / 'lstm_performance.png'
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"✓ Performance plot saved: {plot_path}")

plt.close()

# ============================================================================
# FINAL SUMMARY
# ============================================================================

print("\n" + "="*70)
print("EXECUTION COMPLETE!")
print("="*70)
print("\nGenerated files:")
print(f"  Models:      models/lstm_baseline_do.keras")
print(f"  Scalers:     models/scaler_X.pkl, scaler_y.pkl")
print(f"  Metadata:    models/lstm_baseline_do_info.json")
print(f"  History:     models/lstm_baseline_do_history.csv")
print(f"  Results:     results/lstm_predictions_test.csv")
print(f"  Plot:        results/lstm_performance.png")
print(f"  Data:        data/processed/exo2_data.feather")
print("\n" + "="*70)
