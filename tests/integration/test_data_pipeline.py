# Copyright (c) 2025 Daniel Fry
# MIT License. See LICENSE file in the project root for full license text.
#
"""Integration tests for data pipeline."""

import pytest
import pandas as pd
from pathlib import Path
from imta_analytics.data import load_toa5_file
from imta_analytics.data.loaders import apply_marine_quality_filters


class TestDataPipeline:
    """Test complete data loading and cleaning pipeline."""
    
    def test_load_and_filter_pipeline(self, sample_toa5_with_errors):
        """Test loading TOA5 file and applying quality filters."""
        # Load data
        df, metadata, units = load_toa5_file(sample_toa5_with_errors)
        
        # Apply filters
        df_clean = apply_marine_quality_filters(df)
        
        # Verify pipeline results
        assert len(df_clean) > 0
        assert len(df_clean) < len(df)  # Some rows should be filtered
        
        # Check data quality
        if 'Temp' in df_clean.columns and not df_clean['Temp'].isna().all():
            assert df_clean['Temp'].min() >= -2
            assert df_clean['Temp'].max() <= 35
        
        if 'DO' in df_clean.columns and not df_clean['DO'].isna().all():
            assert df_clean['DO'].min() >= 0
            assert df_clean['DO'].max() <= 150
    
    def test_multiple_file_consistency(self, sample_toa5_file, sample_toa5_with_errors):
        """Test that multiple files can be loaded with consistent structure."""
        df1, meta1, units1 = load_toa5_file(sample_toa5_file)
        df2, meta2, units2 = load_toa5_file(sample_toa5_with_errors)
        
        # Both should have TIMESTAMP column
        assert 'TIMESTAMP' in df1.columns
        assert 'TIMESTAMP' in df2.columns
        
        # Both should have numeric types (excluding TIMESTAMP)
        for col in df1.columns:
            if col != 'TIMESTAMP':
                assert pd.api.types.is_numeric_dtype(df1[col])
        
        for col in df2.columns:
            if col != 'TIMESTAMP':
                assert pd.api.types.is_numeric_dtype(df2[col])
