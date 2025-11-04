# UNH Aquafort Data Format Analysis

**Date:** November 4, 2025  
**Updated:** November 4, 2025  
**Analyst:** GitHub Copilot  
**Project:** IMTA Analytics - UNH Aquafort Buoy Station

## Executive Summary

The UNH Aquafort team has provided two data files from their buoy station monitoring system. Both files are in **Campbell Scientific TOA5 format**, a specialized text-based format commonly used in environmental data logging applications. These files can be successfully loaded using **Python's pandas library** with a custom parser.

**Update (Nov 4, 2025):** After extensive debugging, we identified critical type inference issues caused by TOA5 line 4 containing "Smp" strings. We also discovered sensor error codes (143052, 193039, 91625, -86.48) that required data cleaning with physical bounds for marine parameters. The final solution uses `skiprows=4` with explicit `pd.to_numeric()` conversion. A Python module (`imta_analytics`) has been created for reusable data loading functionality.

## File Analysis

### File 1: UNH-G2000B_EXO2SumData.dat

**Magic Number / File Type:**
```
Unicode text, UTF-8 text, with CRLF line terminators
```

**Format:** Campbell Scientific TOA5

**Contents:**
- **Data Type:** Water quality monitoring data from EXO2 sonde
- **Parameters Measured:**
  - pH and pH (mV)
  - Temperature (°C)
  - Specific Conductivity (mS/cm)
  - Salinity (psu)
  - Turbidity (FNU)
  - Chlorophyll (RFU and μg/L)
  - Blue-Green Algae Phycoerythrin (RFU and μg/L)
  - Dissolved Oxygen (% Saturation and mg/L)
  - Depth (m)
  - Internal and External Power (V)

**Structure:**
```
Line 1: "TOA5","UNH-G2000B","CR1000X","50927","CR1000X.Std.06.02",...
Line 2: "TIMESTAMP","RECORD","EXO2Date","EXO2Time","EXO2pH",...
Line 3: "TS","RN","","","","mV","QSU","ºC","mS/cm","psu","FNU",...
Line 4: "","","Smp","Smp","Smp","Smp","Smp","Smp",...
Line 5+: Data records (CSV format)
```

### File 2: UNH-G2000B_ZCelEngData.dat

**Magic Number / File Type:**
```
Unicode text, UTF-8 text, with very long lines (921), with CRLF line terminators
```

**Format:** Campbell Scientific TOA5

**Contents:**
- **Data Type:** Current profiler (ADCP) and engineering data from ZCell sensor
- **Parameters Measured:**
  - Battery voltage (Volts)
  - Panel temperature (°C)
  - Record length and date strings
  - Error and status codes
  - Speed of sound (m/s)
  - Heading, Pitch, Roll (degrees)
  - Pressure (dBar)
  - Water Temperature (°C)
  - Analog inputs
  - **20 depth bins** with:
    - Depth (m)
    - Current Speed (m/s)
    - Current Direction (degrees)

**Structure:**
```
Line 1: "TOA5","UNH-G2000B","CR1000X","50927",...
Line 2: "TIMESTAMP","RECORD","batt_volt","PTemp","ZCelRecLen",...
       "ZCelDpth1","CurrSpd1","CurrDir1",...,"ZCelDpth20","CurrSpd20","CurrDir20"
Line 3: "TS","RN","Volts","ºC","","","","","Volts","m/s","º",...
Line 4: "","","Smp","Smp","Smp","Smp","Smp",...
Line 5+: Data records (CSV format with 77 columns)
```

## Python Module Recommendations

### Primary: pandas
**Recommended** ✓

```python
import pandas as pd
from imta_analytics.data import load_toa5_file

# Load TOA5 data with proper type inference
df, metadata, units = load_toa5_file('path/to/file.dat')
```

**Pros:**
- Native CSV parsing capabilities
- Excellent datetime handling
- Rich data manipulation features
- Handles UTF-8 and CRLF line endings automatically
- Efficient for medium to large datasets

**Critical Implementation Notes:**
1. **Type Inference Issue:** Line 4 of TOA5 files contains all "Smp" strings, which confuses pandas type inference
2. **Solution:** Use `skiprows=4` with `header=None` and `names=headers`, then explicitly convert columns with `pd.to_numeric()`
3. **Data Quality:** Sensor error codes (143052, 193039, 91625, -86.48) appear as numeric values and require filtering
4. **Cleaning:** Apply physical bounds for marine parameters (temp: -2 to 35°C, pH: 6.5-9.5, salinity: 0-40 psu)

### Alternative: numpy
**Suitable for specific use cases**

```python
import numpy as np

# For numerical analysis of specific columns
data = np.genfromtxt(filepath, delimiter=',', skip_header=4, 
                     usecols=[2,3,4], encoding='utf-8')
```

**Pros:**
- Fast for numerical operations
- Lower memory footprint
- Good for array-based computations

**Cons:**
- Requires more manual handling of headers and types
- Less convenient for mixed data types

### Not Recommended: Binary format libraries
- ❌ h5py - Not applicable (not HDF5)
- ❌ netCDF4 - Not applicable (not NetCDF)
- ❌ scipy.io - Not applicable (not MATLAB/Fortran binary)
- ❌ pickle - Not applicable (not Python serialized)

## TOA5 Format Specification

### Header Structure

**Line 1: File Information**
```
"TOA5","Station_Name","Logger_Model","Serial_Number","OS_Version","Program_Name","Signature","Table_Name"
```

**Line 2: Column Names**
```
"TIMESTAMP","RECORD","Column1","Column2",...
```

**Line 3: Units**
```
"TS","RN","unit1","unit2",...
```

**Line 4: Processing/Sampling**
```
"","","Smp","Avg","Max",...
```

### Data Section (Line 5+)
- Standard CSV format
- Quoted strings for text fields
- Numeric values unquoted
- CRLF line endings (Windows style)
- UTF-8 encoding

## Setup Instructions

### 1. Create Conda Environment

```bash
# Create environment from YAML file
conda env create -f environment.yml

# Activate environment
conda activate imta-analytics

# Register Jupyter kernel
python -m ipykernel install --user --name imta-analytics --display-name "Python (imta-analytics)"
```

### 2. Load Data in Python

```python
from pathlib import Path
from imta_analytics.data import load_toa5_file

# Load TOA5 files with proper type inference
exo2_df, exo2_meta, exo2_units = load_toa5_file(
    'data/aquafort-buoy-station/UNH-G2000B_EXO2SumData.dat'
)
zcel_df, zcel_meta, zcel_units = load_toa5_file(
    'data/aquafort-buoy-station/UNH-G2000B_ZCelEngData.dat'
)

# The loader returns:
# - df: DataFrame with proper numeric types (int64/float64)
# - metadata: dict with station info, logger model, OS version, etc.
# - units: list of unit strings for each column
```

The `load_toa5_file` function is now available in the `imta_analytics.data` module and handles:
- Proper type inference (skips problematic line 4 with "Smp" strings)
- Explicit numeric conversion with `pd.to_numeric(errors='coerce')`
- TIMESTAMP parsing to datetime objects
- Metadata and units extraction

## Data Characteristics

### Temporal Coverage
- **Time Period:** December 2024 (approximately 1 day of data visible in sample)
- **Sampling Frequency:** 
  - EXO2: ~15 minute intervals
  - ZCell: ~10 minute intervals
- **Time Format:** ISO 8601 (YYYY-MM-DD HH:MM:SS)

### Data Quality Observations
1. **Duplicate Records:** Some duplicate timestamps present in EXO2 data
2. **Missing Values:** Minimal missing data observed
3. **Encoding:** Clean UTF-8 text, no corruption detected
4. **Line Endings:** Windows-style CRLF (handled automatically by pandas)
5. **Sensor Error Codes:** Large numeric values indicate sensor failures:
   - `143052` - Common EXO2 sensor error
   - `193039` - Another EXO2 error code
   - `91625` - Sensor failure indicator
   - `-86.48` - Out-of-range reading
6. **Invalid Data:** ~4-6% of readings fall outside physical bounds for marine parameters
7. **Data Cleaning Required:** Apply physical bounds filtering before analysis

## Integration with Existing Codebase

The custom TOA5 loader has been extracted into a reusable Python module:
- **Module:** `imta_analytics.data`
- **Location:** `imta_analytics/data/loaders.py`
- **Function:** `load_toa5_file(filepath)`
- **Returns:** DataFrame, metadata dict, units list
- **Notebook Usage:** `notebooks/01_initial_data_exploration.ipynb` now imports from module

The `imta_analytics` package is structured for future expansion:
```
imta_analytics/
├── __init__.py
├── data/
│   ├── __init__.py
│   └── loaders.py      # TOA5 and other data format loaders
├── quality/            # Future: data quality checks
├── analysis/           # Future: analysis functions
└── web/                # Future: web application / API
```

### Recommended Workflow

1. **Initial Exploration:** Use the EDA notebook
2. **Data Cleaning:** Create processing pipeline to handle duplicates
3. **Feature Engineering:** Extract tidal phases, stratification indicators
4. **Analysis:** Time series analysis, correlation studies
5. **Modeling:** Predictive models for water quality and current patterns

## References

- **Campbell Scientific TOA5 Format:** Standard ASCII data format for CR1000X series dataloggers
- **EXO2 Sonde:** Multi-parameter water quality sonde
- **ZCell ADCP:** Acoustic Doppler Current Profiler with vertical profiling

## Next Steps

1. ✅ Environment setup complete (`imta-analytics` conda env)
2. ✅ Jupyter kernel registered
3. ✅ EDA notebook created with TOA5 loader
4. ✅ Type inference debugging resolved (skiprows=4 + explicit conversion)
5. ✅ Data quality analysis (identified sensor error codes)
6. ✅ Data cleaning procedure (physical bounds for marine parameters)
7. ✅ Technical documentation downloaded (5 PDFs, 52 MB)
8. ✅ Created `imta_analytics` Python module with data loader
9. ⏭️ Continue EDA analysis with cleaned data
10. ⏭️ Advanced analysis (tidal patterns, correlations, ADCP profiles)
11. ⏭️ Build web application / dashboard (future)
12. ⏭️ Implement real-time data processing daemon (future)
