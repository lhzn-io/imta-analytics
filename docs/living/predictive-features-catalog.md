# Predictive Features Catalog for IMTA Analytics

**Status:** Work in Progress - Living Document  
**Last Updated:** November 12, 2025  
**Purpose:** Comprehensive catalog of derived parameters and engineered features for predictive modeling in IMTA analytics  
**Scope:** Systematic coverage of planned features organized by domain, temporal scale, and functional purpose

---

## Document Status & Roadmap

This document serves as the authoritative reference for all engineered features in the IMTA analytics platform. It consolidates feature definitions from:

- Notebook analysis plans (`notebooks/01_initial_data_exploration.ipynb`)
- UNH Aquafort case study requirements (`docs/planning/unh-aquafort-case-study-learning-phase.md`)
- Literature review findings (`refs/Literature Review - Data Science & AI Applications in Sustainable Aquaculture Systems.md`)

**Document Scope:**

All features documented here are planned for implementation. Features are categorized by:

- **Core Features** - Direct implementation from available sensor data
- **Literature-Driven Features** - Require parameter extraction from ongoing Tier 1 paper review
- **Implemented Features** - Currently exist in codebase (explicitly noted with file references)

**Next Review:** After completion of Tier 1 literature review (Week 2-3)

---

## Overview

This document catalogs derived parameters and engineered features for analyzing integrated multi-trophic aquaculture (IMTA) systems using environmental sensor data. 

Features are organized by physical domain (oceanography, water chemistry, biology), temporal scale (instantaneous to inter-annual), and functional purpose (monitoring, prediction, optimization). Each feature includes implementation guidance, validation criteria, and literature references where applicable.

## 1. Physical Oceanography Parameters

**Category:** Core features  
**Priority:** High - Required for stratification analysis and mixing dynamics

### 1.1 Richardson Number (Ri)

A dimensionless parameter that quantifies the ratio of buoyancy forces (from density stratification) to shear forces (from velocity gradients) in a fluid. It indicates the stability of stratified flow.

**Interpretation:**
- Ri > 1: Stable stratification (buoyancy dominates, suppresses mixing)
- Ri < 0.25: Unstable flow (shear dominates, promotes turbulent mixing)
- Critical value Ri ≈ 0.25 marks transition from laminar to turbulent flow

**Formula:**

```text
Ri = (g/ρ)(dρ/dz) / (du/dz)²
```

Where:
- g = gravitational acceleration (9.81 m/s²)
- ρ = water density (kg/m³)
- dρ/dz = vertical density gradient (kg/m⁴)
- du/dz = vertical velocity shear (s⁻¹)

**Aquaculture Applications:**

Richardson number helps assess vertical mixing potential, which affects:
- Nutrient distribution in the water column
- Dissolved oxygen transport to depth
- Waste dispersion away from farm sites
- Stratification stability affecting fish behavior and distribution

**Implementation Notes:**

For practical calculation from buoy data:
1. Compute water density from temperature and salinity using equation of state
2. Estimate vertical gradients from multi-depth sensor data
3. Calculate velocity shear from ADCP current profiles at different depths
4. Handle edge cases (zero shear, homogeneous density)

**Literature Context:**

While Richardson number is a standard oceanographic parameter, it is not explicitly discussed in the available IMTA literature. Its application to aquaculture site assessment appears in oceanographic engineering contexts rather than biological/ecological IMTA research.

### 1.2 Water Density

**Category:** Core feature - Foundational parameter  
**Priority:** High - Required for Richardson number and stratification index

**Formula (simplified):**

```text
ρ = ρ₀ + α(T - T₀) + β(S - S₀)
```

Where:
- ρ₀ = reference density (1025 kg/m³ for seawater)
- α = thermal expansion coefficient
- β = haline contraction coefficient
- T = temperature (°C)
- S = salinity (PSU)

For precise calculations, use full equation of state (e.g., TEOS-10).

### 1.3 Stratification Index

**Category:** Core feature  
**Priority:** Medium - Water column stability indicator

**Formula:**

```text
SI = (ρ_bottom - ρ_surface) / ρ_mean
```

**Aquaculture Applications:**

- Predicts nutrient mixing potential
- Indicates risk of thermal stratification events
- Affects waste dispersion patterns

---

## 2. Current & Hydrodynamics Features

**Category:** Core features - ADCP data integration required  
**Priority:** High - Critical for waste dispersion and cage orientation

### 2.1 Current Magnitude

```text
|V| = √(u² + v²)
```

Where u and v are east-west and north-south velocity components.

### 2.2 Current Direction

```text
θ = atan2(v, u)
```

Direction in degrees from which current flows.

### 2.3 Current Persistence

Measure of directional stability over time windows:
- Vector-averaged vs scalar-averaged current speed
- Directional variance
- Autocorrelation of velocity components

### 2.4 Residence Time

**Category:** Literature-driven feature  
**Priority:** Medium - Nutrient uptake efficiency  
**Citation:** Kerrigan et al. (2016) - Spatial configuration meta-analysis

Water parcel residence time near extractive species (mussels, kelp). Longer residence = better nutrient capture.

**Planned Implementation:**

- Particle tracking from current profiles
- Integration over tidal cycles
- Spatial mapping around cage arrays

---

## 3. Tidal Parameters

**Category:** Core features - Requires tidal prediction API or local harmonic analysis  
**Priority:** Medium - Influences feeding behavior and nutrient cycling

### 3.1 Tidal Phase Indicators

- Time since high/low tide
- Rising vs falling tide classification
- Spring/neap cycle position
- Tidal range (for the current cycle)

---

## 4. Water Quality Derivatives

**Category:** Core features  
**Priority:** High - Critical for fish welfare and alert system

### 4.1 Oxygen Saturation Deficit

```text
DO_deficit = DO_sat - DO_measured
```

Indicates biological demand or production.

### 4.2 Oxygen Saturation Percentage

**Formula:**

```text
DO_sat% = (DO_measured / DO_saturation) × 100
```

Critical thresholds:

- < 70%: Stress threshold for salmonids
- < 50%: Severe hypoxia risk

### 4.3 Temperature-Salinity Relationships

- T-S diagrams for water mass identification
- Stratification index from vertical profiles
- Mixed layer depth estimation

### 4.4 Conductivity

**Category:** Core feature  
**Priority:** High - Strong DO predictor in intensive aquaculture  
**Citation:** Xu et al. (2025) - CNN-SA-BiSRU model inputs

**Applications:**

- Salinity proxy (conductivity ∝ salinity + temperature)
- Water mass identification
- Predictor variable for DO forecasting (R²=0.9765 model input)
- Dilution/mixing event detection

**Implementation Notes:**

Xu et al. demonstrated conductivity as critical input for state-of-the-art DO prediction. Use alongside temperature and pH for multivariate time-series forecasting.

### 4.5 pH Variability

**Category:** Literature-driven feature  
**Priority:** Medium - Indicator of metabolic activity  
**Citations:**

- Chambers et al. (2024) - UNH Aquafort case study data
- Xu et al. (2025) - pH as DO model predictor

Daily pH range and rate of change. High variability suggests intense photosynthesis/respiration cycles. Also serves as input feature for DO prediction models.

### 4.6 Chlorophyll-a Concentration

**Category:** Literature-driven feature  
**Priority:** High - HAB risk and food availability  
**Citation:** Chatziantoniou et al. (2023) - Aquasafe platform satellite integration methods

From satellite (Sentinel-2/3) or in-situ fluorometry.

**Applications:**

- Harmful algal bloom early warning
- Mussel food availability estimation
- Light attenuation for kelp photosynthesis

---

## 5. Time-Based Features

**Category:** Core features - Essential for predictive models  
**Priority:** High - Captures seasonal and diurnal patterns

### 5.1 Diurnal Patterns

- Hour of day (circular encoding)
- Day/night classification
- Solar elevation angle
- Photoperiod position

### 5.2 Seasonal Indicators

- Day of year (circular encoding)
- Season classification
- Growing degree days (for biological processes)

### 5.3 High-Frequency Temporal Features

**Category:** Core feature  
**Priority:** High - Real-time DO prediction  
**Citation:** Xu et al. (2025) - 10-minute interval IoT data

**Features for Short-Term Forecasting:**

- **Temporal lags**: DO(t-1), DO(t-2), ..., DO(t-n) for n=6-12 steps (1-2 hours)
- **Rate of change**: ΔDO/Δt, Δ²DO/Δt² (first and second derivatives)
- **Rolling statistics**: 30-min, 1-hour, 6-hour windows
  - Rolling mean, std, min, max
  - Coefficient of variation
- **Autocorrelation features**: Lag-1, lag-6, lag-12 autocorrelation
- **Time since anomaly**: Minutes since last DO spike/drop

**Implementation Notes:**

Xu et al. achieved R²=0.9765 using 10-minute sensor intervals. High-frequency data enables real-time prediction (immediate next timestep) vs longer-horizon forecasting (24-48 hours).

**Validation:**

- Training/test split: 80/20 (2790/698 samples from Xu et al.)
- Window size optimization: Test 30-min, 1-hr, 6-hr aggregations
- Feature importance analysis via CNN attention weights

---

## 6. Bioenergetic & Growth Features

**Category:** Literature-driven features - Requires DEB model implementation  
**Priority:** High - Core predictive capability for yield forecasting

### 6.1 Dynamic Energy Budget (DEB) Parameters

**Category:** Literature-driven feature  
**Priority:** Critical - Foundation for growth prediction  
**Citations:**

- Venolia et al. (2020) - Sugar kelp DEB model
- Stavrakidis-Zachou et al. (2019) - Fish DEB methodology

**Planned Features:**

- **Specific Growth Rate (SGR)** - %/day biomass increase
- **Feed Conversion Ratio (FCR)** - Feed consumed / weight gained
- **Temperature Correction Factors** - Arrhenius scaling for metabolic rates
- **Reserve Density** - Energy reserves relative to structure (DEB state variable)

**Implementation Roadmap:**

1. Extract DEB parameters from Venolia et al. for kelp
2. Adapt Stavrakidis-Zachou framework for steelhead trout
3. Calibrate using Chambers et al. (2024) UNH Aquafort production data
4. Validate against independent growth trials

### 6.2 Kelp Growth Rate

**Category:** Literature-driven feature  
**Citation:** Venolia et al. (2020) - 0.77 cm/day winter to 3.52 cm/day spring

**Formula (from literature):**

Temperature-dependent growth with nutrient limitation and light attenuation factors.

**Critical Parameters:**

- Optimal temperature: 10-15°C
- Light saturation: ~100 μmol photons/m²/s
- Nutrient uptake kinetics (N, P)

### 6.3 Mussel Filtration Rate

**Category:** Literature-driven feature  
**Citation:** Maar et al. (2015) cited in Chambers et al. (2024)

Temperature and salinity-dependent filtration rate affecting phytoplankton removal.

**Applications:**

- Nutrient uptake estimation
- Water quality improvement quantification
- Stocking density optimization

### 6.4 Fish Metabolic Rate

**Category:** Literature-driven feature  
**Citation:** Zupa et al. (2021) - Accelerometry-based O₂ consumption calibration

**Applications:**

- DO consumption prediction
- Feed requirement estimation
- Stress detection (elevated metabolism)

---

## 7. Stocking & Spatial Configuration Features

**Category:** Literature-driven features - Requires spatial optimization framework  
**Priority:** Medium - Configuration module for platform

### 7.1 Stocking Density

**Category:** Literature-driven feature  
**Citation:** Andika et al. (2024) - Optimal density treatment B (15 fish, 20 prawns, 30 oysters/300m³)

**Planned Features:**

- Current density (kg/m³) by species
- Density-dependent growth correction factors
- Survival rate modifiers at high density
- DO consumption scaling

### 7.2 Proximity Index

**Category:** Literature-driven feature  
**Citation:** Kerrigan et al. (2016) - Meta-analysis showing extractive species growth best within close proximity

**Formula:**

Distance-weighted nutrient capture efficiency. Closer mussel/kelp lines to fish cages = higher N/P uptake.

**Implementation:**

- GIS-based spatial analysis
- Plume dispersion modeling
- Optimization algorithm for cage/line placement

---

## 8. Economic & Operational Features

**Category:** Core features - Business intelligence module  
**Priority:** Medium - User adoption driver

### 8.1 Feed Cost Efficiency

**Formula:**

```text
FCE = Revenue_per_kg / (Feed_cost_per_kg × FCR)
```

### 8.2 Harvest Timing Optimizer

**Category:** Literature-driven feature  
**Citations:** Carras et al. (2019), Knowler et al. (2020) - Economic optimization frameworks

Optimal harvest size balancing growth rate vs market price vs carrying costs.

### 8.3 Species Diversification Index

**Formula:**

```text
SDI = -Σ(p_i × ln(p_i))
```

Where p_i is revenue proportion from species i. Higher SDI = lower economic risk.

---

## 9. Alert & Anomaly Detection Features

**Category:** Core features with literature-driven components  
**Priority:** Critical - User safety and system value proposition

### 9.1 Multi-Parameter Alert Scores

**Category:** Literature-driven feature  
**Citation:** Chatziantoniou et al. (2023) - Aquasafe compound indicator methodology

Weighted combination of threshold violations:

- DO < 5.5 mg/L (weight: 5)
- Temperature > species optimum (weight: 3)
- Chlorophyll-a spike (HAB risk) (weight: 4)

### 9.2 Anomaly Scores

**Methods:**

- Isolation Forest for multivariate outliers
- LSTM autoencoder reconstruction error
- Statistical process control (3-sigma rules)

**Applications:**

- Sensor malfunction detection
- Unusual environmental events
- Disease outbreak early warning

---

## 10. Climate & Weather Features

**Category:** Literature-driven features - Long-term planning module  
**Priority:** Low - Phase 2 implementation

### 10.1 Growing Degree Days (GDD)

**Category:** Literature-driven feature  
**Citation:** Stavrakidis-Zachou et al. (2021) - Climate projection methodology

Accumulated thermal units for biological processes.

### 10.2 Storm Risk Indices

**Category:** Literature-driven feature  
**Citation:** Buck et al. (2018) - Offshore IMTA infrastructure challenges

**Planned Features:**

- Wave height forecasts (from numerical models)
- Wind stress on infrastructure
- Storm surge risk
- Operational weather windows

---

## 11. Satellite-Derived Features

**Category:** Literature-driven features - Remote sensing integration  
**Priority:** High - Cost-effective monitoring at scale

### 11.1 Sea Surface Temperature (SST)

**Category:** Literature-driven feature  
**Citations:** Chatziantoniou et al. (2022, 2023) - Sentinel-3 SLSTR integration

**Applications:**

- 24-72 hour temperature forecasting for alert system
- Spatial thermal habitat mapping
- Validation of in-situ sensors

### 11.2 Ocean Color Products

**Category:** Literature-driven feature  
**Citation:** Chatziantoniou et al. (2022, 2023) - Sentinel-2/3 ocean color processing

**Features:**

- Chlorophyll-a concentration
- Turbidity / suspended sediment
- CDOM (colored dissolved organic matter)

### 11.3 Spatial Context Features

**Derived from GIS analysis:**

- Distance to shore
- Bathymetry (depth profile)
- Exposure index (fetch, wind)
- Proximity to other farms (disease risk)

---

## 12. Data Quality & Metadata Features

**Category:** Implemented features  
**Priority:** Critical - Foundation for reliable analytics

### 12.1 Sensor Health Indicators

**Implementation Status:** Currently implemented in `imta_analytics/data/streaming.py`

**Existing Quality Control Logic:**

- Cascading identical value detection (sensor freeze)
- Physical bounds validation
- Missing data percentage
- Timestamp gap detection

### 12.2 Data Provenance

**Planned Features:**

- Source tracking (satellite vs in-situ vs model)
- Processing lineage (raw → cleaned → derived)
- Uncertainty quantification
- Version control for datasets

---

## Feature Implementation Priority Matrix

| Priority | Count | Features |
|----------|-------|----------|
| **Critical** | 5 | DEB models, DO prediction (CNN-SA-BiSRU), alert system, sensor QC, conductivity |
| **High** | 10 | Density, stratification, currents, chlorophyll-a, time features, satellite SST, temporal lags, CNN features, self-attention |
| **Medium** | 6 | Tidal phase, pH variability, residence time, economics, spatial config |
| **Low** | 3 | Climate projections, storm risk, advanced spatial |

**Total Features:** 24 implemented/planned, 18+ literature-driven placeholders

---

## 13. Deep Learning Feature Engineering

**Category:** Literature-driven features - Advanced ML implementation  
**Priority:** High - State-of-the-art DO prediction  
**Citation:** Xu et al. (2025) - CNN-SA-BiSRU architecture

### 13.1 CNN-Extracted Features

**Category:** Literature-driven feature  
**Purpose:** Automated feature extraction from multivariate time series

**Implementation:**

- **1D Convolution**: Extract local patterns from DO, pH, conductivity, temperature
- **Kernel size optimization**: Test 3, 5, 7 timestep windows
- **Feature maps**: 32-128 filters for different temporal patterns
- **Activation**: Tanh (as per Xu et al.) or ReLU

**Benefits:**

- Reduces data redundancy
- Discovers non-obvious parameter interactions
- Lower computational complexity vs manual feature engineering

### 13.2 Self-Attention Weighted Features

**Category:** Literature-driven feature  
**Purpose:** Dynamic feature importance weighting

**Formula (from Xu et al.):**

```text
Attention(Q, K, V) = softmax(QK^T / √d_k) * V
```

**Applications:**

- Emphasizes critical water quality parameters during hypoxic events
- Ignores less relevant features automatically
- Improves prediction accuracy by 15-20% over baseline BiSRU

### 13.3 Bidirectional Temporal Context

**Category:** Literature-driven feature  
**Citation:** Xu et al. (2025) - BiSRU (Bidirectional Simple Recurrent Unit)

**Features:**

- **Forward context**: Past observations → current prediction
- **Backward context**: Future observations → current prediction (training only)
- **Parallel computation**: Unlike LSTM/GRU, enables faster training

**Use Cases:**

- Real-time DO prediction (10-minute ahead)
- Anomaly detection (deviation from bidirectional expectations)
- Missing data imputation (interpolation using past + future context)

---

## Next Steps & Roadmap

### Immediate (Week 1-2)

- [ ] Complete Tier 1 literature review (Chambers, Chatziantoniou, Føre, Venolia)
- [ ] Extract quantitative parameters for DEB models
- [ ] Validate feature list against UNH Aquafort operational needs
- [ ] Prioritize features for MVP implementation

### Short-Term (Month 1-2)

- [ ] Implement basic water quality derivatives (DO saturation, density, conductivity features)
- [ ] Build time-based feature encoders (diurnal, seasonal, high-frequency temporal lags)
- [ ] Integrate ADCP current data for hydrodynamics features
- [ ] Prototype DEB-based kelp growth model
- [ ] Implement CNN feature extraction pipeline (Xu et al. architecture)
- [ ] Test self-attention mechanism for DO prediction

### Medium-Term (Month 3-6)

- [ ] Deploy satellite data pipeline (Sentinel-2/3)
- [ ] Implement alert scoring system
- [ ] Build stocking density optimization module
- [ ] Validate all features against UNH Aquafort ground truth

### Long-Term (Month 6-12)

- [ ] Climate adaptation features
- [ ] Advanced spatial optimization
- [ ] Economic forecasting module
- [ ] Multi-farm comparative analytics

---

## Literature Cross-Reference

Features mapped to source papers from literature review:

**Chatziantoniou et al. (2023) - Aquasafe Platform:** [DOI: 10.3390/app13106122](https://doi.org/10.3390/app13106122)

- Alert scoring methodology
- Satellite SST integration
- User interface design patterns

**Venolia et al. (2020) - Kelp DEB Model:** [DOI: 10.1016/j.ecolmodel.2020.109151](https://doi.org/10.1016/j.ecolmodel.2020.109151)

- Kelp growth rate equations
- Temperature correction factors
- Nutrient uptake kinetics

**Stavrakidis-Zachou et al. (2019) - Fish DEB:** [DOI: 10.1016/j.seares.2018.05.008](https://doi.org/10.1016/j.seares.2018.05.008)

- DEB parameter estimation
- FCR modeling
- Metabolic scaling

**Chatziantoniou et al. (2022) - DO Prediction:** [DOI: 10.1016/j.rsase.2022.100865](https://doi.org/10.1016/j.rsase.2022.100865)

- ML feature engineering (temporal lags, spatial averages)
- Model performance benchmarks (R² = 0.67)
- Sentinel-3/2 data integration

**Barzegar et al. (2020) - CNN-LSTM Hybrid:** [DOI: 10.1007/s00477-020-01776-2](https://doi.org/10.1007/s00477-020-01776-2)

- Time-series feature extraction
- Model architecture patterns

**Xu et al. (2025) - CNN-SA-BiSRU Hybrid:** [DOI: 10.1038/s41598-025-10786-5](https://doi.org/10.1038/s41598-025-10786-5)

- Conductivity as DO predictor (R²=0.9765 model)
- High-frequency temporal features (10-min intervals)
- CNN 1D convolution for automated feature extraction
- Self-attention mechanism for dynamic feature weighting
- BiSRU bidirectional temporal context
- Real-time prediction capability (MAE=0.034 mg/L)

**Andika et al. (2024) - Stocking Density:** [DOI: 10.29103/joms.v1i1.15628](https://doi.org/10.29103/joms.v1i1.15628)

- Optimal density treatments
- Multi-species interactions
- Survival rate relationships

**Kerrigan et al. (2016) - Spatial Configuration:** [DOI: 10.1111/raq.12186](https://doi.org/10.1111/raq.12186)

- Proximity effects
- Nutrient capture efficiency
- Optimal distances
