# IMTA Analytics Package

**Version:** 0.1.0  
**Date:** November 4, 2025  
**Status:** Alpha - Active Development

## Overview

The `imta_analytics` package provides a reusable Python library for working with Integrated Multi-Trophic Aquaculture (IMTA) monitoring data. It consolidates data loading, quality control, and analysis functions that can be used across Jupyter notebooks, scripts, and eventually web applications.

## Installation

From the project root directory:

```bash
# Activate your conda environment
conda activate imta-analytics

# Install in editable/development mode
pip install -e .
```

This installs the package so you can:
- Import it from any Python script or notebook
- Edit the source code and see changes immediately (no reinstall needed)
- Use it as a foundation for web applications

## Current Features

### Data Loading (v0.1.0)

#### `load_toa5_file(filepath)`

Load Campbell Scientific TOA5 format files with proper type inference.

**Returns:**
- `df` (DataFrame): Data with proper numeric types (int64/float64) and datetime TIMESTAMP
- `metadata` (dict): Station name, logger model, OS version, program signature, etc.
- `units` (list): Unit strings for each column

**Key Features:**
- Solves the "line 4 type inference" problem (skips the "Smp" strings)
- Explicitly converts all non-TIMESTAMP columns to numeric types
- Handles sensor error codes gracefully (converts to NaN)
- Returns metadata and units separately for reference

**Example:**
```python
from imta_analytics.data import load_toa5_file

df, metadata, units = load_toa5_file('data/UNH-G2000B_EXO2SumData.dat')
print(f"Station: {metadata['station']}")
print(f"Shape: {df.shape}")
print(df.dtypes)  # All numeric except TIMESTAMP
```

#### `apply_marine_quality_filters(df)`

Remove sensor error codes and physically impossible values.

**Physical Bounds:**
- Temperature: -2 to 35°C
- pH: 6.5 to 9.5
- Salinity: 0 to 40 psu
- Dissolved Oxygen: 0 to 150% saturation
- Conductivity: 0 to 70 mS/cm
- Turbidity: 0 to 1000 FNU
- Chlorophyll: 0 to 200 μg/L
- Depth: 0 to 100 m

**Example:**
```python
from imta_analytics.data.loaders import apply_marine_quality_filters

df_clean = apply_marine_quality_filters(df)
print(f"Removed {len(df) - len(df_clean)} invalid records")
```

## Module Structure

```
imta_analytics/
├── __init__.py              # Package initialization
│   └── Exports: load_toa5_file
│
├── data/                    # Data loading and parsing
│   ├── __init__.py          # Exports: load_toa5_file
│   └── loaders.py           # TOA5 loader, quality filters
│
├── quality/                 # Data quality checks (future)
├── analysis/                # Analysis functions (future)
└── web/                     # Web application (future)
```

## Usage in Notebooks

The EDA notebook (`notebooks/01_initial_data_exploration.ipynb`) now uses the package:

```python
# Instead of defining load_toa5_file() inline, just import it:
from imta_analytics.data import load_toa5_file

# Use it the same way:
exo2_df, exo2_meta, exo2_units = load_toa5_file(EXO2_FILE)
```

**Benefits:**
- Cleaner notebooks (no 50-line function definitions)
- Consistent behavior across all notebooks
- Easy to update in one place
- Can be imported by web apps, scripts, APIs

## Roadmap

### v0.2.0 (Future)
- [ ] Data quality module (`imta_analytics.quality`)
  - Statistical outlier detection (IQR, Z-score)
  - Time series gap detection
  - Sensor drift detection
- [ ] ADCP current profile utilities
  - Load ZCell data
  - Vertical profile visualization
  - Current speed/direction analysis

### v0.3.0 (Future)
- [ ] Analysis module (`imta_analytics.analysis`)
  - Time series decomposition (trend, seasonal, residual)
  - Correlation analysis
  - Tidal signal extraction
- [ ] Plotting utilities
  - Standard water quality plots
  - Current profile heatmaps
  - Multi-parameter dashboards

### v0.4.0 (Future)
- [ ] Web application (`imta_analytics.web`)
  - FastAPI backend
  - Real-time data ingestion
  - REST API for model predictions
- [ ] Database integration
  - PostgreSQL + TimescaleDB
  - Automated ETL pipelines

### v1.0.0 (Future)
- [ ] Machine learning models
  - Growth prediction models
  - Environmental forecasting
  - Anomaly detection
- [ ] Production deployment
  - Docker containerization
  - CI/CD pipelines
  - Documentation site

## Development

### Running Tests

```bash
pytest tests/  # Not yet implemented
```

### Code Style

Follow PEP 8 guidelines. Use type hints where possible:

```python
def load_toa5_file(filepath: Union[str, Path]) -> Tuple[pd.DataFrame, Dict[str, str], List[str]]:
    """Load TOA5 file."""
    ...
```

### Adding New Features

1. Create a new module or add to existing module
2. Update `__init__.py` to export public functions
3. Add docstrings with examples
4. Update this CHANGELOG.md
5. Test in a notebook before committing

## Technical Notes

### Why Skip Line 4?

TOA5 files have this structure:
```
Line 1: "TOA5","Station","Logger",...     <- Metadata
Line 2: "TIMESTAMP","RECORD","Temp",...   <- Column names
Line 3: "TS","RN","°C",...                <- Units
Line 4: "","","Smp","Smp","Smp",...       <- Processing type (THIS IS THE PROBLEM!)
Line 5+: 2024-12-15 00:00:00,1,18.5,...   <- Data
```

If pandas sees line 4 (all "Smp" strings), it infers that **all columns are strings**. Our solution:
1. Skip all 4 header lines: `skiprows=4`
2. Read column names separately: `pd.read_csv(skiprows=1, nrows=1)`
3. Explicitly set column names: `names=headers`
4. Force numeric conversion: `pd.to_numeric(df[col], errors='coerce')`

### Sensor Error Codes

Campbell Scientific/YSI sensors return these codes for failures:
- `143052` - Common EXO2 error
- `193039` - Sensor communication error
- `91625` - Out-of-range measurement
- `-86.48` - Calibration error

These appear as **numeric values** in the CSV, so basic `pd.read_csv()` won't catch them. Use `apply_marine_quality_filters()` to remove them.

## Questions?

- Package issues: Check import paths, run `pip install -e .` again
- Data loading issues: See `docs/data-format-analysis.md`
- Sensor error codes: See `refs/technical/README.md`

## Changelog

### v0.1.0 (2025-11-04)

**Added:**
- Initial package structure
- `load_toa5_file()` function with proper type inference
- `apply_marine_quality_filters()` for data cleaning
- Setup.py for pip installation
- Package README and documentation

**Fixed:**
- TOA5 line 4 type inference issue
- Sensor error codes appearing in data
- Notebooks now import from package instead of inline definitions

**Known Issues:**
- No automated tests yet
- Documentation needs expansion
- Type hints incomplete
