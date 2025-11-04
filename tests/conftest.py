"""Pytest configuration and shared fixtures for imta_analytics tests."""

import pytest
import pandas as pd
from pathlib import Path


@pytest.fixture
def sample_toa5_file(tmp_path):
    """Create a minimal valid TOA5 file for testing.
    
    Returns:
        Path: Path to the temporary TOA5 file
    """
    content = '''"TOA5","TestStation","CR1000X","12345","CR1000X.Std.03.02","CPU:Test.CR1X","1234","EXO2SumData"
"TIMESTAMP","RECORD","Temp","DO","pH"
"TS","RN","°C","mg/L",""
"","","Smp","Smp","Smp"
"2024-01-01 00:00:00",0,15.5,8.2,7.8
"2024-01-01 00:15:00",1,15.6,8.1,7.9
"2024-01-01 00:30:00",2,15.7,8.0,8.0
'''
    file_path = tmp_path / "test.dat"
    file_path.write_text(content)
    return file_path


@pytest.fixture
def sample_toa5_with_errors(tmp_path):
    """Create a TOA5 file with known sensor error codes.
    
    Returns:
        Path: Path to the temporary TOA5 file with errors
    """
    content = '''"TOA5","TestStation","CR1000X","12345","CR1000X.Std.03.02","CPU:Test.CR1X","1234","EXO2SumData"
"TIMESTAMP","RECORD","Temp","DO","pH","Salinity"
"TS","RN","°C","mg/L","","psu"
"","","Smp","Smp","Smp","Smp"
"2024-01-01 00:00:00",0,15.5,8.2,7.8,28.5
"2024-01-01 00:15:00",1,143052,8.1,7.9,29.0
"2024-01-01 00:30:00",2,15.7,193039,8.0,28.8
"2024-01-01 00:45:00",3,15.6,8.0,91625,29.1
"2024-01-01 01:00:00",4,-86.48,8.1,7.8,28.9
"2024-01-01 01:15:00",5,15.8,8.2,7.9,29.2
'''
    file_path = tmp_path / "test_errors.dat"
    file_path.write_text(content)
    return file_path


@pytest.fixture
def sample_clean_dataframe():
    """Create a sample dataframe with valid marine data.
    
    Returns:
        pd.DataFrame: Clean dataframe for testing
    """
    return pd.DataFrame({
        'TIMESTAMP': pd.date_range('2024-01-01', periods=5, freq='15min'),
        'RECORD': range(5),
        'Temp': [15.5, 15.6, 15.7, 15.8, 15.9],
        'DO': [8.2, 8.1, 8.0, 8.1, 8.2],
        'pH': [7.8, 7.9, 8.0, 7.9, 7.8],
        'Salinity': [28.5, 29.0, 28.8, 29.1, 28.9]
    })


@pytest.fixture
def sample_dataframe_with_outliers():
    """Create a sample dataframe with physical outliers.
    
    Returns:
        pd.DataFrame: Dataframe with outliers for testing filters
    """
    return pd.DataFrame({
        'TIMESTAMP': pd.date_range('2024-01-01', periods=8, freq='15min'),
        'RECORD': range(8),
        'Temp': [15.5, -5.0, 40.0, 15.7, 15.8, 15.9, 16.0, 16.1],  # -5 and 40 are outliers
        'DO': [8.2, 8.1, 200.0, -1.0, 8.1, 8.2, 8.3, 8.0],  # 200 and -1 are outliers
        'pH': [7.8, 5.0, 11.0, 7.9, 8.0, 7.8, 7.9, 8.1],  # 5 and 11 are outliers
        'Salinity': [28.5, 29.0, 50.0, -5.0, 28.9, 29.1, 28.8, 29.2]  # 50 and -5 are outliers
    })
