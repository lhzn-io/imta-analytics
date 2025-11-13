#!/usr/bin/env python
# Copyright (c) 2025 Daniel Fry
# MIT License. See LICENSE file in the project root for full license text.
#
"""
Command-line tool for converting TOA5 files to Feather format.

This tool provides fast conversion of Campbell Scientific TOA5 files
to Arrow Feather format for blazing fast loading and streaming.

Usage:
    python -m imta_analytics.data.convert_toa5 input.dat output.feather
    python -m imta_analytics.data.convert_toa5 input.dat output.feather --filter-outliers
    python -m imta_analytics.data.convert_toa5 input.dat output.feather --parquet
"""

import argparse
import sys
from pathlib import Path
from typing import Optional

import pandas as pd

from .loaders import load_toa5_file, apply_marine_data_quality_filters
from .streaming import convert_to_feather


def convert_toa5(
    input_path: Path,
    output_path: Path,
    filter_outliers: bool = False,
    to_parquet: bool = False,
    compression: str = 'lz4',
    verbose: bool = True
) -> None:
    """
    Convert TOA5 file to Feather or Parquet format.
    
    Parameters
    ----------
    input_path : Path
        Input TOA5 .dat file
    output_path : Path
        Output file path
    filter_outliers : bool, default False
        Apply marine data quality filtering
    to_parquet : bool, default False
        Output as Parquet instead of Feather
    compression : str, default 'lz4'
        Compression algorithm ('lz4', 'zstd', or 'uncompressed')
    verbose : bool, default True
        Print progress messages
    """
    if verbose:
        print(f"Loading TOA5 file: {input_path}")
    
    # Load TOA5 file
    df, metadata, units = load_toa5_file(input_path)
    
    if verbose:
        print(f"  Station: {metadata['station']}")
        print(f"  Table: {metadata['table_name']}")
        print(f"  Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
        print(f"  Date range: {df['TIMESTAMP'].min()} to {df['TIMESTAMP'].max()}")
    
    # Apply quality filtering if requested
    if filter_outliers:
        if verbose:
            print("Applying data quality filters...")
        
        df_clean = apply_marine_data_quality_filters(df)
        removed = len(df) - len(df_clean)
        
        if verbose:
            print(f"  Removed {removed:,} rows ({removed/len(df)*100:.2f}%)")
        
        df = df_clean
    
    # Create output directory if needed
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Convert to requested format
    if to_parquet:
        if verbose:
            print(f"Writing Parquet file: {output_path}")
        df.to_parquet(output_path, compression=compression, index=False)
    else:
        if verbose:
            print(f"Writing Feather file: {output_path}")
        convert_to_feather(df, output_path, compression=compression)
    
    # Report file size
    if verbose:
        size_mb = output_path.stat().st_size / (1024 * 1024)
        print(f"  Output size: {size_mb:.2f} MB")
        print(f"✓ Conversion complete")


def main():
    """Command-line entry point."""
    parser = argparse.ArgumentParser(
        description='Convert Campbell Scientific TOA5 files to Feather/Parquet format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic conversion to Feather
  %(prog)s input.dat output.feather
  
  # With outlier filtering
  %(prog)s input.dat output.feather --filter-outliers
  
  # Convert to Parquet instead
  %(prog)s input.dat output.parquet --parquet
  
  # Use zstd compression (slower but smaller)
  %(prog)s input.dat output.feather --compression zstd
        """
    )
    
    parser.add_argument(
        'input',
        type=Path,
        help='Input TOA5 .dat file'
    )
    
    parser.add_argument(
        'output',
        type=Path,
        help='Output file path (.feather or .parquet)'
    )
    
    parser.add_argument(
        '--filter-outliers',
        action='store_true',
        help='Apply marine data quality filtering (removes outliers and sensor errors)'
    )
    
    parser.add_argument(
        '--parquet',
        action='store_true',
        help='Output as Parquet instead of Feather (better compression, slower reads)'
    )
    
    parser.add_argument(
        '--compression',
        choices=['lz4', 'zstd', 'uncompressed'],
        default='lz4',
        help='Compression algorithm (default: lz4 - fast)'
    )
    
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Suppress progress messages'
    )
    
    args = parser.parse_args()
    
    # Validate input file exists
    if not args.input.exists():
        print(f"Error: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)
    
    try:
        convert_toa5(
            input_path=args.input,
            output_path=args.output,
            filter_outliers=args.filter_outliers,
            to_parquet=args.parquet,
            compression=args.compression,
            verbose=not args.quiet
        )
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
