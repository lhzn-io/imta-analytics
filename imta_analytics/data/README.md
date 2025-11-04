# IMTA Analytics - Data Loaders Module

## Overview

This module provides data loading and parsing functions for environmental monitoring systems used in Integrated Multi-Trophic Aquaculture (IMTA) research. The primary focus is on Campbell Scientific dataloggers and associated sensors.

## Supported Formats

### Campbell Scientific TOA5

The TOA5 (Table Output ASCII, version 5) format is used by Campbell Scientific dataloggers to record sensor data. These files have a specific structure that requires specialized parsing.

#### TOA5 File Structure

```text
"TOA5","UNH-G2000B","CR1000X","12345","CR1000X.Std.03.02","CPU:UNH_G2000B_2024.CR1X","59064","EXO2SumData"
"TIMESTAMP","RECORD","EXO2Temp","EXO2Salinity",...
"TS","RN","°C","psu",...
"","","Smp","Smp",...
"2024-08-01 00:00:00",0,18.5,28.3,...
```

- **Line 1:** Metadata (station, logger model, serial number, program, table name)
- **Line 2:** Column headers
- **Line 3:** Units for each measurement
- **Line 4:** Sampling information (e.g., "Smp", "Avg") - **CONFUSES PANDAS TYPE INFERENCE**
- **Line 5+:** CSV data

## Campbell Scientific NaN Sentinel Values

### Critical Implementation Detail

Campbell Scientific dataloggers **do not use IEEE NaN** for floating-point data. Instead, they use **data-type-specific sentinel values** to represent invalid measurements.

#### Sentinel Values by Data Type

| Data Type | NaN Representation | Range | Notes |
|-----------|-------------------|-------|-------|
| **FP2** (Float Point 2) | **-7999** | -7999 to +7999 | Most common for sensor data |
| **Long Integer** | **-2147483648** | -2³¹ to 2³¹-1 | Most negative 32-bit integer |
| **Overrange** | ±6999, ±7999 | N/A | Measurement exceeds range |

#### When NaN/Sentinel Values Occur

According to Campbell Scientific CR1000X documentation (Section 14.2):

> "NAN (not a number) and INF (infinite) are data words indicating an exceptional occurrence in data logger function or processing. NAN indicates an invalid measurement."

NaN sentinel values appear when:

1. **Input signals exceed voltage range** chosen for the measurement
2. **Invalid SDI-12 command** is sent to sensor
3. **SDI-12 sensor does not respond** or aborts without sending data
4. **Measurement overrange** - values exceed sensor specifications

#### Example from Real Data

```python
# Before processing with load_toa5_file():
df['EXO2Temp'] = [18.5, 19.2, -7999, 18.8, 19.1]  # -7999 is FP2 NaN

# After processing with load_toa5_file():
df['EXO2Temp'] = [18.5, 19.2, NaN, 18.8, 19.1]    # Proper pandas NaN
```

### Why This Matters

If you don't convert these sentinel values:

- Statistical calculations become invalid (mean, std include -7999)
- Plots show spurious spikes to -7999 or -2147483648
- Physical bounds checking may miss these values
- Data quality flags fail to identify invalid measurements

The `load_toa5_file()` function **automatically converts all Campbell Scientific sentinel values to proper NaN**.

## Usage

### Basic Loading

```python
from imta_analytics.data import load_toa5_file

# Load TOA5 file with automatic NaN conversion
df, metadata, units = load_toa5_file('data/UNH-G2000B_EXO2SumData.dat')

print(f"Station: {metadata['station']}")
print(f"Logger: {metadata['logger_model']}")
print(f"Table: {metadata['table_name']}")
print(f"Shape: {df.shape}")

# Campbell Scientific sentinels are now proper NaN
print(f"Missing temp values: {df['EXO2Temp'].isna().sum()}")
```

### With Quality Filtering

```python
from imta_analytics.data import load_toa5_file, apply_marine_quality_filters

# Load data
df, metadata, units = load_toa5_file('data/buoy_station.dat')

# Apply marine-specific physical bounds
df_clean = apply_marine_quality_filters(df)

print(f"Records after QC: {len(df_clean)}")
```

### Accessing Metadata

```python
df, metadata, units = load_toa5_file('data/sensor_data.dat')

# Metadata dictionary keys:
# - format: "TOA5"
# - station: Station/site identifier
# - logger_model: "CR1000X", "CR3000", etc.
# - serial_number: Logger serial number
# - os_version: Datalogger OS version
# - program: Program filename
# - signature: Program signature
# - table_name: Data table name

# Units list corresponds to DataFrame columns
for col, unit in zip(df.columns, units):
    print(f"{col}: {unit}")
```

## API Reference

### `load_toa5_file(filepath)`

Load a Campbell Scientific TOA5 format file with proper NaN handling.

**Parameters:**
- `filepath` (str or Path): Path to TOA5 .dat file

**Returns:**
- `df` (DataFrame): Loaded data with Campbell Scientific sentinels converted to NaN
- `metadata` (dict): File metadata from header
- `units` (list): Units for each column

**Key Features:**
- Automatic conversion of Campbell Scientific NaN sentinels (-7999, -2147483648, ±6999, ±7999)
- Explicit numeric type conversion (bypasses pandas type inference issues)
- DateTime parsing for TIMESTAMP column
- Metadata extraction from header

### `apply_marine_quality_filters(df)`

Apply physical bounds filtering for marine water quality parameters.

**Parameters:**
- `df` (DataFrame): DataFrame with water quality columns

**Returns:**
- `df_clean` (DataFrame): Filtered DataFrame with invalid readings removed

**Physical Bounds:**
- Temperature: -2 to 35°C
- pH: 6.5 to 9.5
- Salinity: 0 to 40 psu
- Dissolved Oxygen: 0 to 150% saturation
- Conductivity: 0 to 70 mS/cm
- Turbidity: 0 to 1000 FNU
- Chlorophyll: 0 to 200 μg/L
- Depth: 0 to 100 m

## Common Sensors

### YSI EXO2 Multiparameter Sonde

Water quality measurements connected to Campbell Scientific datalogger via SDI-12.

**Parameters:**
- `EXO2Temp`: Temperature (°C)
- `EXO2Salinity`: Salinity (psu)
- `EXO2pH`: pH (units)
- `EXO2DO`: Dissolved oxygen (% saturation)
- `EXO2Chlor`: Chlorophyll fluorescence (RFU)
- `EXO2Turb`: Turbidity (FNU)
- `EXO2Depth`: Depth/pressure (m)
- `EXO2spCond`: Specific conductivity (mS/cm)
- `EXO2DomgpL`: Dissolved oxygen (mg/L)

### ZCell ADCP Current Profiler

Acoustic Doppler Current Profiler for water current measurements.

**Parameters:**
- `ZCel_Hdng`: Heading (degrees)
- `ZCel_Pitch`: Pitch (degrees)
- `ZCel_Roll`: Roll (degrees)
- `ZCel_Press`: Pressure (dBar)
- `ZCel_WTmp`: Water temperature (°C)
- `ZCelDpth_*`: Depth bins (m)
- `CurrSpd_*`: Current speed at depth (m/s)
- `CurrDir_*`: Current direction at depth (degrees)

## Data Quality Considerations

### Two-Stage Quality Control

1. **Sentinel Value Conversion** (automatic in `load_toa5_file()`):
   - Converts -7999, -2147483648, ±6999, ±7999 to NaN
   - Happens at data loading stage
   - Ensures statistical calculations are valid

2. **Physical Bounds Filtering** (optional via `apply_marine_quality_filters()`):
   - Removes physically impossible values
   - Marine/estuarine parameter specific
   - Catches sensor drift and calibration issues

### Recommended Workflow

```python
# 1. Load with automatic sentinel conversion
df, metadata, units = load_toa5_file('data/station.dat')

# 2. Check for NaN from sentinels
print(f"Sentinel NaN: {df.isna().sum()}")

# 3. Apply physical bounds (optional)
df_clean = apply_marine_quality_filters(df)

# 4. Apply domain-specific QC (your analysis)
# - Diurnal pattern validation
# - Cross-parameter consistency checks
# - Rate of change limits
# - etc.
```

## References

- **Campbell Scientific CR1000X Product Manual**, Section 14.2 "Understanding NAN"
  - Explains NaN representation in different data types
  - Documents when sentinel values occur
  - Located in: `refs/technical/CR1000X-Product-Manual.md`

- **YSI EXO2 User Manual**
  - Sensor specifications and calibration procedures
  - Located in: `refs/technical/EXO-User-Manual.md`

## Troubleshooting

### Issue: Strange spikes in plots at -7999

**Cause:** Campbell Scientific NaN sentinels not converted to NaN.

**Solution:** Ensure you're using `load_toa5_file()` which automatically converts sentinels.

### Issue: Type inference errors when loading TOA5

**Cause:** Line 4 contains "Smp" strings that confuse pandas.

**Solution:** `load_toa5_file()` skips all 4 header lines and explicitly converts types.

### Issue: Statistics include impossible values

**Cause:** Sentinel values (-7999) included in calculations.

**Solution:** Use `load_toa5_file()` for automatic conversion, then check with `df.isna().sum()`.

### Issue: Physical bounds not catching errors

**Cause:** May need tighter bounds for specific deployment.

**Solution:** Customize bounds in `apply_marine_quality_filters()` or create custom filter function.

## Contributing

When adding new loader functions:

1. Document data format structure in docstring
2. Explain any format-specific quirks (like TOA5 line 4 issue)
3. Handle error/sentinel values explicitly
4. Return metadata along with data
5. Add usage examples to this README

## See Also

- **Notebooks:** See `notebooks/01_initial_data_exploration.ipynb` for usage examples
- **Package Documentation:** `PACKAGE.md` in repository root
- **Technical References:** `refs/technical/` directory for sensor manuals
