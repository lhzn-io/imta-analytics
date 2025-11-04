"""
Data format loaders for various aquaculture monitoring systems.

This module provides functions for loading and parsing data files from
environmental monitoring systems, particularly Campbell Scientific dataloggers.
"""

import csv
from pathlib import Path
from typing import Union, Tuple, Dict, List

import pandas as pd


def load_toa5_file(filepath: Union[str, Path]) -> Tuple[pd.DataFrame, Dict[str, str], List[str]]:
    """
    Load a Campbell Scientific TOA5 format file with proper NaN handling.
    
    TOA5 files have a specific 4-line header structure:
    - Line 1: File metadata (station, logger model, OS version, etc.)
    - Line 2: Column headers
    - Line 3: Units for each column
    - Line 4: Sampling/processing info (typically "Smp", "Avg", etc.)
    - Line 5+: Actual data in CSV format
    
    CRITICAL: Line 4 contains strings like "Smp" which confuse pandas type
    inference. We skip all 4 header lines and explicitly convert types.
    
    Campbell Scientific NaN Sentinel Values
    ----------------------------------------
    Campbell Scientific dataloggers represent NaN (invalid measurements) using 
    data-type-specific sentinel values:
    
    - **FP2 (Float Point 2)**: NaN appears as **-7999**
      - Range: -7999 to +7999
      - Common for most sensor measurements
      
    - **Long Integer**: NaN appears as **-2147483648** (most negative 32-bit int)
      - Used for integer-only data types
      
    - **Overrange values**: ±6999, ±7999 may indicate measurement overrange
    
    These sentinel values occur when:
    1. Input signals exceed the voltage range chosen for the measurement
    2. An invalid SDI-12 command is sent
    3. An SDI-12 sensor does not respond or aborts without sending data
    4. Measurement overrange (values exceed sensor specifications)
    
    This function automatically converts these sentinel values to proper NaN.
    
    Parameters
    ----------
    filepath : str or Path
        Path to the TOA5 .dat file
        
    Returns
    -------
    df : pandas.DataFrame
        Loaded data with proper column names and types. Campbell Scientific
        sentinel values (-7999, -2147483648, etc.) are converted to NaN.
        Numeric columns are float64/int64, TIMESTAMP is datetime64.
    metadata : dict
        File metadata from header line containing:
        - format: File format identifier (e.g., "TOA5")
        - station: Station name
        - logger_model: Datalogger model
        - serial_number: Logger serial number
        - os_version: Logger OS version
        - program: Program name
        - signature: Program signature
        - table_name: Data table name
    units : list of str
        Units for each column (e.g., "°C", "mV", "psu")
        
    Examples
    --------
    >>> df, metadata, units = load_toa5_file('data/UNH-G2000B_EXO2SumData.dat')
    >>> print(f"Station: {metadata['station']}")
    Station: UNH-G2000B
    >>> print(f"Shape: {df.shape}")
    Shape: (8640, 21)
    >>> print(df['TIMESTAMP'].dtype)
    datetime64[ns]
    >>> # Campbell Scientific sentinel values are now NaN
    >>> print(df['EXO2Temp'].isna().sum())
    142  # -7999 values converted to NaN
    
    Notes
    -----
    - Campbell Scientific NaN sentinels (-7999, -2147483648, ±6999, ±7999) are
      automatically converted to proper NaN values during loading
    - Missing or invalid values are also converted to NaN via pd.to_numeric()
    - All columns except TIMESTAMP are explicitly converted to numeric types
    - TIMESTAMP column is parsed to pandas datetime objects
    - Additional quality filtering may be needed using physical bounds for
      marine parameters (see apply_marine_quality_filters)
    
    References
    ----------
    Campbell Scientific CR1000X Product Manual, Section 14.2 "Understanding NAN"
    
    See Also
    --------
    apply_marine_quality_filters : Apply physical bounds for marine data
    pandas.read_csv : Underlying CSV parser
    pandas.to_numeric : Type conversion with error handling
    """
    filepath = Path(filepath)
    
    # Read the first line to get metadata
    with open(filepath, 'r', encoding='utf-8') as f:
        metadata_line = f.readline().strip().strip('"').split('","')
        
    metadata = {
        'format': metadata_line[0],
        'station': metadata_line[1],
        'logger_model': metadata_line[2],
        'serial_number': metadata_line[3],
        'os_version': metadata_line[4],
        'program': metadata_line[5],
        'signature': metadata_line[6],
        'table_name': metadata_line[7]
    }
    
    # Read header (line 2) with proper quoting handling
    header_df = pd.read_csv(
        filepath, 
        skiprows=1, 
        nrows=1, 
        header=None, 
        quoting=csv.QUOTE_ALL,
        encoding='utf-8'
    )
    headers = [str(col) for col in header_df.iloc[0].values]
    
    # Read units (line 3) with proper quoting handling
    units_df = pd.read_csv(
        filepath, 
        skiprows=2, 
        nrows=1, 
        header=None, 
        quoting=csv.QUOTE_ALL,
        encoding='utf-8'
    )
    units = [str(u) for u in units_df.iloc[0].values]
    
    # Read the actual data - skip first 4 header lines completely
    # Use header=None and names=headers to explicitly set column names
    # DON'T let pandas see line 4 (all "Smp" strings) as it confuses type inference
    df = pd.read_csv(
        filepath, 
        skiprows=4, 
        header=None, 
        names=headers, 
        low_memory=False,
        encoding='utf-8'
    )
    
    # Now explicitly convert columns to appropriate types
    # All columns except TIMESTAMP should be numeric
    for col in df.columns:
        if col != 'TIMESTAMP':
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Convert Campbell Scientific NaN sentinel values to proper NaN
    # These are data-type-specific sentinel values used by Campbell dataloggers
    CAMPBELL_NAN_SENTINELS = [
        -7999,          # FP2 (Float Point 2) NaN representation
        7999,           # FP2 positive overrange
        -6999,          # FP2 near-limit value
        6999,           # FP2 near-limit value
        -2147483648,    # Long Integer NaN representation (most negative 32-bit int)
    ]
    
    for col in df.columns:
        if col != 'TIMESTAMP' and pd.api.types.is_numeric_dtype(df[col]):
            # Replace sentinel values with NaN
            df[col] = df[col].replace(CAMPBELL_NAN_SENTINELS, pd.NA)
    
    # Parse the TIMESTAMP column
    df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'], errors='coerce')
    
    return df, metadata, units


def apply_marine_data_quality_filters(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply data quality filtering for marine sensor data.
    
    This function performs post-load data quality control to remove:
    1. YSI EXO2 sensor malfunction artifacts (cascading identical values)
    2. YSI-specific error codes in date/time/voltage fields
    3. Physically impossible values based on marine/estuarine bounds
    
    NOTE: This operates AFTER load_toa5_file() has already converted Campbell
    Scientific NaN sentinels (-7999, -2147483648, etc.) to proper NaN values.
    
    YSI EXO2 Sensor Malfunctions
    -----------------------------
    When the YSI EXO2 water quality sonde experiences a malfunction, it outputs
    the same garbage value across multiple measurement fields. For example, a 
    single row might have the value 143052 appearing in EXO2Time, EXO2Temp, 
    EXO2Chlor, EXO2DO, and EXO2ExtPwr simultaneously. This function detects 
    these "cascading errors" by identifying rows where the same numeric value 
    appears in 5 or more columns.
    
    Additionally, specific error codes appear in date/time/voltage fields:
    - 143052, 193039: Appear in EXO2Time, EXO2Temp, and sensor readings
    - 91625: Appears in EXO2Date and EXO2Time (date/time encoding failure)
    - -86.48: Appears in EXO2pHmV and voltage readings (sensor error)
    
    These are NOT Campbell Scientific datalogger error codes - they are
    artifacts from the YSI EXO2 probe itself during sensor malfunctions.
    
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame with water quality columns (must contain TIMESTAMP).
        Expected to have been loaded via load_toa5_file() with Campbell
        Scientific NaN sentinels already converted to NaN.
        
    Returns
    -------
    df_clean : pandas.DataFrame
        Filtered DataFrame with invalid readings removed
        
    Notes
    -----
    Physical bounds used (marine/estuarine):
    - Temperature: -2 to 35°C
    - pH: 6.5 to 9.5
    - Salinity: 0 to 40 psu
    - Dissolved Oxygen: 0 to 150% saturation
    - Conductivity: 0 to 70 mS/cm
    - Turbidity: 0 to 1000 FNU
    - Chlorophyll: 0 to 200 μg/L
    - Depth: 0 to 100 m
    
    Examples
    --------
    >>> from imta_analytics.data import load_toa5_file, apply_marine_data_quality_filters
    >>> df, metadata, units = load_toa5_file('data.dat')
    >>> df_clean = apply_marine_data_quality_filters(df)
    >>> print(f"Removed {len(df) - len(df_clean)} rows with data quality issues")
    
    See Also
    --------
    load_toa5_file : Load TOA5 files with Campbell Scientific NaN sentinel conversion
    """
    df_clean = df.copy()
    
    # Get numeric columns for cascading error detection
    numeric_cols = [col for col in df_clean.columns 
                    if col not in ['TIMESTAMP', 'RECORD'] 
                    and pd.api.types.is_numeric_dtype(df_clean[col])]
    
    # Step 1: Remove rows with cascading sensor failures
    # (same value appears in 5+ columns - indicates sensor malfunction)
    def has_cascading_error(row, threshold=5):
        """Detect if same value appears in multiple columns (sensor malfunction)."""
        row_clean = row.dropna()
        if len(row_clean) == 0:
            return False
        value_counts = row_clean.value_counts()
        return (value_counts >= threshold).any()
    
    cascading_mask = df_clean[numeric_cols].apply(has_cascading_error, axis=1)
    df_clean = df_clean[~cascading_mask]
    
    # Step 2: Remove rows with YSI-specific error codes
    # These appear in date/time/voltage fields during sensor errors
    ysi_error_codes = [143052, 193039, 91625, -86.48]
    
    # Remove rows containing any error codes in numeric columns
    for col in df_clean.columns:
        if col != 'TIMESTAMP' and pd.api.types.is_numeric_dtype(df_clean[col]):
            for error_code in ysi_error_codes:
                df_clean = df_clean[df_clean[col] != error_code]
    
    # Define physical bounds for each parameter (with generic names)
    # Maps both EXO2-specific and generic column names
    bounds = {
        # EXO2-specific names
        'EXO2Temp_C': (-2, 35),
        'EXO2pH': (6.5, 9.5),
        'EXO2Sal_psu': (0, 40),
        'EXO2DO_sat': (0, 150),
        'EXO2SpCond_mScm': (0, 70),
        'EXO2Turb_FNU': (0, 1000),
        'EXO2Chl_ugL': (0, 200),
        'EXO2Depth_m': (0, 100),
        # Generic names (for testing and other sensors)
        'Temp': (-2, 35),
        'pH': (6.5, 9.5),
        'Salinity': (0, 40),
        'DO': (0, 150),
        'Conductivity': (0, 70),
        'Turbidity': (0, 1000),
        'Chlorophyll': (0, 200),
        'Depth': (0, 100),
    }
    
    # Apply bounds filtering
    for col, (min_val, max_val) in bounds.items():
        if col in df_clean.columns:
            df_clean = df_clean[
                (df_clean[col] >= min_val) & (df_clean[col] <= max_val)
            ]
    
    return df_clean
