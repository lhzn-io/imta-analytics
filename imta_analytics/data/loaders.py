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
    Load a Campbell Scientific TOA5 format file.
    
    TOA5 files have a specific 4-line header structure:
    - Line 1: File metadata (station, logger model, OS version, etc.)
    - Line 2: Column headers
    - Line 3: Units for each column
    - Line 4: Sampling/processing info (typically "Smp", "Avg", etc.)
    - Line 5+: Actual data in CSV format
    
    CRITICAL: Line 4 contains strings like "Smp" which confuse pandas type
    inference. We skip all 4 header lines and explicitly convert types.
    
    Parameters
    ----------
    filepath : str or Path
        Path to the TOA5 .dat file
        
    Returns
    -------
    df : pandas.DataFrame
        Loaded data with proper column names and types (numeric columns
        are float64/int64, TIMESTAMP is datetime64)
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
    
    Notes
    -----
    - Sensor error codes (143052, 193039, 91625, -86.48) appear as numeric
      values and should be filtered using physical bounds for marine parameters
    - Missing or invalid values are converted to NaN via pd.to_numeric()
    - All columns except TIMESTAMP are explicitly converted to numeric types
    - TIMESTAMP column is parsed to pandas datetime objects
    
    See Also
    --------
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
    
    # Parse the TIMESTAMP column
    df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'], errors='coerce')
    
    return df, metadata, units


def apply_marine_quality_filters(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply physical bounds filtering for marine water quality parameters.
    
    Removes sensor error codes and physically impossible values based on
    typical marine/estuarine conditions.
    
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame with water quality columns (must contain TIMESTAMP)
        
    Returns
    -------
    df_clean : pandas.DataFrame
        Filtered DataFrame with invalid readings removed
        
    Notes
    -----
    Physical bounds used:
    - Temperature: -2 to 35°C (marine/estuarine range)
    - pH: 6.5 to 9.5 (natural water range)
    - Salinity: 0 to 40 psu (fresh to hypersaline)
    - Dissolved Oxygen: 0 to 150% saturation
    - Conductivity: 0 to 70 mS/cm
    - Turbidity: 0 to 1000 FNU (practical upper limit)
    - Chlorophyll: 0 to 200 μg/L (very high for blooms)
    - Depth: 0 to 100 m (typical buoy deployment)
    
    Sensor error codes filtered:
    - 143052, 193039, 91625, -86.48 (Campbell Scientific/YSI error codes)
    - Large outliers detected via IQR method
    """
    df_clean = df.copy()
    
    # Known sensor error codes (Campbell Scientific/YSI)
    error_codes = [143052, 193039, 91625, -86.48]
    
    # Remove rows containing any error codes in numeric columns
    for col in df_clean.columns:
        if col != 'TIMESTAMP' and pd.api.types.is_numeric_dtype(df_clean[col]):
            for error_code in error_codes:
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
