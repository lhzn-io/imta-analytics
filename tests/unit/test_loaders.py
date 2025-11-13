# Copyright (c) 2025 Daniel Fry
# MIT License. See LICENSE file in the project root for full license text.
#
"""Unit tests for TOA5 data loaders."""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
from imta_analytics.data import load_toa5_file
from imta_analytics.data.loaders import apply_marine_data_quality_filters


class TestLoadTOA5File:
    """Tests for load_toa5_file() function."""
    
    def test_basic_loading(self, sample_toa5_file):
        """Test that basic TOA5 file loads correctly."""
        df, metadata, units = load_toa5_file(sample_toa5_file)
        
        # Check dataframe shape
        assert len(df) == 3
        assert 'TIMESTAMP' in df.columns
        assert 'Temp' in df.columns
        assert 'DO' in df.columns
        assert 'pH' in df.columns
        
        # Check data types
        assert pd.api.types.is_datetime64_any_dtype(df['TIMESTAMP'])
        assert pd.api.types.is_numeric_dtype(df['Temp'])
        assert pd.api.types.is_numeric_dtype(df['DO'])
        assert pd.api.types.is_numeric_dtype(df['pH'])
    
    def test_metadata_extraction(self, sample_toa5_file):
        """Test that metadata is extracted correctly."""
        df, metadata, units = load_toa5_file(sample_toa5_file)
        
        assert metadata['station'] == 'TestStation'
        assert metadata['logger_model'] == 'CR1000X'
        assert metadata['table_name'] == 'EXO2SumData'
    
    def test_units_extraction(self, sample_toa5_file):
        """Test that units are extracted correctly."""
        df, metadata, units = load_toa5_file(sample_toa5_file)
        
        assert len(units) == len(df.columns)
        temp_idx = df.columns.get_loc('Temp')
        do_idx = df.columns.get_loc('DO')
        assert isinstance(temp_idx, int) and units[temp_idx] == '°C'
        assert isinstance(do_idx, int) and units[do_idx] == 'mg/L'
    
    def test_sensor_errors_become_nan(self, sample_toa5_with_errors):
        """Test that sensor error codes are loaded as numeric values."""
        df, metadata, units = load_toa5_file(sample_toa5_with_errors)
        
        # Error codes should be loaded as numeric values (not NaN yet)
        # They get filtered by apply_marine_data_quality_filters()
        assert pd.api.types.is_numeric_dtype(df['Temp'])
        assert pd.api.types.is_numeric_dtype(df['DO'])
        assert pd.api.types.is_numeric_dtype(df['pH'])
        
        # Check that the filter function removes them
        df_filtered = apply_marine_data_quality_filters(df)
        assert len(df_filtered) < len(df)  # Should have removed error rows
    
    def test_timestamp_parsing(self, sample_toa5_file):
        """Test that timestamps are parsed correctly."""
        df, metadata, units = load_toa5_file(sample_toa5_file)
        
        expected_timestamps = pd.to_datetime([
            '2024-01-01 00:00:00',
            '2024-01-01 00:15:00',
            '2024-01-01 00:30:00'
        ])
        # Compare the series values, not as an index
        pd.testing.assert_series_equal(
            df['TIMESTAMP'].reset_index(drop=True), 
            pd.Series(expected_timestamps).reset_index(drop=True),
            check_names=False
        )


class TestMarineQualityFilters:
    """Tests for apply_marine_data_quality_filters() function."""
    
    def test_clean_data_unchanged(self, sample_clean_dataframe):
        """Test that clean data passes through filters unchanged."""
        df_filtered = apply_marine_data_quality_filters(sample_clean_dataframe.copy())
        
        assert len(df_filtered) == len(sample_clean_dataframe)
        pd.testing.assert_frame_equal(df_filtered, sample_clean_dataframe)
    
    def test_outliers_removed(self, sample_dataframe_with_outliers):
        """Test that physical outliers are removed."""
        df_filtered = apply_marine_data_quality_filters(sample_dataframe_with_outliers.copy())
        
        # Should have fewer rows after filtering
        assert len(df_filtered) < len(sample_dataframe_with_outliers)
        
        # Check that all remaining values are within bounds
        if 'Temp' in df_filtered.columns:
            assert df_filtered['Temp'].min() >= -2
            assert df_filtered['Temp'].max() <= 35
        
        if 'DO' in df_filtered.columns:
            assert df_filtered['DO'].min() >= 0
            assert df_filtered['DO'].max() <= 150
        
        if 'pH' in df_filtered.columns:
            assert df_filtered['pH'].min() >= 6.5
            assert df_filtered['pH'].max() <= 9.5
        
        if 'Salinity' in df_filtered.columns:
            assert df_filtered['Salinity'].min() >= 0
            assert df_filtered['Salinity'].max() <= 40
    
    @pytest.mark.parametrize("error_code", [143052, 193039, 91625, -86.48])
    def test_specific_error_codes_removed(self, error_code):
        """Test that specific known error codes are filtered out."""
        df = pd.DataFrame({
            'TIMESTAMP': pd.date_range('2024-01-01', periods=3, freq='15min'),
            'RECORD': range(3),
            'Temp': [15.5, error_code, 15.7]
        })
        
        df_filtered = apply_marine_data_quality_filters(df)
        
        # The row with error code should be removed
        assert len(df_filtered) < len(df)
        assert error_code not in df_filtered['Temp'].values
    
    def test_timestamp_preserved(self, sample_dataframe_with_outliers):
        """Test that TIMESTAMP column is preserved after filtering."""
        df_filtered = apply_marine_data_quality_filters(sample_dataframe_with_outliers.copy())
        
        assert 'TIMESTAMP' in df_filtered.columns
        assert pd.api.types.is_datetime64_any_dtype(df_filtered['TIMESTAMP'])
    
    def test_empty_dataframe(self):
        """Test handling of empty dataframe."""
        df = pd.DataFrame()
        df_filtered = apply_marine_data_quality_filters(df)
        
        assert len(df_filtered) == 0
