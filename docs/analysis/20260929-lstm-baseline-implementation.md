---
title: "LSTM Baseline Model for DO Prediction - Implementation Report"
subtitle: "Baseline Deep Learning Model for Dissolved Oxygen Forecasting"
author: "IMTA Analytics Team"
date: "September 29, 2026"
---

**Project:** IMTA Analytics - UNH Aquafort Buoy Station  
**Model Type:** LSTM Baseline  
**Previous Analysis:** [20251113-data-exploration-findings.md](20251113-data-exploration-findings.md)

## Executive Summary

This document describes the implementation of a baseline Long Short-Term Memory (LSTM) neural network for predicting dissolved oxygen (DO) levels in the UNH Aquafort IMTA system. The model serves as a performance benchmark for future advanced architectures.

**Implementation Status:** Trained and evaluated on 2026-10-03; see Section 11 for results.

**Key Deliverables:**
- Pipeline script: `scripts/run_lstm_baseline.py`
- Jupyter notebook: `notebooks/baseline_do_prediction_lstm.ipynb`
- Model architecture based on literature best practices (Barzegar et al. 2020)
- Comprehensive evaluation framework
- Model persistence and deployment readiness

## 1. Background and Literature Review

### 1.1 Performance Benchmarks

Based on recent literature in aquaculture DO prediction:

**Barzegar et al. (2020) - CNN-LSTM Deep Learning Model:**
- R² = 0.90-0.93 for DO prediction
- RMSE < 1.0 mg/L
- MAE < 0.6 mg/L
- Architecture: Hybrid CNN-LSTM with dropout regularization

**Xu et al. (2025) - Hybrid Deep Learning Framework:**
- State-of-the-art: CNN-SA-BiSRU architecture
- R² = 0.93 for real-time DO prediction
- Advanced features: Self-attention, bidirectional processing

### 1.2 Target Performance

**Baseline Target:** R² > 0.85
**Strong Performance:** R² > 0.90 (literature benchmark)

## 2. Data Characteristics

### 2.1 Source Data

From [20251113-data-exploration-findings.md](20251113-data-exploration-findings.md):

**EXO2 Water Quality Data:**
- **Duration:** January-October 2025 (~9 months)
- **Sampling Rate:** 15 minutes (96 samples/day)
- **Total Records:** ~35,000-40,000 (>95% valid after QC)
- **DO Statistics:**
  - Mean: 103.80% saturation
  - Std Dev: 6.62%
  - Range: 60-140% (post-cleaning)

**Data Quality:**
- Campbell Scientific sentinel values converted to NaN
- Physical bounds filtering applied
- Processed feather files available for fast loading

### 2.2 Suitability for LSTM

✓ **15-minute sampling rate** - Ideal for LSTM (within 10-30 min recommended range)  
✓ **>2000 samples** - Sufficient training data  
✓ **Temporal continuity** - Excellent coverage with minimal gaps  
✓ **Multiple features** - Temperature, salinity, pH, chlorophyll, turbidity, depth

## 3. Model Architecture

### 3.1 Network Design

Based on Barzegar et al. (2020) baseline LSTM:

```
Input Layer
  ↓
  Shape: (timesteps=1, features=22)
  ↓
LSTM Layer (64 neurons, ELU activation)
  ↓
Dropout (rate=0.001)
  ↓
Dense Output (1 neuron, linear activation)
```

**Hyperparameters:**
- LSTM units: 64
- Activation: ELU (Exponential Linear Unit)
- Dropout rate: 0.001
- Optimizer: Adam (learning rate = 0.01)
- Loss function: MSE (Mean Squared Error)
- Batch size: 64
- Epochs: 100 (with early stopping)

### 3.2 Rationale

- **Single LSTM layer:** Baseline simplicity, faster training
- **64 neurons:** Literature-recommended for water quality prediction
- **ELU activation:** Better gradient flow than ReLU for time series
- **Low dropout (0.001):** Minimal regularization, following Barzegar et al.
- **Adam optimizer:** Adaptive learning rate, industry standard

## 4. Feature Engineering

### 4.1 Input Features

**Physical Water Quality Parameters:**
1. `EXO2Temp` - Temperature (°C)
   - Strong inverse correlation with DO solubility
2. `EXO2Salinity` - Salinity (psu)
   - Affects DO solubility
3. `EXO2pH` - pH
   - Linked to photosynthesis/respiration cycles
4. `EXO2Chlor` - Chlorophyll (RFU)
   - Indicator of photosynthetic activity
5. `EXO2Turb` - Turbidity (FNU)
   - Affects light availability for photosynthesis
6. `EXO2Depth` - Depth (m)
   - Stratification indicator

**Temporal Features (Circular Encoding):**
7-8. `hour_sin`, `hour_cos` - Hour of day (0-23)
   - Captures diurnal cycles (photosynthesis, respiration)
9-10. `doy_sin`, `doy_cos` - Day of year (1-365)
   - Captures seasonal patterns

**Lag Features (Historical DO):**
11-22. `DO_lag_1` through `DO_lag_12`
   - Captures 1-3 hours of history (at 15-min intervals)
   - Autoregressive component crucial for time series prediction

**Total Features:** 22

### 4.2 Normalization

Min-Max scaling to [0, 1] range:
```
x' = (x - x_min) / (x_max - x_min)
```

**Critical:** Scalers fitted ONLY on training data to prevent data leakage!

### 4.3 Temporal Encoding Rationale

Circular encoding for cyclical features prevents discontinuities:
- Hour 23 → Hour 0: Without circular encoding, distance = 23
- With sin/cos encoding: smooth transition

Formula:
```
hour_sin = sin(2π × hour / 24)
hour_cos = cos(2π × hour / 24)
```

## 5. Training Methodology

### 5.1 Train/Test Split

**Method:** Chronological split (NO shuffling!)
- Training: 80% (first ~21,000 samples)
- Testing: 20% (last ~5,000 samples)

**Rationale:** Time series require temporal order preservation to:
- Prevent data leakage from future to past
- Evaluate true forecasting performance
- Simulate real-world deployment scenario

### 5.2 Training Configuration

```python
EPOCHS = 100
BATCH_SIZE = 64
VALIDATION_SPLIT = 0.2  # From training set
```

**Callbacks:**
- **Early Stopping:**
  - Monitor: validation loss
  - Patience: 15 epochs
  - Restore best weights
- **Reduce Learning Rate on Plateau:**
  - Factor: 0.5
  - Patience: 5 epochs
  - Min LR: 0.0001

### 5.3 Computational Requirements

- Training time: ~5-10 minutes (CPU) / ~1-2 minutes (GPU)
- Model size: ~50KB (very efficient)
- Inference time: <10ms per prediction

## 6. Evaluation Framework

### 6.1 Performance Metrics

**Primary Metric:**
- **R² (Coefficient of Determination)**
  - Measures proportion of variance explained
  - Target: > 0.85 (baseline), > 0.90 (strong)

**Secondary Metrics:**
- **MAE (Mean Absolute Error)**
  - Average prediction error magnitude
  - Target: < 0.6 mg/L ≈ 6% saturation
- **RMSE (Root Mean Squared Error)**
  - Penalizes large errors more heavily
  - Target: < 1.0 mg/L ≈ 10% saturation

### 6.2 Visualizations

The notebook generates comprehensive evaluation plots:

1. **Time Series Comparison**
   - Actual vs predicted DO over time
   - Training set (first 1000 samples for clarity)
   - Test set (all samples)

2. **Scatter Plots**
   - Predicted vs actual DO
   - Perfect prediction reference line
   - Visual R² assessment

3. **Residual Analysis**
   - Residuals vs predicted values
   - Residual distribution histograms
   - Mean and variance assessment

4. **Feature Importance**
   - Correlation between features and prediction errors
   - Identifies which features contribute most to accuracy

5. **Training History**
   - Loss curves (training vs validation)
   - MAE evolution over epochs
   - Early stopping effectiveness

## 7. Implementation Details

### 7.1 Notebook Structure

**Location:** `notebooks/baseline_do_prediction_lstm.ipynb`

**Sections:**
1. Setup and Imports
2. Data Loading (from processed feather files)
3. Data Preparation and Feature Engineering
4. Build LSTM Model
5. Train Model
6. Model Evaluation
7. Save Model and Results
8. Summary and Next Steps

### 7.2 Dependencies

```python
# Core libraries
pandas >= 1.5.0
numpy >= 1.23.0

# Deep learning
tensorflow >= 2.10.0
keras (included in TensorFlow)

# Machine learning utilities
scikit-learn >= 1.1.0

# Visualization
matplotlib >= 3.6.0
seaborn >= 0.12.0
```

### 7.3 Model Artifacts

The notebook saves:

1. **Trained Model:** `models/lstm_baseline_do.keras`
   - TensorFlow/Keras format
   - Loadable with `keras.models.load_model()`

2. **Scalers:** `models/scaler_X.pkl`, `models/scaler_y.pkl`
   - Pickle format
   - Required for production inference

3. **Model Info:** `models/lstm_baseline_do_info.json`
   - Architecture parameters
   - Training configuration
   - Performance metrics
   - Feature list

4. **Training History:** `models/lstm_baseline_do_history.csv`
   - Loss and metric values per epoch
   - For post-training analysis

## 8. Expected Results and Interpretation

### 8.1 Performance Targets

**Baseline Success (R² > 0.85):**
- Model captures majority of DO variance
- Suitable for aquaculture monitoring applications
- Ready for deployment testing

**Strong Performance (R² > 0.90):**
- Matches literature benchmarks
- Excellent predictive capability
- Competitive with advanced architectures

**Needs Improvement (R² < 0.85):**
- May indicate data quality issues
- Could require hyperparameter tuning
- Consider advanced architectures

### 8.2 Residual Analysis Interpretation

**Ideal Residuals:**
- Mean ≈ 0 (unbiased predictions)
- Constant variance (homoscedastic)
- Normally distributed
- No patterns in residual plots

**Warning Signs:**
- Non-zero mean: systematic bias
- Increasing variance: heteroscedasticity
- Patterns in residuals: missing features or non-linearity

## 9. Next Steps

### 9.1 If Performance Meets Baseline (R² > 0.85)

**Advanced Architectures:**
1. **CNN-LSTM Hybrid** (Barzegar et al. 2020)
   - Convolutional layers for feature extraction
   - LSTM layers for temporal dependencies
   - Expected improvement: +2-5% R²

2. **CNN-SA-BiSRU** (Xu et al. 2025)
   - State-of-the-art architecture
   - Self-attention mechanism
   - Bidirectional processing
   - Expected R² > 0.93

**Feature Enhancement:**
- Cross-correlation with ZCell current data
- Rolling statistics (30-min, 1-hour windows)
- Derived features (water density, Richardson number)

**Hyperparameter Optimization:**
- Grid search or Bayesian optimization
- LSTM units: [32, 64, 128]
- Dropout rates: [0.001, 0.01, 0.1]
- Learning rates: [0.001, 0.01, 0.1]

### 9.2 If Performance Below Baseline (R² < 0.85)

**Immediate Actions:**
1. Verify data quality and temporal gaps
2. Increase lag window (24 lags = 6 hours)
3. Add ZCell features (current speed/direction)
4. Check for seasonal patterns (separate models?)

**Data Investigation:**
- Temporal continuity assessment
- Outlier detection and treatment
- Feature correlation re-analysis
- Train/test split validation

### 9.3 Deployment Preparation

**Production Inference Pipeline:**
1. Load trained model and scalers
2. Accept new sensor readings (last 3 hours)
3. Apply feature engineering
4. Normalize inputs
5. Generate prediction
6. Inverse transform output
7. Return DO forecast

**Real-Time Integration:**
- Model size: ~50KB (edge-deployable)
- Inference latency: <10ms
- Update frequency: Every 15 minutes
- Input requirements: Last 12 readings (3 hours)

## 10. References

### 10.1 Literature

**Primary References:**
1. **Xu, Y., et al. (2025).** "Hybrid deep learning framework for real-time dissolved oxygen prediction in aquaculture." *Aquacultural Engineering*.
   - Location: `refs/publications/Xu et. al. - 2025 - Hybrid deep learning framework for real-time DO prediction in aquaculture.md`

2. **Barzegar, R., et al. (2020).** "Short-term water quality variable prediction using a hybrid CNN-LSTM deep learning model." *Stochastic Environmental Research and Risk Assessment*.
   - Location: `refs/publications/Barzegar et. al. - 2020 - Short-term water quality variable prediction using a hybrid CNN-LSTM deep learning model.md`

### 10.2 Project Documentation

- **Data Format Analysis:** `docs/analysis/20251104-data-format-analysis.md`
- **Data Exploration Findings:** `docs/analysis/20251113-data-exploration-findings.md`
- **Predictive Features Catalog:** `docs/living/predictive-features-catalog.md`

### 10.3 Code Resources

- **Data Loaders:** `imta_analytics/data/loaders.py`
- **Analysis Utilities:** `imta_analytics/analysis/`
- **Notebook Utilities:** `imta_analytics/notebook_utils.py`

## 11. Technical Notes

### 11.1 Reproducibility

Random seeds set for reproducibility:
```python
np.random.seed(42)
tf.random.set_seed(42)
```

### 11.2 Data Assumptions

1. **Temporal Continuity:** 15-minute intervals maintained
2. **Quality Control:** Processed feather files already cleaned
3. **No Gaps:** Lag features require continuous data
4. **Stationary Target:** DO distribution similar across train/test

### 11.3 Limitations

1. **Single-Site Model:** Trained on UNH Aquafort data only
2. **Seasonal Coverage:** 9 months may not capture all seasonal patterns
3. **Single-Depth:** EXO2 measures at fixed depth
4. **No Multi-Step Forecasting:** Predicts t+1 only (15 minutes ahead)

### 11.4 Future Enhancements

- Multi-step ahead forecasting (1 hour, 6 hours, 24 hours)
- Multi-output prediction (DO + temperature + pH)
- Ensemble methods (multiple LSTM models)
- Transfer learning to other aquaculture sites

---

**Document Status:** Initial Implementation  
**Last Updated:** September 29, 2026  
**Next Review:** After model training and evaluation completion

**Related Documents:**
- Implementation Notebook: `notebooks/baseline_do_prediction_lstm.ipynb`
- Model Artifacts: `models/lstm_baseline_do.*`
- Data Analysis: `docs/analysis/20251113-data-exploration-findings.md`

## 11. Results (Run of 2026-10-03)

### 11.1 Initial Run: Outlier Contamination

The first training run (41 epochs with early stopping) reported a test R² of 0.9489. That figure was an artefact of three `EXO2DO` values that survived cleaning: 184,541% and 171,545% saturation (physically impossible) and 0.00%. They compressed the min-max scaled normal range to roughly 0.0005 of [0, 1], and the model learned to predict the outliers. On the normal operating range (80 to 130% saturation) the same model scored R² = -11.92 with MAE 16.92% saturation, and produced 126 predictions above 200% or below -100%.

The cause was that cleaning removed only the -7999 sentinel value and applied no physical bounds.

### 11.2 Physical Bounds Filtering

`scripts/run_lstm_baseline.py` now drops rows outside these ranges before feature engineering:

| Variable | Valid Range |
| :--- | :--- |
| `EXO2DO` | 60 to 140% saturation |
| `EXO2Temp` | 0 to 35 °C |
| `EXO2Salinity` | 0 to 40 psu |
| `EXO2pH` | 6.5 to 9.5 |
| `EXO2Chlor` | 0 to 100 RFU |
| `EXO2Turb` | 0 to 100 FNU |
| `EXO2Depth` | 0 to 20 m |

This removed 2,024 rows (3.29%), 8 of them for `EXO2DO`, leaving 59,545 samples.

### 11.3 Retrained Baseline

Trained for 42 epochs on 47,636 samples and tested on 11,909, with 22 features (6 sensor variables, 4 temporal encodings, 12 DO lags):

| Metric | Value |
| :--- | :--- |
| Test R² | 0.5240 |
| MAE | 3.30% saturation |
| RMSE | 4.58% saturation |
| Predictions within ±10% | 95% |
| Predictions outside the valid range | 6 |

Run metadata is recorded in `models/lstm_baseline_do_info.json`. The trained model and figures are not tracked in git.

### 11.4 Interpretation and Known Limitations

- R² of 0.52 is below the 0.85 baseline target. MAE is close to the archived v0.1 baseline (3.31%; see `models/README.md`), while R² is much lower; whether the v0.1 evaluation data contained the same outliers should be checked before v0.1 is used as a reference.
- Out-of-bounds rows are dropped before the lag features are built with `shift()`, so a lag can span a gap wherever rows were removed rather than exactly 15 minutes per step. Masking values and building lags on the regular 15-minute index would remove this bias.
- Next steps follow Section 9.2: add ZCell current features and evaluate the advanced architectures.
