# Data Sources

**Last Updated**: 2025-11-12

## Overview

This document catalogs data sources for the IMTA Analytics platform, including access methods, update frequencies, spatial/temporal resolution, quality considerations, and integration status. Data flows from multiple sources into the multi-source integration pipeline for harmonization and quality control.

**Infrastructure Provider**: Long Horizon Initiative provides cloud storage infrastructure as catalyzed partner (Google Cloud Storage primary, Azure Blob Storage secondary). Cost estimates reflect operational costs at scale.

See [README.md](../../README.md) for project context and [infrastructure-architecture.md](infrastructure-architecture.md) for processing infrastructure.

---

## In-Situ Sensors (Currently Active)

### UNH Aquafort Buoy Station

**Status**: Primary data source for platform development (2023-2024 baseline data)

**Instrumentation**:

- **Campbell Scientific CR1000X**: Data logger
  - Sample interval: 15 minutes
  - Data format: TOA5 (comma-delimited with metadata headers)
  - Storage: Onboard + manual retrieval
  
- **YSI EXO2 Multi-Parameter Sonde**: Water quality
  - **Parameters**: Dissolved oxygen (% saturation, mg/L), temperature (°C), pH, salinity (PSU), specific conductance (mS/cm), chlorophyll-a (RFU, μg/L), blue-green algae phycocyanin (RFU, μg/L), turbidity (FNU), fluorescent dissolved organic matter (fDOM, QSU)
  - **Depth**: Surface to ~5m (vertical profiling capability)
  - **Accuracy**: DO ±1% saturation, Temp ±0.01°C, pH ±0.1 units, Salinity ±1% or 0.1 PSU
  
- **Z-Cell ADCP**: Acoustic Doppler Current Profiler
  - **Measurements**: 3D current velocity profiles
  - **Vertical bins**: TBD
  - **Range**: TBD

**Data Access**:

- Current: Manual download from datalogger
- Planned: Automated telemetry (cellular/satellite modem)

**Data Quality**:

- Campbell Scientific NaN sentinels: "NAN", 7999, -6999 (see [TOA5 format documentation](analysis/20251104-data-format-analysis.md))
- Behavioral heuristics for sensor failures (cascading identical values, physical impossibilities)
- ~0.5% invalid records detected in 2023-2024 dataset (147 of 27,129 samples)

**Storage Location**: `data/aquafort-buoy-station/`

---

## Satellite Remote Sensing (Under Evaluation)

### Sentinel-2 MSI (Multispectral Instrument)

**Provider**: ESA Copernicus Programme (free and open data)

**Specifications**:

- **Spatial Resolution**: 10m (visible/NIR), 20m (red edge/SWIR), 60m (coastal aerosol)
- **Temporal Resolution**: 5 days (2-satellite constellation)
- **Spectral Bands**: 13 bands (443nm to 2190nm)
- **Swath Width**: 290 km

**IMTA Applications**:

- **Chlorophyll-a estimation**: Red edge bands (705nm, 740nm, 783nm) for coastal/turbid waters
- **Dissolved oxygen estimation**: Derived from SST + chlorophyll-a (ML models, R² ~0.67-0.81 reported in literature)
- **Surface oil detection**: Short-wave infrared bands for fish farm waste monitoring
- **Turbidity/suspended sediment**: Visible bands (490nm, 560nm, 665nm)

**Access Methods**:

- **Sentinelsat Python API**: Automated search and download
- **Google Earth Engine**: Cloud-based processing (no download required)
- **Copernicus Data Space**: Direct access via OpenSearch API

**Processing Requirements**:

- Atmospheric correction (Sen2Cor, ACOLITE for water)
- Cloud masking (QA60 band)
- Geometric correction (already orthorectified)

**Cost**: Free

**Status**: Literature review complete, API testing pending

### Sentinel-3 OLCI/SLSTR

**Provider**: ESA Copernicus Programme (free and open data)

**Specifications**:

- **OLCI (Ocean and Land Color Instrument)**:
  - Spatial Resolution: 300m (full resolution), 1.2km (reduced resolution)
  - Temporal Resolution: <2 days (2-satellite constellation)
  - Spectral Bands: 21 bands (400nm to 1020nm)
  - Swath Width: 1270 km
  
- **SLSTR (Sea and Land Surface Temperature Radiometer)**:
  - Spatial Resolution: 500m (thermal), 1km (nadir)
  - Temporal Resolution: <1 day
  - Spectral Bands: 9 bands (visible to thermal infrared)

**IMTA Applications**:

- **Sea surface temperature (SST)**: Daily coverage, ~0.3°C accuracy
- **Ocean color variables**: Chlorophyll-a, total suspended matter, dissolved organic carbon
- **Thermal stress monitoring**: Temperature anomalies, marine heatwaves

**Access Methods**: Same as Sentinel-2 (Sentinelsat, GEE, Copernicus Data Space)

**Cost**: Free

**Status**: Under evaluation for thermal monitoring

### Sentinel-1 SAR (Synthetic Aperture Radar)

**Provider**: ESA Copernicus Programme (free and open data)

**Specifications**:

- **Spatial Resolution**: 5m (stripmap), 20m (interferometric wide swath), 100m (extra wide swath)
- **Temporal Resolution**: 6-12 days (2-satellite constellation)
- **Frequency**: C-band (5.405 GHz)
- **Polarization**: Dual-pol (VV+VH or HH+HV)

**IMTA Applications**:

- **Surface oil film detection**: Fish farm waste plumes (30m resolution)
- **All-weather monitoring**: Radar penetrates clouds
- **Infrastructure monitoring**: Cage position/deformation detection

**Processing Requirements**:

- Radiometric calibration
- Geometric correction (Range-Doppler terrain correction)
- Speckle filtering

**Cost**: Free

**Status**: Future consideration (requires SAR processing expertise)

### Commercial Satellite Data (Evaluation Pending)

**Providers Under Consideration**:

- **Planet Labs**: PlanetScope (3m daily), SkySat (50cm video)
- **Maxar**: WorldView-3 (31cm), WorldView-4 (31cm)
- **Airbus**: Pléiades Neo (30cm)

**Cost Estimate**: $500-2000/month depending on coverage area and temporal frequency

**Decision Pending**: Cost-benefit analysis vs. Sentinel data quality for IMTA applications

**Status**: No active evaluation yet

---

## Biogeochemical Models (Planned)

### CMEMS (Copernicus Marine Environment Monitoring Service)

**Provider**: EU Copernicus Programme (free registration required)

**Products**:

- **Level-4 SST**: Daily gap-free sea surface temperature (1-4km resolution)
- **Level-4 Chlorophyll-a**: Daily gap-free concentration maps (1-4km resolution)
- **Numerical Forecasts**:
  - Dissolved oxygen (3D fields)
  - Salinity (surface and depth profiles)
  - Ocean currents (u, v, w components)
  - Nutrients (nitrate, phosphate)
  
**Spatial Coverage**: Global and regional models (Northwest Atlantic available)

**Temporal Coverage**: Near-real-time + historical reanalysis

**Access Methods**:

- **MOTU Client**: Python API for automated download
- **OPeNDAP**: Direct data access without full download
- **FTP**: Bulk download of archived data

**Cost**: Free (registration required)

**Status**: Planned for integration, API credentials pending

### US Alternatives (NOAA/IOOS)

**NOAA CoastWatch/OceanWatch**:

- Satellite-derived SST, chlorophyll-a, ocean color products
- 5km resolution for US coastal waters
- Near-real-time and historical data
- ERDDAP server for programmatic access

**NOAA IOOS (Integrated Ocean Observing System)**:

- Regional operational models
- Real-time sensor data aggregation
- Standardized data formats (CF conventions)

**NOAA NOMADS (National Operational Model Archive)**:

- Operational ocean forecast models
- Wave height, currents, temperature, salinity
- High-resolution coastal models (e.g., RTOFS, CBOFS)

**Cost**: Free

**Status**: Alternative to CMEMS for US-specific applications

---

## IoT Sensor Networks (Current + Planned Expansion)

### Current: UNH Aquafort Buoy

See "In-Situ Sensors" section above for specifications.

### Planned Expansion

**Water Quality Sensors**:

- Additional YSI EXO2 sondes at different depths/locations
- Dissolved oxygen profilers (optical sensors)
- pH/pCO2 sensors for carbonate chemistry monitoring

**Environmental Sensors**:

- **ADCP/AWCP**: Acoustic current profilers for 3D velocity fields
- **Wave sensors**: Significant wave height, period, direction
- **Weather stations**: Wind speed/direction, air temperature, barometric pressure
- **Light sensors**: PAR (photosynthetically active radiation) for productivity modeling

**Structural Health Monitoring**:

- **Load cells**: Tension on mooring lines, cage structural loads
- **Position sensors**: GPS/GNSS for cage drift monitoring
- **Tilt sensors**: Cage orientation under current/wave forcing
- **Acoustic tags**: Fish behavior and distribution within cages

**Biofouling Monitoring**:

- **Cameras**: Underwater imaging for biofouling assessment
- **Acoustic sensors**: Passive acoustics for fish behavior

**Integration Challenges**:

- Power management (solar/wind for remote deployments)
- Data telemetry (cellular coverage limited offshore)
- Sensor calibration and drift correction
- Biofouling of optical sensors

**Status**: Architecture planning phase, deployment pending funding

---

## Aquafort Operational Data (Future Integration)

### Growth Measurements

**Current Practice** (manual):

- Length/weight sampling during handling events
- Periodic cage population surveys
- Visual health assessments

**Planned Automation**:

- **Hydroacoustic biomass estimation**: Sonar-based fish counting and sizing
- **Stereo camera systems**: Non-invasive length/weight estimation
- **Computer vision**: Automated growth tracking from video feeds

### Feeding Logs

**Data Sources**:

- Feed delivery timestamps and quantities
- Feed type/formulation changes
- Uneaten feed observations (waste monitoring)

**ML Applications**:

- Feed conversion ratio (FCR) prediction
- Optimal feeding schedule optimization
- Appetite prediction from environmental conditions

### Harvest Data

**Records**:

- Individual fish weights and lengths
- Batch harvest totals (biomass, count)
- Quality grades (market size, health status)
- Processing yields

**ML Applications**:

- Harvest timing optimization
- Market price integration for economic optimization
- Quality prediction models

### Operational Events

**Event Types**:

- Crowding operations
- Delousing treatments (sea lice management)
- Fish transfers between cages
- Mortality events
- Equipment maintenance

**ML Applications**:

- Stress response prediction
- Treatment efficacy modeling
- Operational scheduling optimization

**Integration Challenges**:

- Data standardization (currently paper logs)
- Timestamp synchronization with sensor data
- Data privacy and commercial sensitivity

**Status**: Partnership discussions for data sharing agreements

---

## Machine Learning Outputs (Derived Data Products)

### Predicted Environmental Variables

**Dissolved Oxygen from Satellite Data**:

- **Input Features**: Sentinel-2/3 derived SST, chlorophyll-a, turbidity
- **Model Performance**: R² ~0.67-0.81 (reported in literature for similar systems)
- **Spatial Resolution**: 10-300m (depending on satellite source)
- **Temporal Resolution**: 5-day revisit (Sentinel-2) to daily (CMEMS Level-4)
- **Status**: Literature validation, model training planned

### Growth Forecasts

**DEB Model Outputs**:

- Individual fish growth trajectories (length, weight)
- Temperature-dependent growth rates
- Feeding response predictions
- Energy allocation (somatic growth vs. reproduction)

**Data-Driven ML Models**:

- LSTM/GRU time-series forecasts
- Random Forest/XGBoost for non-linear environmental responses
- Hybrid physics-ML models

**Status**: Under development (see Research Focus Areas in README)

### Behavioral Pattern Analysis

**Stress/Disease Indicators**:

- Anomalous swimming patterns (reduced activity, erratic movement)
- Feeding behavior changes (appetite loss)
- Schooling behavior disruption

**Data Sources**:

- Acoustic telemetry (fish position tracking)
- Underwater video (computer vision analysis)
- Feed intake monitoring (automated feeders)

**Status**: Future research direction

---

## Reference Datasets (For Validation)

### Published IMTA Datasets

**Chambers et al. (2024) - UNH Aquafort**:

- Nitrogen cycling measurements (2023 production cycle)
- Multi-species production data (steelhead, mussels, kelp)
- Dataset availability: Contact authors for research use

**Other Published Datasets**:

- Search in progress for public IMTA datasets
- Most published research uses proprietary farm data

### Benchmark Datasets from Literature

**Environmental Prediction Benchmarks**:

- Xu et al. (2025): DO prediction for intensive aquaculture (China, 3,500 measurements)
- Chatziantoniou et al. (2022): Mediterranean fish farm environmental monitoring

**Growth Modeling Benchmarks**:

- Stavrakidis-Zachou et al. (2021): DEB models for Mediterranean finfish
- Venolia et al. (2020): Kelp growth rate seasonality

**Status**: Literature review complete, dataset acquisition in progress where available

---

## Data Integration Architecture

### Harmonization Requirements

**Temporal Alignment**:

- Resample to common time intervals (15-min, hourly, daily)
- Handle irregular sampling (satellite cloud gaps)
- Interpolation methods for missing data

**Spatial Alignment**:

- Reproject satellite data to common CRS (e.g., WGS84 / EPSG:4326)
- Buffer zones around aquaculture sites (100m, 500m, 1km)
- Depth standardization for 3D data (ADCP, models)

**Quality Control Pipeline**:

- Automated flagging of sensor errors (behavioral heuristics)
- Outlier detection (statistical + domain knowledge)
- Data provenance tracking (source, processing history)

**Storage Strategy**:

- Raw data: Preserve original formats (TOA5, NetCDF, GeoTIFF)
- Processed data: Feather/Parquet for fast loading
- Metadata: JSON sidecar files with processing history

**Status**: Architecture designed, implementation in progress (TOA5 loader complete)

### Data Sharing and Version Control

**Current Practice**:

- UNH Aquafort sensor data shared via email (manual transfer)
- Data files stored locally in `data/` directory (not tracked in git)
- `.gitignore` prevents accidental commit of large data files

**Challenges**:

- No automated data delivery from sensor platforms
- Manual synchronization between collaborators
- Difficult to track which version of data was used for specific analyses
- Risk of data loss if only one person has latest files

**Planned Improvements**:

1. **Cloud Storage with Access Control**
   - **Google Cloud Storage (GCS) bucket**: Primary storage backend
     - IAM policies for UNH.edu account access
     - Versioning enabled to track data updates
     - Cost: ~$1-5/month for initial dataset sizes
   - **Alternative**: Azure Blob Storage (if GCP limitations arise)
   
2. **Data Version Control (DVC)**
   - **Tool**: DVC (Data Version Control) - Git-like versioning for datasets
   - **Backend**: GCS (primary) or Azure Blob Storage (fallback)
   - **Benefits**:
     - Track exact data versions used for each analysis
     - Lightweight git commits (metadata only, not raw data)
     - Reproducibility: `dvc pull` fetches correct data version
     - Collaboration: Share data updates via `dvc push`
   - **Example workflow**:
   
     ```bash
     # Track data file with DVC
     dvc add data/aquafort-buoy-station/UNH-G2000B_EXO2SumData.dat
     git add data/aquafort-buoy-station/.gitignore \
             data/aquafort-buoy-station/UNH-G2000B_EXO2SumData.dat.dvc
     git commit -m "Track EXO2 data with DVC"
     
     # Push data to cloud storage
     dvc push
     
     # Collaborator fetches data
     git pull
     dvc pull
     ```
   
   - **Cost**: ~$1-5/month for GCS storage
   - **Status**: Under consideration for multi-collaborator phase
   
3. **Automated Data Telemetry** (Future)
   - Cellular/satellite modem on buoy for real-time data transmission
   - Direct upload to cloud storage (GCS bucket)
   - Eliminates manual transfer requirement
   - Cost: ~$50-200/month for cellular data plan + hardware ($500-1000)
   - Status: Hardware evaluation pending

**Decision Criteria**:

- **Phase 1 (Current)**: Email sharing sufficient for 1-2 collaborators
- **Phase 2 (Expanding team)**: GCS bucket + manual uploads when 3+ collaborators need access
- **Phase 3 (Production)**: DVC + automated telemetry for operational system

---

## Cost Summary

| Data Source | Cost | Status |
|-------------|------|--------|
| UNH Aquafort Buoy | Included (partnership) | Active |
| Sentinel-1/2/3 | Free | Evaluation |
| CMEMS | Free (registration) | Planned |
| NOAA IOOS/CoastWatch | Free | Planned |
| Commercial Satellite | $500-2000/month | Evaluation pending |
| Additional Sensors | $10k-50k (hardware) | Funding pending |

**Total Current Cost**: $0 (partnership + open data)

**Projected Cost with Commercial Data**: $500-2000/month + sensor hardware investment

---

## Related Documentation

- [README.md](../../README.md) - Project overview
- [infrastructure-architecture.md](infrastructure-architecture.md) - Processing infrastructure and tools
- [predictive-features-catalog.md](predictive-features-catalog.md) - Derived features and transformations
- [analysis/20251104-data-format-analysis.md](../analysis/20251104-data-format-analysis.md) - TOA5 format specification
