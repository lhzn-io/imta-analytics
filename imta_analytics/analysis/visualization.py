# Copyright (c) 2025 Daniel Fry
# MIT License. See LICENSE file in the project root for full license text.
#
"""Visualization utilities for IMTA data analysis.

This module provides reusable plotting functions for marine sensor data,
reducing code duplication across notebooks and analysis scripts.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from typing import List, Tuple, Optional


def plot_timeseries_grid(
    df: pd.DataFrame,
    params: List[Tuple[str, str]],
    timestamp_col: str = 'TIMESTAMP',
    title: str = 'Time Series Data',
    figsize: Tuple[int, int] = (14, 16),
    layout: Tuple[int, int] = (4, 2),
) -> Tuple[plt.Figure, np.ndarray]:
    """Plot multiple timeseries in a grid layout with shared x-axis.
    
    Args:
        df: DataFrame containing timeseries data
        params: List of (column_name, unit) tuples to plot
        timestamp_col: Name of timestamp column
        title: Overall figure title
        figsize: Figure size (width, height)
        layout: Grid layout as (rows, cols)
        
    Returns:
        Tuple of (figure, axes array)
    """
    rows, cols = layout
    fig, axes = plt.subplots(rows, cols, figsize=figsize, sharex=True)
    fig.suptitle(title, fontsize=14, y=0.995)
    
    # Flatten axes for easier iteration
    axes_flat = axes.flatten() if isinstance(axes, np.ndarray) else [axes]
    
    for idx, (param, unit) in enumerate(params):
        if idx >= len(axes_flat):
            break
            
        ax = axes_flat[idx]
        ax.plot(df[timestamp_col], df[param], linewidth=0.8, alpha=0.8)
        ax.set_ylabel(unit, fontsize=10)
        ax.set_title(param, fontsize=10, pad=8)
        ax.grid(True, alpha=0.3)
        ax.margins(x=0)
        
        # Format y-axis to avoid scientific notation for small ranges
        ax.ticklabel_format(style='plain', axis='y')
    
    # Set x-label only on bottom row
    for ax in axes_flat[-(cols):]:
        ax.set_xlabel('Date', fontsize=10)
    
    # Hide unused subplots
    for idx in range(len(params), len(axes_flat)):
        axes_flat[idx].set_visible(False)
    
    plt.tight_layout()
    return fig, axes


def plot_availability_timeline(
    dfs: List[pd.DataFrame],
    labels: List[str],
    timestamp_col: str = 'TIMESTAMP',
    record_col: str = 'RECORD',
    resample_freq: str = 'H',
    title: str = 'Data Availability Timeline',
    figsize: Tuple[int, int] = (14, 8),
    logy: Optional[bool] = None,
) -> Tuple[plt.Figure, np.ndarray]:
    """Plot data availability over time for multiple datasets.
    
    Args:
        dfs: List of DataFrames to plot
        labels: Labels for each dataset
        timestamp_col: Name of timestamp column
        record_col: Name of record count column
        resample_freq: Resampling frequency ('H' for hourly, 'D' for daily)
        title: Figure title
        figsize: Figure size (width, height)
        logy: Use log scale for y-axis. If None (default), automatically enables
              when max/median ratio > 10 for any dataset (indicating outliers)
        
    Returns:
        Tuple of (figure, axes array)
    """
    n_datasets = len(dfs)
    fig, axes = plt.subplots(n_datasets, 1, figsize=figsize, sharex=True)
    
    # Handle single subplot case
    if n_datasets == 1:
        axes = [axes]
    
    # Adaptive log scaling: check if any dataset has extreme outliers
    if logy is None:
        logy = False
        for df in dfs:
            resampled = df.set_index(timestamp_col).resample(resample_freq).count()[record_col]
            nonzero = resampled[resampled > 0]
            if len(nonzero) > 0:
                ratio = nonzero.max() / nonzero.median()
                if ratio > 10:  # More than 10x difference indicates outliers
                    logy = True
                    break
    
    for idx, (df, label) in enumerate(zip(dfs, labels)):
        ax = axes[idx]
        
        # Resample to get record counts
        resampled = df.set_index(timestamp_col).resample(resample_freq).count()[record_col]
        
        ax.plot(resampled.index, resampled.values, linewidth=1.2, alpha=0.8)
        ax.set_ylabel(f'Records/{resample_freq}{"(log)" if logy else ""}', fontsize=10)
        ax.set_title(label, fontsize=11, pad=8)
        ax.grid(True, alpha=0.3, which='both' if logy else 'major')
        ax.margins(x=0)
        
        if logy:
            ax.set_yscale('log')
            # Add minor grid lines for log scale
            ax.grid(True, alpha=0.15, which='minor')
    
    axes[-1].set_xlabel('Date', fontsize=10)
    fig.suptitle(title, fontsize=14, y=0.995)
    
    plt.tight_layout()
    return fig, axes


def plot_correlation_heatmap(
    df: pd.DataFrame,
    columns: Optional[List[str]] = None,
    title: str = 'Correlation Matrix',
    figsize: Tuple[int, int] = (10, 8),
    cmap: str = 'RdBu_r',
    vmin: float = -1.0,
    vmax: float = 1.0,
    annot: bool = True,
) -> Tuple[plt.Figure, plt.Axes, pd.DataFrame]:
    """Plot correlation heatmap for specified columns.
    
    Args:
        df: DataFrame containing data
        columns: List of column names to include (None = all numeric columns)
        title: Plot title
        figsize: Figure size (width, height)
        cmap: Colormap name
        vmin: Minimum value for color scale
        vmax: Maximum value for color scale
        annot: Whether to annotate cells with correlation values
        
    Returns:
        Tuple of (figure, axes, correlation_matrix)
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Calculate correlation matrix
    if columns is None:
        corr_data = df.select_dtypes(include=[np.number]).corr()
    else:
        corr_data = df[columns].corr()
    
    # Create heatmap
    sns.heatmap(
        corr_data,
        annot=annot,
        fmt='.2f',
        cmap=cmap,
        vmin=vmin,
        vmax=vmax,
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={'label': 'Correlation'},
        ax=ax
    )
    
    ax.set_title(title, fontsize=14, pad=12)
    plt.tight_layout()
    
    return fig, ax, corr_data


def plot_current_profile(
    depths: List[float],
    speeds: List[float],
    directions: List[float],
    timestamp: str,
    title: str = 'Current Profile',
    figsize: Tuple[int, int] = (12, 6),
) -> Tuple[plt.Figure, np.ndarray]:
    """Plot current speed and direction profiles vs depth.
    
    Args:
        depths: List of depth values (meters)
        speeds: List of current speed values (m/s)
        directions: List of current direction values (degrees)
        timestamp: Timestamp string for the profile
        title: Overall plot title
        figsize: Figure size (width, height)
        
    Returns:
        Tuple of (figure, axes array)
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize, sharey=True)
    
    # Speed profile
    ax1.plot(speeds, depths, 'o-', linewidth=2, markersize=6, color='blue', alpha=0.7)
    ax1.set_xlabel('Current Speed (m/s)', fontsize=11)
    ax1.set_ylabel('Depth (m)', fontsize=11)
    ax1.set_title('Current Speed Profile', fontsize=11, pad=8)
    ax1.invert_yaxis()
    ax1.grid(True, alpha=0.3)
    
    # Direction profile
    ax2.plot(directions, depths, 'o-', linewidth=2, markersize=6, color='red', alpha=0.7)
    ax2.set_xlabel('Current Direction (°)', fontsize=11)
    ax2.set_title('Current Direction Profile', fontsize=11, pad=8)
    ax2.invert_yaxis()
    ax2.grid(True, alpha=0.3)
    
    fig.suptitle(f'{title} - {timestamp}', fontsize=13, y=0.98)
    plt.tight_layout()
    
    return fig, (ax1, ax2)
