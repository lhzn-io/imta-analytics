# IMTA Analytics

![Aquafort IMTA System](assets/aquafort.jpg)

**Data Science & AI Tools for Sustainable Integrated Multi-Trophic Aquaculture**

A research and development platform for predictive yield modeling, intelligent decision support systems, and precision farming technologies for IMTA operations. Developed in partnership with UNH Aquafort.

---

## 🎯 Mission

Bridge the gap between cutting-edge aquaculture research and practical farm operations by developing AI-powered tools that:

- **Predict** biomass yields 30-90 days in advance based on environmental factors
- **Monitor** water quality parameters in real-time using satellite + IoT sensor fusion
- **Optimize** multi-species stocking densities and harvest timing
- **Assist** operators with intelligent decision support and troubleshooting
- **Validate** IMTA's environmental benefits (nitrogen reduction, carbon sequestration)

---

## 🚀 Core Projects

### 1. Predictive Yield Modeling

Machine learning models that forecast harvest weights for multi-species IMTA systems based on:

- **Environmental Parameters**: Temperature, dissolved oxygen, chlorophyll-a, salinity
- **Operational Factors**: Stocking density, feeding regimes, biomass loading
- **Species-Specific Growth**: Dynamic Energy Budget (DEB) models coupled with data-driven ML

**Target Performance**: R² > 0.75, MAPE < 15% (benchmark: existing systems achieve R² = 0.67)

**Key Technologies**:
- Random Forest, XGBoost, LSTM neural networks
- Physics-informed neural networks (hybrid mechanistic-ML approach)
- Sentinel-2/3 satellite imagery + in-situ sensor integration

### 2. IMTA Operator Co-Pilot (AI Assistant)

Conversational AI system providing real-time decision support, training, and troubleshooting:

- **Natural Language Interface**: Ask questions like "Why is my kelp growth slow?" or "Should I harvest early?"
- **Proactive Alerts**: Predictive anomaly detection (24-48 hour advance warnings)
- **Scenario Simulation**: "What if I increase stocking by 20%?" → model-based forecasting
- **Knowledge Base**: Integrated access to 50+ research papers, SOPs, and regulatory guidelines

**Key Technologies**:
- Retrieval-Augmented Generation (RAG) with GPT-4/Claude-3
- Knowledge graphs (Neo4j) for structured aquaculture domain knowledge
- Function calling to query databases, run models, access sensor APIs

### 3. Multi-Source Data Integration Pipeline

Automated data collection, harmonization, and quality control from:

- **Satellite Remote Sensing**: Sentinel-2 MSI (10m), Sentinel-3 OLCI/SLSTR (300m-1km)
- **Biogeochemical Models**: CMEMS numerical forecasts
- **IoT Sensor Networks**: DO, temperature, pH, salinity (Arduino/ESP32, Raspberry Pi)
- **Farm Records**: Growth measurements, feeding logs, harvest data

**Key Technologies**:
- PostgreSQL + TimescaleDB (time-series optimization)
- PostGIS (spatial data)
- Spatiotemporal kriging for gap-filling (cloud coverage, sensor failures)
- Edge computing (NVIDIA Jetson) for on-farm processing

---

## 📊 Research Focus Areas

### Environmental Monitoring & Prediction

- **Dissolved Oxygen Forecasting**: SVR models (R² = 0.67, MAE = 0.33 mg/L)
- **Hypoxia Early Warning**: Detection of critical events (DO < 5.5 mg/L) 24-48 hours in advance
- **Temperature-DO Interaction Modeling**: Capturing synergistic effects (r = -0.85 correlation)

### Growth & Yield Optimization

- **Multi-Species Growth Models**: Finfish (DEB-based), bivalves, seaweeds
- **Feed Conversion Efficiency**: Dynamic FCR prediction based on environmental conditions
- **Harvest Window Optimization**: Align species cycles, maximize market price capture

### Species Interaction & Nutrient Cycling

- **Bioremediation Quantification**: N/P removal by extractive species
- **Trophic Transfer Modeling**: Fish effluent → mussel/kelp uptake pathways
- **Carrying Capacity Assessment**: Optimize ratios (e.g., 15 fish : 20 prawns : 30 oysters)

### Economic Analysis & Market Intelligence

- **Net Present Value (NPV) Modeling**: IMTA vs. monoculture profitability
- **Risk-Adjusted Returns**: Product diversification benefits
- **Price Premium Analysis**: Consumer willingness-to-pay for sustainable products (10-36% documented)

---

## 🗂️ Repository Structure

```text
imta-analytics/
├── notebooks/              # Jupyter notebooks for exploratory analysis
│   ├── 01_data_exploration/
│   ├── 02_growth_modeling/
│   ├── 03_environmental_prediction/
│   └── 04_economic_analysis/
├── src/                    # Production-ready code
│   ├── data/              # ETL pipelines, data loaders
│   ├── models/            # ML model implementations
│   │   ├── growth/        # DEB models, yield predictors
│   │   ├── environment/   # DO, temperature, chl-a forecasting
│   │   └── optimization/  # Multi-objective optimization
│   ├── api/               # REST APIs for model serving
│   ├── copilot/           # AI assistant (RAG, knowledge graphs)
│   └── utils/             # Shared utilities, config
├── data/                   # Data directory (not tracked in git)
│   ├── raw/               # Original datasets
│   ├── processed/         # Cleaned, feature-engineered data
│   └── external/          # Satellite imagery, CMEMS downloads
├── models/                 # Trained model artifacts (.pkl, .h5)
├── refs/                   # Reference materials
│   ├── Literature Review - Data Science & AI Applications.md
│   └── publications/      # 50+ research papers (PDFs, markdown notes)
├── docs/                   # Documentation
│   ├── setup.md           # Installation guide
│   ├── data_sources.md    # How to access satellite/sensor data
│   └── model_cards/       # Model documentation (performance, limitations)
├── tests/                  # Unit and integration tests
├── docker/                 # Containerization (Docker, docker-compose)
├── .github/workflows/      # CI/CD pipelines
├── requirements.txt        # Python dependencies
├── environment.yml         # Conda environment (alternative)
└── README.md
```

---

## 🛠️ Tech Stack

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

## 🚦 Getting Started

### Prerequisites

- **Python**: 3.10 or higher
- **Database**: PostgreSQL 14+ with PostGIS and TimescaleDB extensions
- **Optional**: Docker (for containerized deployment)
- **API Keys**: 
  - Copernicus Data Space (Sentinel satellite imagery)
  - OpenAI or Anthropic (for AI assistant)
  - OpenWeatherMap (meteorological data)

### Installation

#### 1. Clone Repository

```bash
git clone https://github.com/lhzn-io/imta-analytics.git
cd imta-analytics
```

#### 2. Set Up Python Environment

**Option A: Conda (Recommended for geospatial work)**

```bash
conda env create -f environment.yml
conda activate imta-analytics
```

**Option B: venv + pip**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### 3. Configure Database

```bash
# Install PostgreSQL + extensions (Ubuntu/Debian example)
sudo apt-get install postgresql-14 postgresql-14-postgis-3 postgresql-14-timescaledb

# Create database
sudo -u postgres psql -c "CREATE DATABASE imta_data;"
sudo -u postgres psql -d imta_data -c "CREATE EXTENSION postgis;"
sudo -u postgres psql -d imta_data -c "CREATE EXTENSION timescaledb;"

# Initialize schema
psql -d imta_data -f src/data/schema.sql
```

#### 4. Set Environment Variables

```bash
cp .env.example .env
# Edit .env with your API keys and database credentials
```

Example `.env`:
```bash
DATABASE_URL=postgresql://user:password@localhost:5432/imta_data
OPENAI_API_KEY=sk-...
COPERNICUS_USERNAME=your_email
COPERNICUS_PASSWORD=your_password
```

#### 5. Download Sample Data

```bash
# Download preprocessed test dataset (1GB)
python scripts/download_sample_data.py

# Or set up data pipelines to fetch from sources
python scripts/setup_data_sources.py
```

### Quick Start: Run Yield Prediction

```python
from src.models.growth import YieldPredictor

# Load trained model
predictor = YieldPredictor.load('models/yield_rf_v1.pkl')

# Make prediction
forecast = predictor.predict(
    species='steelhead_trout',
    current_weight_kg=2.5,
    stocking_date='2024-04-15',
    temperature_celsius=18.5,
    do_mg_per_l=6.8,
    feeding_rate_pct=2.3,
    forecast_days=60
)

print(f"Predicted harvest weight: {forecast.mean:.2f} kg ± {forecast.std:.2f}")
```

### Quick Start: Launch AI Assistant (Local)

```bash
# Start backend API
uvicorn src.api.main:app --reload

# In another terminal, start frontend
cd src/copilot/frontend
npm install && npm start

# Open browser: http://localhost:3000
```

---

## 📈 Key Results & Validation

### Dissolved Oxygen Prediction
- **R² = 0.67** on validation set (Mediterranean aquaculture sites)
- **MAE = 0.33 mg/L** (clinically meaningful accuracy)
- Successfully detected 100% of hypoxic events (DO < 4.7 mg/L) in test period

### Growth Modeling
- **RMSE = 6.92%** for plant biomass estimation (computer vision)
- Accurately captured latitudinal growth differences across 3 Greek sites
- Kelp growth rate modeling: 0.77 cm/day (winter) → 3.52 cm/day (spring)

### Economic Validation
- IMTA systems demonstrate **24-174% revenue increase** vs. monoculture (product diversification)
- **B/C ratio 1.1-1.7** in suitable sites
- **10-36% price premium** for eco-certified IMTA products (consumer surveys)

### Environmental Benefits
- **16.4 kg net nitrogen reduction** per production cycle (validated at commercial scale)
- **38-180 kg N/ha** annual kelp uptake
- **1,100-1,800 kg C/ha** carbon sequestration

---

## 🔬 Research Gaps & Opportunities

1. **Seaweed Yield Modeling**: No published ML models exist (high variability, labor-intensive measurement)
2. **Integrated Multi-Species Models**: Current models treat species independently; need coupled nutrient transfer
3. **Causal Inference**: Move beyond correlation → enable "what-if" scenario testing with confidence
4. **Edge AI Deployment**: Reduce latency from 12-48 hours (cloud) to 1-3 hours (on-farm processing)
5. **Explainable AI**: Integrate SHAP/LIME for farmer trust and adoption
6. **Public Datasets**: Establish IMTA Data Commons for reproducibility

See full analysis in [`refs/Literature Review - Data Science & AI Applications.md`](refs/Literature%20Review%20-%20Data%20Science%20%26%20AI%20Applications%20in%20Sustainable%20Aquaculture%20Systems.md)

---

## 📚 Documentation

- **[Setup Guide](docs/setup.md)**: Detailed installation instructions
- **[Data Sources](docs/data_sources.md)**: How to access Sentinel, CMEMS, sensor data
- **[Model Cards](docs/model_cards/)**: Performance metrics, limitations, ethical considerations
- **[API Reference](docs/api.md)**: REST endpoints for model serving
- **[Contributing](CONTRIBUTING.md)**: Development workflow, code standards

---

## 🤝 Contributing

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

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

**Note**: Research papers in `refs/publications/` retain their original copyrights. Included under fair use for academic research.

---

## 🙏 Acknowledgments

- **UNH Aquafort**: Farm data, domain expertise, field validation
- **Literature Sources**: 50+ peer-reviewed papers synthesized in this work (see [Literature Review](refs/Literature%20Review%20-%20Data%20Science%20%26%20AI%20Applications%20in%20Sustainable%20Aquaculture%20Systems.md))
- **Open Data Providers**: 
  - ESA Copernicus (Sentinel satellite imagery)
  - CMEMS (marine biogeochemical models)
  - NOAA (meteorological data)
- **Open Source Community**: Scikit-learn, PyTorch, LangChain, PostGIS

---

## 📧 Contact

- **Project Lead**: [Your Name] - [your.email@unh.edu]
- **Issues**: [GitHub Issues](https://github.com/lhzn-io/imta-analytics/issues)
- **Discussions**: [GitHub Discussions](https://github.com/lhzn-io/imta-analytics/discussions)

---

## 🌊 Why IMTA?

> "The solution to nitrification is not dilution but conversion."  
> — Chopin et al., 2001

Integrated Multi-Trophic Aquaculture represents a fundamental shift toward ecosystem-based food production:

- **Environmental**: Convert waste into harvestable biomass, reduce eutrophication
- **Economic**: Diversify revenue streams, capture premium prices
- **Social**: Align aquaculture with sustainability values, support coastal communities

This project aims to make IMTA commercially viable through data-driven optimization and intelligent automation.
