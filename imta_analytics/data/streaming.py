# Copyright (c) 2025 Daniel Fry
# MIT License. See LICENSE file in the project root for full license text.
#
"""
Streaming utilities for efficient processing of large timeseries datasets.

This module provides utilities for:
- Converting TOA5 files to Feather format (blazing fast reads)
- Streaming record batches for iterative algorithms
- Memory-efficient data processing pipelines
"""

from pathlib import Path
from typing import Union, Optional, Iterator, Tuple, Dict, List
import pandas as pd
import pyarrow as pa
import pyarrow.feather as feather
import pyarrow.ipc as ipc


def stream_feather_batches(
    filepath: Union[str, Path],
    batch_size: int = 10000,
    columns: Optional[List[str]] = None
) -> Iterator[pd.DataFrame]:
    """
    Stream records from a Feather file in batches.
    
    This is the fastest way to process large timeseries files iteratively.
    Uses Arrow's zero-copy reads for maximum performance.
    
    Parameters
    ----------
    filepath : str or Path
        Path to the Feather file
    batch_size : int, default 10000
        Number of records per batch
    columns : list of str, optional
        Subset of columns to read (reads all if None)
        
    Yields
    ------
    pd.DataFrame
        Batch of records as a DataFrame
        
    Examples
    --------
    >>> for batch in stream_feather_batches('data.feather', batch_size=5000):
    ...     mean_temp = batch['temperature'].mean()
    ...     print(f"Batch mean: {mean_temp:.2f}")
    """
    filepath = Path(filepath)
    
    # Open the IPC file for streaming
    with ipc.open_file(filepath) as reader:
        # Get total record batches
        num_batches = reader.num_record_batches
        
        for i in range(num_batches):
            batch = reader.get_batch(i)
            
            # Convert to pandas, selecting columns if specified
            if columns:
                df = batch.select(columns).to_pandas()
            else:
                df = batch.to_pandas()
            
            # Yield in smaller chunks if batch is larger than batch_size
            if len(df) > batch_size:
                for start in range(0, len(df), batch_size):
                    yield df.iloc[start:start + batch_size]
            else:
                yield df


def stream_parquet_batches(
    filepath: Union[str, Path],
    batch_size: int = 10000,
    columns: Optional[List[str]] = None
) -> Iterator[pd.DataFrame]:
    """
    Stream records from a Parquet file in batches.
    
    Good for reading compressed archived data. Slower than Feather
    but better compression ratio.
    
    Parameters
    ----------
    filepath : str or Path
        Path to the Parquet file
    batch_size : int, default 10000
        Number of records per batch
    columns : list of str, optional
        Subset of columns to read (reads all if None)
        
    Yields
    ------
    pd.DataFrame
        Batch of records as a DataFrame
        
    Examples
    --------
    >>> for batch in stream_parquet_batches('data.parquet', batch_size=5000):
    ...     process_sensor_data(batch)
    """
    import pyarrow.parquet as pq
    
    filepath = Path(filepath)
    parquet_file = pq.ParquetFile(filepath)
    
    for batch in parquet_file.iter_batches(batch_size=batch_size, columns=columns):
        yield batch.to_pandas()


def convert_to_feather(
    df: pd.DataFrame,
    output_path: Union[str, Path],
    compression: str = 'lz4',
    chunksize: Optional[int] = None
) -> None:
    """
    Convert DataFrame to Feather format for blazing fast reads.
    
    Feather (Arrow IPC) format provides:
    - 5-50x faster reads than CSV
    - 2-5x faster reads than Parquet
    - Zero-copy memory mapping
    - Perfect for intermediate data and streaming algorithms
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to write
    output_path : str or Path
        Output file path (.feather extension recommended)
    compression : str, default 'lz4'
        Compression algorithm: 'lz4' (fast), 'zstd' (smaller), or 'uncompressed'
    chunksize : int, optional
        Write in chunks for very large DataFrames (reduces memory usage)
        
    Examples
    --------
    >>> df = pd.read_csv('large_data.csv')
    >>> convert_to_feather(df, 'large_data.feather')
    >>> # Now reads are 10-50x faster
    >>> df_fast = pd.read_feather('large_data.feather')
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    if chunksize is None:
        # Write entire DataFrame at once
        df.to_feather(output_path, compression=compression)
    else:
        # Write in chunks for very large files
        table = pa.Table.from_pandas(df)
        with ipc.new_file(output_path, table.schema) as writer:
            for i in range(0, len(table), chunksize):
                batch = table.slice(i, min(chunksize, len(table) - i))
                writer.write_batch(batch)


def get_file_info(filepath: Union[str, Path]) -> Dict[str, any]:
    """
    Get metadata about a Feather or Parquet file.
    
    Parameters
    ----------
    filepath : str or Path
        Path to Feather or Parquet file
        
    Returns
    -------
    dict
        File metadata including:
        - format: 'feather' or 'parquet'
        - num_rows: Total number of rows
        - num_columns: Total number of columns
        - columns: List of column names
        - size_mb: File size in megabytes
        - compression: Compression algorithm used
        
    Examples
    --------
    >>> info = get_file_info('data.feather')
    >>> print(f"Rows: {info['num_rows']:,}, Size: {info['size_mb']:.1f} MB")
    """
    filepath = Path(filepath)
    
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    size_mb = filepath.stat().st_size / (1024 * 1024)
    
    # Try to detect format from extension or content
    if filepath.suffix.lower() in ['.feather', '.arrow', '.ipc']:
        with ipc.open_file(filepath) as reader:
            schema = reader.schema
            num_rows = sum(reader.get_batch(i).num_rows 
                          for i in range(reader.num_record_batches))
            return {
                'format': 'feather',
                'num_rows': num_rows,
                'num_columns': len(schema),
                'columns': schema.names,
                'size_mb': size_mb,
                'compression': 'unknown'  # Arrow IPC doesn't expose this easily
            }
    elif filepath.suffix.lower() == '.parquet':
        import pyarrow.parquet as pq
        parquet_file = pq.ParquetFile(filepath)
        metadata = parquet_file.metadata
        return {
            'format': 'parquet',
            'num_rows': metadata.num_rows,
            'num_columns': metadata.num_columns,
            'columns': parquet_file.schema.names,
            'size_mb': size_mb,
            'compression': metadata.row_group(0).column(0).compression
        }
    else:
        raise ValueError(f"Unknown format for file: {filepath}")
