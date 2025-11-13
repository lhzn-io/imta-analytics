---
title: "UNH Aquafort Data Exploration Findings"
subtitle: "Initial Analysis Results and Data Processing Pipeline"
author: "IMTA Analytics Team"
date: "November 13, 2025"
---

**Project:** IMTA Analytics - UNH Aquafort Buoy Station  
**Previous Analysis:** [20251104-data-format-analysis.md](20251104-data-format-analysis.md)

## Executive Summary

Following the successful implementation of TOA5 data loaders and quality control procedures, we conducted comprehensive exploratory data analysis on both EXO2 water quality and ZCell ADCP datasets. This document presents key findings from visualization analysis and documents the production-ready data processing pipeline.

**Key Achievements:**

- Successfully cleaned and validated 9+ months of continuous monitoring data
- Identified distinct seasonal patterns in water temperature and biological activity
- Characterized current regime with strong tidal influence and vertical stratification
- Established optimized data formats (Feather/Parquet) for streaming analytics
- Documented data quality issues and implemented automated filtering

## 1. Data Processing Pipeline

### 1.1 Quality Control Workflow

The implemented two-stage quality control process successfully handles both Campbell Scientific-specific issues and physical parameter validation:

#### Stage 1: Campbell Scientific Sentinel Conversion

- Automatically converts sentinel values (-7999, -2147483648, ±6999, ±7999) to NaN
- Implemented in `load_toa5_file()` function
- References: CR1000X Product Manual, Section 14.2 "Understanding NAN"

#### Stage 2: Physical Bounds Filtering

- EXO2 Water Quality Parameters:
  - Temperature: -2 to 35°C (freezing to tropical)
  - Salinity: 0 to 40 psu (fresh to hypersaline)
  - pH: 6.5 to 9.5 (marine range)
  - Dissolved Oxygen: 0 to 200% saturation
  - Chlorophyll: -1 to 100 RFU
  - Turbidity: 0 to 100 FNU
  - Depth: -1 to 100 m
  - Specific Conductivity: 0 to 70 mS/cm

- ZCell Engineering Parameters:
  - Battery Voltage: 9 to 16V (12V system)
  - Panel Temperature: -5 to 40°C
  - Heading: 0 to 360 degrees
  - Pitch/Roll: -45 to 45 degrees
  - Pressure: 0 to 100 dBar (0-100m depth)
  - Water Temperature: -2 to 35°C

**Results:**

- EXO2: ~4-6% of readings filtered as physically impossible
- ZCell: Minimal filtering required (mostly sentinel conversions)
- Valid records maintained temporal continuity

### 1.2 Optimized Storage Formats

Successfully converted cleaned datasets to production-ready formats:

**EXO2 Water Quality Data (Cleaned):**

- Feather: 1.64 MB (optimized for fast streaming reads)
- Parquet: 0.95 MB (42% compression, archival storage)
- Compression ratio: 1.73x (Feather vs Parquet)

**ZCell Current Profiler Data (Cleaned):**

- Feather: 6.70 MB (optimized for fast streaming reads)
- Parquet: 3.03 MB (55% compression, archival storage)
- Compression ratio: 2.21x (Feather vs Parquet)

**Performance Characteristics:**

- Feather read speed: ~10-20ms for full dataset reload
- Parquet read speed: ~30-50ms for full dataset reload
- Both formats preserve Arrow schema for zero-copy streaming
- Suitable for real-time simulation and replay scenarios

## 2. Water Quality Analysis Findings

### 2.1 Temporal Coverage and Data Quality

**Dataset Characteristics:**

- **Duration:** January 2025 to October 2025 (~9 months)
- **Sampling Interval:** 15 minutes (most common)
- **Total Records:** Variable by deployment phase
- **Data Availability:**
  - Excellent coverage January-February 2025
  - Gap in late February to mid-March 2025
  - Continuous coverage April-October 2025

**Quality Issues Identified:**

- Duplicate timestamps present (requires deduplication)
- Sensor error codes successfully filtered by bounds checking
- Missing data periods correspond to maintenance/deployment events

### 2.2 Seasonal Water Temperature Patterns

**Observed Trends (from Water Quality Parameters Over Time plot):**

- **Winter (Jan-Feb):** ~2-5°C baseline
- **Spring Warming (Mar-May):** Gradual increase to ~10-15°C
- **Summer (Jun-Aug):** Peak temperatures ~15-20°C
- **Fall Cooling (Sep-Oct):** Declining to ~10-15°C

**Biological Significance:**

- Temperature range suitable for cold-water aquaculture species
- Seasonal variation influences dissolved oxygen solubility
- Critical for kelp growth season timing (spring/fall optimal)

### 2.3 Salinity and Conductivity Patterns

**Key Observations (from cleaned timeseries):**

- **Baseline Salinity:** ~30-32 psu (typical Gulf of Maine coastal water)
- **Conductivity:** Tracks salinity with expected temperature compensation
- **Variability Events:**
  - Sharp salinity drops visible in spring (likely freshwater runoff)
  - Brief hyposaline events (<20 psu) during precipitation/melt
  - Rapid recovery to baseline indicates strong tidal mixing

**Correlation Analysis Results:**

- Specific Conductivity vs Salinity: r = 0.99 (perfect positive correlation)
- Temperature vs Conductivity: r = -0.17 (weak negative, expected)
- Salinity vs Temperature: r = -0.03 (minimal correlation)

### 2.4 Dissolved Oxygen Dynamics

**Distribution Characteristics (from histograms):**

- **Mean DO (% saturation):** 103.80%
- **Standard Deviation:** 6.62%
- **Range:** 60-140% (post-cleaning)
- **Distribution:** Slightly right-skewed, near-normal

**Key Patterns:**

- Generally supersaturated conditions (beneficial for aquaculture)
- Negative correlation with temperature (r = -0.23, expected inverse solubility)
- Positive correlation with pH (r = 0.49, photosynthesis linkage)
- Positive correlation with internal power (r = 0.45, likely artifact)

**Biological Implications:**

- Excellent oxygenation for fish/shellfish culture
- Supersaturation suggests active photosynthesis during measurement periods
- Low DO events (<80%) rare and brief

### 2.5 pH Variability

**Distribution Characteristics:**

- **Mean pH:** 8.06
- **Standard Deviation:** 0.07
- **Range:** 7.6-8.6 (post-cleaning)
- **Distribution:** Normal distribution centered at 8.06

**Temporal Patterns:**

- Relatively stable throughout monitoring period
- Brief acidification events (<7.9) visible in timeseries
- Strong negative correlation with temperature (r = -0.23)
- Weak correlation with most other parameters

### 2.6 Chlorophyll and Turbidity Events

**Chlorophyll Fluorescence:**

- **Mean:** 0.43 RFU
- **High-Variance Distribution:** σ = 0.39 RFU
- **Episodic Bloom Events:** Several peaks >2 RFU visible in timeseries
- **Seasonality:** Higher chlorophyll in spring/summer months

**Turbidity:**

- **Mean:** 2.53 FNU
- **High-Variance Distribution:** σ = 3.78 FNU
- **Extreme Events:** Occasional spikes >20 FNU (storm/resuspension)
- **Correlation:** Moderate positive with temperature (r = 0.33)

**Biological Context:**

- Bloom events correspond to spring/summer phytoplankton productivity
- Turbidity spikes likely storm-driven sediment resuspension
- Negative correlation between turbidity and DO (r = -0.33) suggests light limitation during high-turbidity events

### 2.7 Depth Sensor Analysis

**Observed Characteristics:**

- **Mean Depth:** 0.37 m
- **Standard Deviation:** 0.09 m
- **Range:** 0.0-0.8 m (post-cleaning)

**Interpretation:**

- Likely measures sonde depth below surface (not total water column depth)
- Variability suggests tidal influence or wave action
- Positive correlation with temperature (r = 0.33) may indicate surface heating effects

## 3. Current Profile Analysis Findings

### 3.1 Vertical Current Structure

**Key Observations (from Current Speed by Depth heatmap):**

- **Surface Layer (0-5m):** Highest velocities, frequently >0.2 m/s
- **Mid-depth (5-15m):** Moderate velocities, 0.1-0.2 m/s
- **Bottom Layer (15-20m):** Reduced velocities, often <0.1 m/s
- **Vertical Stratification:** Clear shear visible between layers

**Temporal Patterns:**

- Strong tidal modulation (12.4-hour periodicity visible)
- Enhanced currents during January-February period
- Reduced flow velocities March-April (data gap period)
- Resumption of strong tidal currents April-October

### 3.2 Current Speed Distributions

**Depth-Dependent Statistics (from box plot analysis):**

- **Surface (0m):** Mean ~0.08 m/s, max ~0.3 m/s, high variance
- **Mid-depth (10m):** Mean ~0.12 m/s, max ~0.4 m/s, moderate variance
- **Bottom (19m):** Mean ~0.08 m/s, max ~0.3 m/s, lower variance

**Key Findings:**

- Mid-depth layer exhibits strongest mean currents
- Surface layer shows highest variability (wind/wave influence)
- Bottom layer more consistent (reduced turbulence)

### 3.3 Directional Current Patterns

**Dominant Flow Directions (from polar histograms):**

- **Surface (0m):** Strong northward flow dominance (~16,000 observations)
- **Mid-depth (10m):** Similar northward preference (~16,000 observations)
- **Bottom (19m):** Strong northward flow (~16,000 observations)

**Interpretation:**

- Highly directional flow regime (not omnidirectional)
- Likely tidal channel or coastal current influence
- Minimal directional shear between depth layers (vertically coherent)
- Bidirectional tidal flow (north-south oscillation)

### 3.4 Depth-Averaged Current Metrics

**Mean Speed Timeseries:**

- Baseline: 0.05-0.15 m/s
- Tidal peaks: 0.20-0.30 m/s
- Clear fortnightly (spring/neap) tidal modulation visible

**Vertical Shear (Standard Deviation):**

- Typical: 0.02-0.05 m/s
- Enhanced during peak currents: up to 0.15 m/s
- Indicates stronger stratification during flood/ebb tides

**Dominant Direction Scatter:**

- Bidirectional pattern clear (N and S modes)
- Directional variability during slack tides (intermediate directions)

### 3.5 Engineering Parameter Correlations

**Strong Correlations Identified:**

- **Panel Temp vs Water Temp:** r = 0.85 (thermal equilibrium)
- **ZCell Battery vs Internal Battery:** r = 0.46 (moderate positive)
- **Pressure vs Water Temp:** r = 0.58 (depth-temperature coupling)

**Sensor Health Indicators:**

- Battery voltages stable at ~12-13V (nominal 12V system)
- Heading stable with minimal drift
- Pitch/Roll within normal operational range
- Pressure readings decrease over deployment (expected drift or biofouling)

## 4. Cross-Dataset Correlation Opportunities

Based on temporal overlap between EXO2 and ZCell datasets, future analyses can investigate:

1. **Current-Water Quality Coupling:**
   - DO response to tidal flushing
   - Salinity modulation by tidal currents
   - Turbidity resuspension during strong currents

2. **Stratification Analysis:**
   - Temperature gradient vs current shear
   - Vertical mixing during storm events
   - Tidal stratification breakdown

3. **Biological-Physical Interactions:**
   - Chlorophyll bloom timing vs current patterns
   - Nutrient delivery via tidal advection
   - Particle transport and sedimentation

## 5. Data Quality Metrics Summary

### 5.1 EXO2 Dataset Quality

**Original Dataset:**

- Total Records: ~35,000-40,000
- Columns: 16 parameters
- Raw Missing Data: Variable by parameter

**Cleaned Dataset:**

- Sentinel Conversions: ~1,500-2,000 values
- Physical Bounds Filtering: ~1,500-2,000 additional values
- Final Valid Records: >95% of original
- Quality Flags: Maintained in processing metadata

### 5.2 ZCell Dataset Quality

**Original Dataset:**

- Total Records: ~50,000-60,000
- Columns: 77 parameters (20 depth bins × 3 measurements + 17 engineering)
- Raw Missing Data: Minimal in engineering params

**Cleaned Dataset:**

- Sentinel Conversions: ~500-1,000 values
- Physical Bounds Filtering: <100 additional values
- Final Valid Records: >98% of original
- Current Profile Completeness: Excellent

## 6. Implications for IMTA Analytics

### 6.1 Aquaculture Suitability Assessment

**Favorable Conditions Identified:**

- Consistent tidal flushing (0.1-0.3 m/s currents)
- Excellent dissolved oxygen (>100% saturation typical)
- Stable salinity (30-32 psu marine conditions)
- Moderate turbidity (low biofouling risk)

**Seasonal Considerations:**

- Winter: Cold temperatures limit growth rates
- Spring: Optimal kelp growing season, bloom events
- Summer: Peak temperatures, highest chlorophyll
- Fall: Declining temperatures, optimal harvest timing

### 6.2 Multi-Trophic Integration Opportunities

**Vertical Zonation:**

- **Surface (0-5m):** Kelp culture zone, high light, strong currents
- **Mid-depth (5-15m):** Shellfish culture zone, moderate flow, particle capture
- **Bottom (15-20m):** Benthic habitat, reduced currents, detritus accumulation

**Nutrient Cycling:**

- Tidal flushing provides nutrient renewal
- Chlorophyll blooms indicate productivity
- DO supersaturation suggests net photosynthesis

### 6.3 Real-Time Monitoring Dashboard Requirements

Based on analysis findings, dashboard should feature:

1. **Water Quality Panel:**
   - Temperature, salinity, DO, pH (real-time trends)
   - Alarm thresholds for critical parameters
   - Bloom detection (chlorophyll spikes)

2. **Current Profile Panel:**
   - Depth-averaged speed/direction
   - Vertical shear indicator
   - Tidal phase prediction

3. **Data Quality Panel:**
   - Sensor health metrics (battery, pitch/roll)
   - Missing data indicators
   - Automatic quality flagging

## 7. Next Steps and Recommendations

### 7.1 Immediate Priorities

1. **Tidal Analysis:**
   - Implement harmonic analysis for tidal constituents
   - Calculate spring/neap tidal cycles
   - Predict optimal deployment/harvest windows

2. **Feature Engineering:**
   - Derive Richardson number (stratification indicator)
   - Calculate water density from T/S
   - Compute tidal phase indicators

3. **Correlation Analysis:**
   - Cross-correlate EXO2 and ZCell datasets
   - Lag analysis for current-water quality coupling
   - Identify predictive relationships

### 7.2 Advanced Analytics

1. **Predictive Modeling:**
   - Dissolved oxygen forecasting
   - Chlorophyll bloom prediction
   - Water quality anomaly detection

2. **Streaming Analytics:**
   - Implement real-time QC using Feather format
   - Develop sliding window aggregations
   - Alert system for out-of-bounds conditions

3. **Visualization Enhancements:**
   - Interactive plotly dashboards
   - 3D current vector fields
   - Animated tidal cycle visualizations

## 8. Technical Implementation Notes

### 8.1 Data Loading Best Practices

```python
from imta_analytics.data import load_toa5_file
import pandas as pd

# Initial load from TOA5 format
df, metadata, units = load_toa5_file('path/to/file.dat')

# Fast reload from processed formats
df_fast = pd.read_feather('data/processed/exo2_data.feather')  # ~10-20ms
df_archive = pd.read_parquet('data/processed/exo2_data.parquet')  # ~30-50ms
```

### 8.2 Quality Control Pipeline

```python
from imta_analytics.data import apply_quality_bounds

# Apply physical bounds filtering
df_clean = apply_quality_bounds(df, parameter_type='water_quality')

# Export in both formats
df_clean.to_feather('output.feather', compression='lz4')
df_clean.to_parquet('output.parquet', compression='zstd')
```

### 8.3 Visualization Utilities

```python
from imta_analytics.analysis import (
    plot_timeseries_grid,
    plot_current_profile,
    plot_correlation_heatmap,
)
from imta_analytics.analysis.zcel import (
    plot_engineering_timeseries,
    plot_depth_averaged_currents,
    plot_current_speed_heatmap,
)

# All plotting functions now available in imta_analytics package
```

## 9. References and Resources

### 9.1 Data Format Documentation

- TOA5 Format Analysis (Nov 4, 2025)
- Campbell Scientific CR1000X Product Manual, Section 14.2 "Understanding NAN"
- Campbell Scientific Sentinel Values Documentation

### 9.2 Analysis Notebooks

- `notebooks/01_initial_data_exploration.ipynb` - Main EDA notebook
- Future: `notebooks/02_tidal_analysis.ipynb` - Harmonic analysis
- Future: `notebooks/03_predictive_models.ipynb` - ML models

### 9.3 Package Documentation

- IMTA Analytics Package Overview
- Data Loading Module (`imta_analytics/data/loaders.py`)
- Analysis Module (`imta_analytics/analysis/`)

---

**Document Status:** Initial Release  
**Last Updated:** November 13, 2025  
**Next Review:** After tidal analysis completion
