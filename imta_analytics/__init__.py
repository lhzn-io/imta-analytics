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

__all__ = ["load_toa5_file"]
