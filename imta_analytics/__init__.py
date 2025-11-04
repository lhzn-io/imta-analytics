"""
IMTA Analytics - Integrated Multi-Trophic Aquaculture Data Analytics

A Python package for loading, analyzing, and visualizing data from the
UNH Aquafort buoy station and other IMTA monitoring systems.

Modules:
    data: Data loading and parsing utilities (TOA5, etc.)
    quality: Data quality checks and validation
    analysis: Time series analysis and modeling
    web: Web application and API components
"""

__version__ = "0.1.0"
__author__ = "UNH CSSS"

# Import main data loading functions for convenience
from .data import load_toa5_file

# Notebook utilities (optional - only works in Jupyter)
try:
    from .notebook_utils import (
        display_result,
        display_info,
        display_success,
        display_warning,
        display_error,
        format_dict_as_list,
        format_stats_table
    )
    _notebook_utils_available = True
except ImportError:
    _notebook_utils_available = False

__all__ = ["load_toa5_file"]
