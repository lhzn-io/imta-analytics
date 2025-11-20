# IMTA Analytics - Model Artifacts

This directory contains trained model artifacts. Binary files (`.h5`, `.pkl`) are excluded from git via `.gitignore`.

## Baseline LSTM Model (v0.1)

**Status**: ARCHIVED - November 20, 2025  
**Purpose**: Reference baseline, NOT for production deployment  
**Critical Issues**: 11% train-test gap, flawed validation methodology

### Artifacts

- `lstm_baseline_do.h5` (286 KB) - Trained Keras model
- `scaler_do.pkl` (1.3 KB) - MinMaxScaler for feature normalization
- `lstm_baseline_metadata.json` (1.2 KB) - Model configuration and metrics

### Performance Metrics

| Metric | Training | Test | Literature Target |
|--------|----------|------|-------------------|
| R² | 0.9389 | **0.8300** | > 0.85 (0.90-0.93) |
| MAE | - | 3.31% sat | < 0.6% sat |
| RMSE | - | 3.78% sat | < 1.0% sat |

**Train-Test Gap**: 10.9% (indicates overfitting)

### Architecture

```python
Sequential([
    LSTM(64, activation='elu'),
    Dropout(0.001),
    Dense(1, activation='linear')
])
```

- Optimizer: Adam (lr=0.01)
- Loss: MSE
- Epochs: 11 (early stopping)
- Features: 22 (7 base + 12 lags + 4 temporal)

### Known Limitations

**DO NOT use for production deployment** - the following issues must be addressed:

1. **Overfitting**: 11% train-test performance gap
2. **No Cross-Validation**: Single train/test split, no temporal stability evidence
3. **Validation Methodology Flaw**: Keras `validation_split=0.2` uses easier interpolation task
4. **Insufficient Regularization**: Dropout = 0.001 (essentially none)
5. **No External Validation**: Untested on different years, sites, or conditions

### Reproduction

To reproduce this baseline:

```bash
conda activate imta-analytics
jupyter nbconvert --to notebook --execute \
  notebooks/02_baseline_do_prediction_lstm.ipynb
```

**Seeds**: NumPy=42, TensorFlow=42  
**Expected**: R² = 0.8300 ± 0.01

### Next Version (v0.2) Requirements

Must address before production deployment:

- [ ] Temporal cross-validation (5 folds)
- [ ] Interleaved train/test split
- [ ] Increased regularization (dropout ≥ 0.1)
- [ ] Residual diagnostics (ACF/PACF)
- [ ] Train-test gap < 5%

**Target Date**: December 18, 2025

### References

- Analysis: `docs/analysis/20251113-lstm-baseline-do-prediction.md`
- Notebook: `notebooks/02_baseline_do_prediction_lstm.ipynb`
- Visualization: `docs/analysis/lstm_baseline_results.png`

---

**Last Updated**: November 20, 2025  
**Next Review**: December 18, 2025 (v0.2 completion)
