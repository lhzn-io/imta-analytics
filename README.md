# IMTA Analytics

![Aquafort IMTA System](assets/aquafort.jpg)

## Data Science & AI Tools for Sustainable Integrated Multi-Trophic Aquaculture

A research and development platform for predictive yield modeling, intelligent decision support systems, and precision farming technologies for IMTA operations. Developed in partnership with UNH Aquafort.

---

## Mission

Bridge the gap between cutting-edge aquaculture research and practical farm operations by developing AI-powered tools that:

- **Predict** biomass yields based on environmental factors (in development)
- **Monitor** water quality parameters using satellite and IoT sensor fusion (planned)
- **Optimize** multi-species stocking densities and harvest timing (planned)
- **Assist** operators with intelligent decision support and troubleshooting (planned)
- **Validate** IMTA's environmental benefits through data analysis

---

## Core Projects

### 1. Predictive Yield Modeling (In Development)

Machine learning models to forecast harvest weights for multi-species IMTA systems based on:

- **Environmental Parameters**: Temperature, dissolved oxygen, chlorophyll-a, salinity
- **Operational Factors**: Stocking density, feeding regimes, biomass loading
- **Species-Specific Growth**: Dynamic Energy Budget (DEB) models coupled with data-driven ML

**Target Performance**: R² > 0.90, MAPE < 10% (benchmark: published systems achieve R² = 0.98 - Xu et al., 2025)

**Planned Technologies**:

- Random Forest, XGBoost, LSTM neural networks
- Physics-informed neural networks (hybrid mechanistic-ML approach)
- Sentinel-2/3 satellite imagery + in-situ sensor integration

### 2. IMTA Operator Co-Pilot (AI Assistant) (Planned)

Conversational AI system to provide decision support, training, and troubleshooting:

- **Natural Language Interface**: Ask questions like "Why is my kelp growth slow?" or "Should I harvest early?"
- **Proactive Alerts**: Predictive anomaly detection (24-48 hour advance warnings)
- **Scenario Simulation**: "What if I increase stocking by 20%?" → model-based forecasting
- **Knowledge Base**: Integrated access to 50+ research papers, SOPs, and regulatory guidelines

**Planned Technologies**:

- Retrieval-Augmented Generation (RAG) with GPT-4/Claude
- Knowledge graphs (Neo4j) for structured aquaculture domain knowledge
- Function calling to query databases, run models, access sensor APIs

### 3. Multi-Source Data Integration Pipeline (In Development)

Automated data collection, harmonization, and quality control from:

- **Satellite Remote Sensing**: Sentinel-2 MSI (10m), Sentinel-3 OLCI/SLSTR (300m-1km)
- **Biogeochemical Models**: CMEMS numerical forecasts
- **IoT Sensor Networks**: DO, temperature, pH, salinity (Campbell Scientific dataloggers, YSI EXO2)
- **Farm Records**: Growth measurements, feeding logs, harvest data

**Current Implementation**:

- TOA5 data loader for Campbell Scientific dataloggers
- Data quality control for marine sensor data
- PostgreSQL database schema (planned)
- TimescaleDB for time-series optimization (planned)

---

## Research Focus Areas

**Current Phase:** Literature review and exploratory data analysis. Focus areas below represent planned research directions informed by published literature and UNH Aquafort case study.

### Environmental Monitoring & Prediction (Planned)

- **Dissolved Oxygen Forecasting**: Target R² > 0.90 (benchmark: published R² = 0.98 - Xu et al., 2025)
- **Hypoxia Early Warning**: Detection of critical events (DO < 5.5 mg/L) 24-48 hours in advance
- **Temperature-DO Interaction Modeling**: Capturing synergistic effects

### Growth & Yield Optimization (Planned)

- **Multi-Species Growth Models**: Finfish (DEB-based), bivalves, seaweeds
- **Feed Conversion Efficiency**: Dynamic FCR prediction based on environmental conditions
- **Harvest Window Optimization**: Align species cycles, maximize market price capture

### Species Interaction & Nutrient Cycling (Planned)

- **Bioremediation Quantification**: N/P removal by extractive species
- **Trophic Transfer Modeling**: Fish effluent → mussel/kelp uptake pathways
- **Carrying Capacity Assessment**: Optimize ratios based on site characteristics

### Economic Analysis & Market Intelligence (Planned)

- **Net Present Value (NPV) Modeling**: IMTA vs. monoculture profitability
- **Risk-Adjusted Returns**: Product diversification benefits
- **Price Premium Analysis**: Consumer willingness-to-pay for sustainable products

---

## Repository Structure

```text
imta-analytics/
├── imta_analytics/         # Python package (pip install -e .)
│   ├── __init__.py        # Package initialization, version info
│   ├── data/              # Data loading and parsing
│   │   ├── __init__.py
│   │   └── loaders.py     # TOA5 and other format loaders
│   ├── quality/           # Data quality checks (future)
│   ├── analysis/          # Analysis functions (future)
│   └── web/               # Web application components (future)
├── notebooks/              # Jupyter notebooks for exploratory analysis
│   ├── 01_initial_data_exploration.ipynb
│   ├── 02_growth_modeling/ (future)
│   ├── 03_environmental_prediction/ (future)
│   └── 04_economic_analysis/ (future)
├── data/                   # Data directory (not tracked in git)
│   ├── aquafort-buoy-station/  # UNH Aquafort TOA5 files
│   ├── raw/               # Other original datasets
│   ├── processed/         # Cleaned, feature-engineered data
│   └── external/          # Satellite imagery, CMEMS downloads
├── models/                 # Trained model artifacts (.pkl, .h5)
├── refs/                   # Reference materials
│   ├── Literature Review - Data Science & AI Applications.md
│   ├── publications/      # 50+ research papers (PDFs + markdown)
│   └── technical/         # Instrument manuals (CR1000X, EXO2, etc.)
├── docs/                   # Documentation
│   ├── data-format-analysis.md  # TOA5 format documentation
│   ├── planning/          # System design documents
│   └── model_cards/       # Model documentation (future)
├── tests/                  # Unit and integration tests (future)
├── setup.py               # Package installation configuration
├── Makefile               # Build automation (PDF→markdown conversion)
├── environment.yml         # Conda environment specification
└── README.md
```

---

## Tech Stack

### Data Science & ML

- **Core**: Python 3.10+, NumPy, Pandas, Scikit-learn
- **Deep Learning**: PyTorch, TensorFlow/Keras
- **Time Series**: statsmodels, Prophet, LSTM/GRU networks
- **Optimization**: SciPy, Optuna (hyperparameter tuning), DEAP (genetic algorithms)

### Geospatial & Remote Sensing

- **Processing**: GDAL, Rasterio, Sentinelsat, Google Earth Engine API
- **Analysis**: GeoPandas, Shapely, Folium (interactive maps)
- **Database**: PostGIS (spatial extensions for PostgreSQL)

### AI & NLP

- **LLMs**: OpenAI API, Anthropic Claude, LangChain
- **Vector DB**: Chroma, Pinecone (semantic search)
- **Knowledge Graphs**: Neo4j, RDFlib

### Web & APIs

- **Backend**: FastAPI, Flask
- **Frontend**: React, Plotly Dash (dashboards)
- **Database**: PostgreSQL, TimescaleDB

### DevOps

- **Containerization**: Docker, docker-compose
- **Orchestration**: Kubernetes (production), Airflow (data pipelines)
- **Monitoring**: Prometheus, Grafana
- **Version Control**: Git, DVC (data version control)

---

## Getting Started

### Prerequisites

#### Current Development Environment

- **Python**: 3.10 or higher
- **Conda**: For environment management (recommended)

#### Planned Infrastructure

- **Database**: PostgreSQL 14+ with PostGIS and TimescaleDB extensions
- **Optional**: Docker (for containerized deployment)
- **API Keys** (for future features):
  - Copernicus Data Space (Sentinel satellite imagery)
  - OpenAI or Anthropic (for AI assistant)
  - OpenWeatherMap (meteorological data)

### Installation

**Current Status:** Basic Python environment and data loading capabilities implemented. Full installation workflow in development.

#### 1. Clone Repository

```bash
git clone https://github.com/lhzn-io/imta-analytics.git
cd imta-analytics
```

#### 2. Set Up Python Environment

Using Conda (Recommended):

```bash
conda env create -f environment.yml
conda activate imta-analytics
```

#### 3. Install Package

```bash
pip install -e .
```

**Note:** Database setup, API configuration, and additional installation steps forthcoming.

### Quick Start: Load TOA5 Data

```python
from imta_analytics.data import load_toa5_file
from imta_analytics.data.loaders import apply_marine_quality_filters

# Load Campbell Scientific TOA5 format data
df, metadata, units = load_toa5_file('data/aquafort-buoy-station/UNH-G2000B_EXO2SumData.dat')

print(f"Station: {metadata['station']}")
print(f"Logger: {metadata['logger_model']}")
print(f"Data shape: {df.shape}")

# Apply data quality filters (remove sensor errors)
df_clean = apply_marine_quality_filters(df)
print(f"Removed {len(df) - len(df_clean)} invalid records")
```

**Note:** Additional quick start examples forthcoming as features are implemented.

---

## Key Results & Validation

**Note:** Results below are from published literature (citations in [Literature Review](refs/Literature%20Review%20-%20Data%20Science%20%26%20AI%20Applications%20in%20Sustainable%20Aquaculture%20Systems.md)). This project aims to validate and extend these findings for New England IMTA systems.

### Dissolved Oxygen Prediction (Published Benchmarks)

- **R² = 0.98** on validation set - Xu et al. (2025), intensive aquaculture China
- **MAE = 0.034 mg/L** - state-of-the-art precision (10x improvement over Chatziantoniou 2022)
- Hybrid CNN-SA-BiSRU architecture using 10-minute IoT sensor data (3,500 measurements)

### Growth Modeling (Published Benchmarks)

- **RMSE = 6.92%** for plant biomass estimation (computer vision)
- Kelp growth rate modeling: 0.77 cm/day (winter) → 3.52 cm/day (spring) - Venolia et al. (2020)

### Economic Validation (Published Literature)

- IMTA systems demonstrate **24-174% revenue increase** vs. monoculture - Knowler et al. (2020)
- **B/C ratio 1.1-1.7** in suitable sites
- **10-36% price premium** for eco-certified IMTA products

### Environmental Benefits (Chambers et al. 2024 - UNH Aquafort)

- **16.4 kg net nitrogen reduction** per production cycle (validated at commercial scale)
- **416 kg steelhead trout, 3,072 kg mussels, 638 kg kelp** produced in trial period
- Demonstrated feasibility of multi-species offshore system

---

## Research Gaps & Opportunities

1. **Seaweed Yield Modeling**: No published ML models exist (high variability, labor-intensive measurement)
2. **Integrated Multi-Species Models**: Current models treat species independently; need coupled nutrient transfer
3. **Causal Inference**: Move beyond correlation → enable "what-if" scenario testing with confidence
4. **Edge AI Deployment**: Reduce latency from 12-48 hours (cloud) to 1-3 hours (on-farm processing)
5. **Explainable AI**: Integrate SHAP/LIME for farmer trust and adoption
6. **Public Datasets**: Establish IMTA Data Commons for reproducibility

See full analysis in [`refs/Literature Review - Data Science & AI Applications.md`](refs/Literature%20Review%20-%20Data%20Science%20%26%20AI%20Applications%20in%20Sustainable%20Aquaculture%20Systems.md)

---

## Documentation

- **[Feature Engineering](docs/planning/feature-engineering.md)**: Comprehensive catalog of derived parameters and engineered features
- **[Data Format Analysis](docs/analysis/20251104-data-format-analysis.md)**: TOA5 format documentation and sensor data handling
- **Setup Guide** (forthcoming): Detailed installation instructions
- **Data Sources** (forthcoming): How to access Sentinel, CMEMS, sensor data
- **Model Cards** (forthcoming): Performance metrics, limitations, ethical considerations
- **API Reference** (forthcoming): REST endpoints for model serving
- **Contributing Guidelines** (forthcoming): Development workflow, code standards

---

## Contributing

We welcome contributions from researchers, developers, and aquaculture practitioners!

**Priority Areas**:

- Species-specific growth models (mussels, oysters, kelp, sea urchins)
- Sensor data quality control algorithms
- User interface improvements for AI assistant
- Economic optimization models
- Documentation and tutorials

**Workflow**:

1. Fork the repository
2. Create feature branch: `git checkout -b feature/seaweed-yield-model`
3. Commit changes with clear messages
4. Add tests: `pytest tests/`
5. Submit pull request

Contributing guidelines document forthcoming.

---

## License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

**Note**: Research papers in `refs/publications/` retain their original copyrights. Included under fair use for academic research.

---

## Acknowledgments

- **UNH Aquafort**: Farm data, domain expertise, field validation
- **Literature Sources**: 50+ peer-reviewed papers synthesized in this work (see [Literature Review](refs/Literature%20Review%20-%20Data%20Science%20%26%20AI%20Applications%20in%20Sustainable%20Aquaculture%20Systems.md))
- **Open Data Providers**:
  - ESA Copernicus (Sentinel satellite imagery)
  - CMEMS (marine biogeochemical models)
  - NOAA (meteorological data)
- **Open Source Community**: Scikit-learn, PyTorch, LangChain, PostGIS

---

## Contact

### Team

- **Daniel Fry** - Long Horizon Initiative - Catalyzed Partner[^1]
- **David Fredriksson** - [UNH CSSS Director](https://marine.unh.edu/person/david-fredriksson)
- **Michael Chambers** - [UNH CSSS Research Associate Professor](https://marine.unh.edu/person/michael-chambers)
- **Longhuan Zhu** - [UNH CEPS Ocean Engineering Research Scientist](https://ceps.unh.edu/person/longhuan-zhu)

[^1]: [NSF TTP](https://www.nsf.gov/funding/opportunities/nsf-ttp-national-science-foundation-translation-practice/nsf25-540/solicitation) (National Science Foundation Translation to Practice) - potential

### Project Resources

- **Issues**: [GitHub Issues](https://github.com/lhzn-io/imta-analytics/issues)
- **Discussions**: [GitHub Discussions](https://github.com/lhzn-io/imta-analytics/discussions)

---

## Why IMTA?

> "The solution to nitrification is not dilution but conversion."  
> — Chopin et al., 2001

Integrated Multi-Trophic Aquaculture represents a fundamental shift toward ecosystem-based food production:

- **Environmental**: Convert waste into harvestable biomass, reduce eutrophication
- **Economic**: Diversify revenue streams, capture premium prices
- **Social**: Align aquaculture with sustainability values, support coastal communities

This project aims to make IMTA commercially viable through data-driven optimization and intelligent automation.
