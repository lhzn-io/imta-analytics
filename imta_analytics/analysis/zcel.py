# Copyright (c) 2025 Daniel Fry
# MIT License. See LICENSE file in the project root for full license text.
#
"""
ZCell ADCP (Acoustic Doppler Current Profiler) analysis and visualization functions.

This module provides specialized plotting functions for analyzing current profile data
from ZCell ADCP sensors, including timeseries, distributions, and oceanographic
visualizations.
"""

from typing import Tuple, List, Optional
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.figure import Figure
from matplotlib.axes import Axes


def plot_engineering_timeseries(
    df: pd.DataFrame,
    timestamp_col: str = 'TIMESTAMP',
    title: str = 'ZCell Engineering Parameters Over Time',
    figsize: Tuple[int, int] = (14, 12)
) -> Tuple[Figure, List[Axes]]:
    """
    Plot ZCell ADCP engineering parameters as timeseries.
    
    Visualizes key engineering metrics including battery voltages, temperatures,
    pressure, and instrument orientation over time. Useful for assessing instrument
    health and deployment conditions.
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing ZCell data with TIMESTAMP and engineering columns
    timestamp_col : str, default='TIMESTAMP'
        Name of timestamp column
    title : str, default='ZCell Engineering Parameters Over Time'
        Overall plot title
    figsize : tuple of int, default=(14, 12)
        Figure size (width, height) in inches
        
    Returns
    -------
    fig : matplotlib.figure.Figure
        Figure object
    axes : list of matplotlib.axes.Axes
        List of subplot axes (length 6)
        
    Examples
    --------
    >>> from imta_analytics.data import load_toa5_file
    >>> from imta_analytics.analysis.zcel import plot_engineering_timeseries
    >>> df, _, _ = load_toa5_file('ZCelEngData.dat')
    >>> fig, axes = plot_engineering_timeseries(df)
    >>> plt.show()
    """
    params = [
        ('batt_volt', 'V'),
        ('ZCel_Batt', 'V'),
        ('PTemp', '°C'),
        ('ZCel_WTmp', '°C'),
        ('ZCel_Press', 'dBar'),
        ('ZCel_Hdng', '°'),
    ]
    
    fig, axes = plt.subplots(6, 1, figsize=figsize, sharex=True)
    fig.suptitle(title, fontsize=14, fontweight='bold')
    
    for ax, (param, unit) in zip(axes, params):
        if param in df.columns:
            ax.plot(df[timestamp_col], df[param], linewidth=0.8, alpha=0.7)
            ax.set_ylabel(f'{param}\n({unit})', fontsize=10)
            ax.grid(True, alpha=0.3)
            
            # Add reference lines for certain parameters
            if 'volt' in param.lower() or 'batt' in param.lower():
                ax.axhline(y=12, color='r', linestyle='--', alpha=0.3, label='Nominal 12V')
                ax.legend(loc='upper right', fontsize=8)
    
    axes[-1].set_xlabel('Time', fontsize=10)
    plt.tight_layout()
    
    return fig, list(axes)


def compute_depth_averaged_currents(
    df: pd.DataFrame,
    speed_cols: List[str],
    dir_cols: List[str]
) -> pd.DataFrame:
    """
    Compute depth-averaged current speed and direction metrics.
    
    Calculates mean, median, and standard deviation of current speeds across
    all depth bins. Also computes dominant direction using vector averaging.
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing current profile data
    speed_cols : list of str
        Column names for current speeds at each depth bin
    dir_cols : list of str
        Column names for current directions at each depth bin
        
    Returns
    -------
    result_df : pd.DataFrame
        DataFrame with computed metrics:
        - mean_speed: Average speed across all depths
        - median_speed: Median speed across all depths
        - std_speed: Standard deviation of speeds (vertical shear indicator)
        - dominant_direction: Vector-averaged current direction
        
    Examples
    --------
    >>> speed_cols = [col for col in df.columns if col.startswith('CurrSpd')]
    >>> dir_cols = [col for col in df.columns if col.startswith('CurrDir')]
    >>> curr_stats = compute_depth_averaged_currents(df, speed_cols, dir_cols)
    """
    result = df[['TIMESTAMP']].copy() if 'TIMESTAMP' in df.columns else pd.DataFrame(index=df.index)
    
    # Speed statistics
    speeds = df[speed_cols]
    result['mean_speed'] = speeds.mean(axis=1)
    result['median_speed'] = speeds.median(axis=1)
    result['std_speed'] = speeds.std(axis=1)  # Vertical shear indicator
    
    # Vector-averaged direction (correct oceanographic method)
    # Convert to radians
    directions = df[dir_cols]
    dir_rad = np.deg2rad(directions)
    
    # Compute vector components (weighted by speed)
    u_components = speeds.values * np.sin(dir_rad.values)
    v_components = speeds.values * np.cos(dir_rad.values)
    
    # Average vectors
    u_mean = np.nanmean(u_components, axis=1)
    v_mean = np.nanmean(v_components, axis=1)
    
    # Convert back to direction
    result['dominant_direction'] = np.rad2deg(np.arctan2(u_mean, v_mean)) % 360
    
    return result


def plot_depth_averaged_currents(
    df: pd.DataFrame,
    speed_cols: List[str],
    dir_cols: List[str],
    timestamp_col: str = 'TIMESTAMP',
    title: str = 'Depth-Averaged Current Metrics',
    figsize: Tuple[int, int] = (14, 10)
) -> Tuple[Figure, List[Axes]]:
    """
    Plot depth-averaged current speed and direction timeseries.
    
    Shows mean current speed, vertical shear (std dev), and dominant direction
    over time. Useful for identifying flow patterns and stratification.
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing current profile data with TIMESTAMP
    speed_cols : list of str
        Column names for current speeds at each depth bin
    dir_cols : list of str
        Column names for current directions at each depth bin
    timestamp_col : str, default='TIMESTAMP'
        Name of timestamp column
    title : str, default='Depth-Averaged Current Metrics'
        Overall plot title
    figsize : tuple of int, default=(14, 10)
        Figure size (width, height) in inches
        
    Returns
    -------
    fig : matplotlib.figure.Figure
        Figure object
    axes : list of matplotlib.axes.Axes
        List of subplot axes (length 3)
        
    Examples
    --------
    >>> fig, axes = plot_depth_averaged_currents(df, speed_cols, dir_cols)
    >>> plt.show()
    """
    curr_stats = compute_depth_averaged_currents(df, speed_cols, dir_cols)
    
    fig, axes = plt.subplots(3, 1, figsize=figsize, sharex=True)
    fig.suptitle(title, fontsize=14, fontweight='bold')
    
    # Mean speed
    axes[0].plot(df[timestamp_col], curr_stats['mean_speed'], linewidth=0.8, alpha=0.7)
    axes[0].set_ylabel('Mean Speed\n(m/s)', fontsize=10)
    axes[0].grid(True, alpha=0.3)
    
    # Vertical shear (std dev)
    axes[1].plot(df[timestamp_col], curr_stats['std_speed'], linewidth=0.8, alpha=0.7, color='orange')
    axes[1].set_ylabel('Vertical Shear\n(std dev, m/s)', fontsize=10)
    axes[1].grid(True, alpha=0.3)
    
    # Dominant direction
    axes[2].scatter(df[timestamp_col], curr_stats['dominant_direction'], 
                    s=5, alpha=0.5, c=curr_stats['mean_speed'], cmap='viridis')
    axes[2].set_ylabel('Dominant Direction\n(°)', fontsize=10)
    axes[2].set_ylim([0, 360])
    axes[2].set_yticks([0, 90, 180, 270, 360])
    axes[2].set_yticklabels(['N', 'E', 'S', 'W', 'N'])
    axes[2].grid(True, alpha=0.3)
    
    axes[-1].set_xlabel('Time', fontsize=10)
    plt.tight_layout()
    
    return fig, list(axes)


def plot_current_speed_heatmap(
    df: pd.DataFrame,
    speed_cols: List[str],
    depth_cols: List[str],
    timestamp_col: str = 'TIMESTAMP',
    title: str = 'Current Speed by Depth Over Time',
    figsize: Tuple[int, int] = (14, 8),
    cmap: str = 'viridis',
    vmax: Optional[float] = None
) -> Tuple[Figure, Axes]:
    """
    Create depth-time heatmap showing current speeds at all depths.
    
    Visualizes the full vertical structure of currents over time. Useful for
    identifying stratification, internal waves, and vertical shear patterns.
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing current profile data
    speed_cols : list of str
        Column names for current speeds at each depth bin (ordered surface to bottom)
    depth_cols : list of str
        Column names for depths corresponding to each speed measurement
    timestamp_col : str, default='TIMESTAMP'
        Name of timestamp column
    title : str, default='Current Speed by Depth Over Time'
        Plot title
    figsize : tuple of int, default=(14, 8)
        Figure size (width, height) in inches
    cmap : str, default='viridis'
        Colormap name
    vmax : float, optional
        Maximum value for colormap scaling. If None, uses data maximum.
        
    Returns
    -------
    fig : matplotlib.figure.Figure
        Figure object
    ax : matplotlib.axes.Axes
        Axes object with heatmap
        
    Examples
    --------
    >>> fig, ax = plot_current_speed_heatmap(df, speed_cols, depth_cols)
    >>> plt.show()
    """
    # Extract speed data
    speed_data = df[speed_cols].values.T  # Transpose so rows are depths
    
    # Get representative depths (use first valid record)
    first_valid_idx = df[depth_cols].notna().all(axis=1).idxmax()
    depths = df.loc[first_valid_idx, depth_cols].values
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # Create heatmap using pcolormesh instead of imshow for better datetime handling
    import matplotlib.dates as mdates
    
    # Convert timestamps to matplotlib date numbers
    time_nums = mdates.date2num(df[timestamp_col].values)
    
    # Create meshgrid for pcolormesh
    X, Y = np.meshgrid(time_nums, depths)
    
    im = ax.pcolormesh(
        X,
        Y,
        speed_data,
        cmap=cmap,
        vmin=0,
        vmax=vmax,
        shading='nearest'
    )
    
    # Invert y-axis so surface is at top
    ax.invert_yaxis()
    
    # Format x-axis as dates
    ax.xaxis_date()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    
    ax.set_xlabel('Time', fontsize=12)
    ax.set_ylabel('Depth (m)', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=ax, label='Current Speed (m/s)')
    
    plt.tight_layout()
    
    return fig, ax


def plot_current_speed_distributions(
    df: pd.DataFrame,
    speed_cols: List[str],
    depth_cols: List[str],
    title: str = 'Current Speed Distributions by Depth',
    figsize: Tuple[int, int] = (14, 10)
) -> Tuple[Figure, Axes]:
    """
    Create box plots showing current speed distributions at each depth bin.
    
    Useful for understanding speed variability at different depths and
    identifying depth-dependent flow characteristics.
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing current profile data
    speed_cols : list of str
        Column names for current speeds at each depth bin
    depth_cols : list of str
        Column names for depths corresponding to each speed measurement
    title : str, default='Current Speed Distributions by Depth'
        Plot title
    figsize : tuple of int, default=(14, 10)
        Figure size (width, height) in inches
        
    Returns
    -------
    fig : matplotlib.figure.Figure
        Figure object
    ax : matplotlib.axes.Axes
        Axes object with box plot
        
    Examples
    --------
    >>> fig, ax = plot_current_speed_distributions(df, speed_cols, depth_cols)
    >>> plt.show()
    """
    # Get representative depths
    first_valid_idx = df[depth_cols].notna().all(axis=1).idxmax()
    depths = df.loc[first_valid_idx, depth_cols].values
    
    # Prepare data for box plot
    speed_data = [df[col].dropna().values for col in speed_cols]
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # Create horizontal box plot
    bp = ax.boxplot(
        speed_data,
        vert=False,
        labels=[f'{d:.1f}m' for d in depths],
        patch_artist=True,
        showfliers=False  # Hide outliers for cleaner plot
    )
    
    # Color boxes by depth (darker = deeper)
    colors = plt.cm.Blues(np.linspace(0.4, 0.9, len(speed_cols)))
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    ax.set_xlabel('Current Speed (m/s)', fontsize=12)
    ax.set_ylabel('Depth', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    
    return fig, ax


def plot_current_direction_polar(
    df: pd.DataFrame,
    dir_cols: List[str],
    depth_cols: List[str],
    depth_layers: Optional[List[str]] = None,
    title: str = 'Current Direction Distribution by Depth',
    figsize: Tuple[int, int] = (14, 10)
) -> Tuple[Figure, List[Axes]]:
    """
    Create polar histograms (rose diagrams) showing current direction distributions.
    
    Displays directional frequency at different depth layers. Useful for
    identifying dominant flow patterns and directional variability.
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing current profile data
    dir_cols : list of str
        Column names for current directions at each depth bin
    depth_cols : list of str
        Column names for depths corresponding to each direction measurement
    depth_layers : list of str, optional
        Labels for depth layers ['Surface', 'Mid', 'Bottom']. If None, uses first,
        middle, and last depth bins.
    title : str, default='Current Direction Distribution by Depth'
        Overall plot title
    figsize : tuple of int, default=(14, 10)
        Figure size (width, height) in inches
        
    Returns
    -------
    fig : matplotlib.figure.Figure
        Figure object
    axes : list of matplotlib.axes.Axes
        List of polar subplot axes
        
    Examples
    --------
    >>> fig, axes = plot_current_direction_polar(df, dir_cols, depth_cols)
    >>> plt.show()
    """
    # Select representative depth bins
    n_bins = len(dir_cols)
    if depth_layers is None:
        indices = [0, n_bins // 2, n_bins - 1]
        depth_layers = ['Surface', 'Mid-depth', 'Bottom']
    else:
        indices = [0, n_bins // 2, n_bins - 1]
    
    selected_cols = [dir_cols[i] for i in indices]
    
    # Get actual depths
    first_valid_idx = df[depth_cols].notna().all(axis=1).idxmax()
    depths = df.loc[first_valid_idx, depth_cols].values
    selected_depths = [depths[i] for i in indices]
    
    fig, axes = plt.subplots(1, 3, figsize=figsize, subplot_kw={'projection': 'polar'})
    fig.suptitle(title, fontsize=14, fontweight='bold', y=0.98)
    
    # Number of directional bins
    n_dir_bins = 36  # 10-degree bins
    dir_bins = np.linspace(0, 360, n_dir_bins + 1)
    
    for ax, col, layer, depth in zip(axes, selected_cols, depth_layers, selected_depths):
        # Get directions and convert to radians
        directions = df[col].dropna()
        dir_rad = np.deg2rad(directions)
        
        # Create histogram
        counts, bin_edges = np.histogram(directions, bins=dir_bins)
        
        # Convert bin edges to radians for plotting
        theta = np.deg2rad(bin_edges[:-1])
        width = np.deg2rad(360 / n_dir_bins)
        
        # Plot bars
        bars = ax.bar(theta, counts, width=width, alpha=0.7)
        
        # Color bars by magnitude
        colors = plt.cm.viridis(counts / counts.max())
        for bar, color in zip(bars, colors):
            bar.set_facecolor(color)
        
        # Configure polar plot
        ax.set_theta_zero_location('N')
        ax.set_theta_direction(-1)  # Clockwise
        ax.set_title(f'{layer}\n({depth:.1f}m)', fontsize=11, pad=15)
        ax.set_xticks(np.deg2rad([0, 45, 90, 135, 180, 225, 270, 315]))
        ax.set_xticklabels(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])
    
    plt.tight_layout()
    
    return fig, list(axes)


def plot_engineering_correlations(
    df: pd.DataFrame,
    params: Optional[List[str]] = None,
    title: str = 'ZCell Engineering Parameters Correlation Matrix',
    figsize: Tuple[int, int] = (10, 8)
) -> Tuple[Figure, Axes, pd.DataFrame]:
    """
    Create correlation heatmap for engineering parameters.
    
    Shows relationships between battery voltages, temperatures, pressure,
    and orientation parameters. Useful for identifying sensor dependencies
    and environmental correlations.
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing ZCell engineering data
    params : list of str, optional
        List of parameter names to correlate. If None, uses default set.
    title : str, default='ZCell Engineering Parameters Correlation Matrix'
        Plot title
    figsize : tuple of int, default=(10, 8)
        Figure size (width, height) in inches
        
    Returns
    -------
    fig : matplotlib.figure.Figure
        Figure object
    ax : matplotlib.axes.Axes
        Axes object with heatmap
    corr_matrix : pd.DataFrame
        Correlation matrix
        
    Examples
    --------
    >>> fig, ax, corr = plot_engineering_correlations(df)
    >>> plt.show()
    """
    if params is None:
        params = ['batt_volt', 'PTemp', 'ZCel_Batt', 'ZCel_Hdng', 
                  'ZCel_Pitch', 'ZCel_Roll', 'ZCel_Press', 'ZCel_WTmp']
    
    # Filter to existing columns
    params = [p for p in params if p in df.columns]
    
    # Compute correlation matrix
    corr_matrix = df[params].corr()
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # Create heatmap
    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt='.2f',
        cmap='RdBu_r',
        center=0,
        vmin=-1,
        vmax=1,
        square=True,
        linewidths=0.5,
        cbar_kws={'label': 'Correlation Coefficient'},
        ax=ax
    )
    
    ax.set_title(title, fontsize=14, fontweight='bold', pad=15)
    plt.tight_layout()
    
    return fig, ax, corr_matrix
