# Copyright (c) 2025 Daniel Fry
# MIT License. See LICENSE file in the project root for full license text.
#
"""Analysis utilities for IMTA data."""

from .visualization import (
    plot_timeseries_grid,
    plot_availability_timeline,
    plot_correlation_heatmap,
    plot_current_profile,
)

from .zcel import (
    plot_engineering_timeseries,
    compute_depth_averaged_currents,
    plot_depth_averaged_currents,
    plot_current_speed_heatmap,
    plot_current_speed_distributions,
    plot_current_direction_polar,
    plot_engineering_correlations,
)

__all__ = [
    'plot_timeseries_grid',
    'plot_availability_timeline',
    'plot_correlation_heatmap',
    'plot_current_profile',
    'plot_engineering_timeseries',
    'compute_depth_averaged_currents',
    'plot_depth_averaged_currents',
    'plot_current_speed_heatmap',
    'plot_current_speed_distributions',
    'plot_current_direction_polar',
    'plot_engineering_correlations',
]
