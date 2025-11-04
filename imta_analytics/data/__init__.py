"""
Data loading and parsing module for IMTA Analytics.

This module provides functions for loading various data formats used in
aquaculture monitoring systems, with a focus on Campbell Scientific
TOA5 format files.
"""

from .loaders import load_toa5_file

__all__ = ["load_toa5_file"]
