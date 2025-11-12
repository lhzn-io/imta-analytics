# Infrastructure Architecture & Technology Stack

**Last Updated**: 2025-11-12

## Overview

This document tracks technology selections, architectural decisions, and evaluation criteria for the IMTA Analytics platform. Our philosophy emphasizes:

- **Cloud-first architecture** for rapid prototyping and cost optimization during bootstrap phase
- **Open-source preference** where feasible for academic reproducibility
- **Edge deployment readiness** for scenarios with limited connectivity
- **Proven tools** over bleeding-edge to minimize risk

**Infrastructure Provider**: Long Horizon Initiative provides cloud infrastructure and API access as catalyzed partner (GCP, Azure, Anthropic/Azure OpenAI). Cost estimates in this document reflect operational costs at scale.

See [README.md](../README.md) for project context and research goals.

---

## Current Stack (In Production/Active Use)

**Status**: Basic data pipeline and exploratory analysis capabilities

### Core Environment

- **Python**: 3.10+
- **Environment Management**: Conda (`environment.yml`)
- **Package Management**: pip with editable install (`pip install -e .`)

### Data Science & Analysis

- **NumPy**: Array operations and numerical computing
- **Pandas**: DataFrame operations and time-series analysis
- **Matplotlib/Seaborn**: Visualization
- **Jupyter**: Interactive notebooks for exploratory analysis

### Domain-Specific Tools

- **Campbell Scientific TOA5 Parser**: Custom loader in `imta_analytics.data.loaders`
- **Marine Sensor QC**: Behavioral heuristics for detecting sensor errors

### Version Control

- **Git**: Source code version control
- **GitHub**: Repository hosting and collaboration

---

## Under Active Evaluation

**Status**: Researching and prototyping during early development phase

### Cloud Platform (GCP)

**Decision Driver**: Managed services reduce operational overhead during bootstrap phase with limited DevOps resources

- **BigQuery**: Data warehouse for time-series analysis
  - **Cost Estimate**: $5-20/month for initial datasets
  - **Alternative Considered**: Self-hosted PostgreSQL/TimescaleDB
  - **Trade-off**: Higher per-query cost vs. zero maintenance burden

- **Vertex AI**: ML model training and deployment
  - **Cost Estimate**: Pay-per-use, ~$50-200/month for initial experiments
  - **Alternative Considered**: Local GPU workstation
  - **Trade-off**: Higher compute cost vs. instant scalability

- **Enterprise Knowledge Graph**: Structured aquaculture domain knowledge
  - **Cost Estimate**: TBD (pricing inquiry in progress)
  - **Alternative Considered**: Open-source GraphDB, Neo4j AuraDB
  - **Trade-off**: Native GCP integration vs. additional service layer

### Satellite & Remote Sensing

- **Sentinel-2/3**: ESA Copernicus open data
  - **Cost**: Free for public data
  - **Access**: Sentinelsat Python API, Google Earth Engine

- **Commercial Datasets**: Planet Labs, Maxar (evaluation pending)
  - **Cost Estimate**: $500-2000/month depending on coverage area
  - **Decision Pending**: Cost-benefit analysis vs. public data quality

### AI & NLP (For IMTA Operator Co-Pilot)

**LLM Strategy**: Prioritize open-source models aligned with UNH partnership and NSF funding constraints, with proprietary models available for evaluation.

**Current Access (Operational)**:

- **Anthropic Claude (Sonnet 4.5, Opus 4.1)**: Direct API access, proven aquaculture domain performance
- **Google Gemini 2.5 Pro**: GCP integration, multimodal capabilities

**Available for Evaluation**:

- **Azure OpenAI (GPT-5, o1, 4o)**: Via Microsoft enterprise agreement, requires minimal integration work
- **Ai2 Open Models (OLMo, Molmo)**: Fully open text and multimodal models
  - **UNH Connection**: Dr. Samuel Carton (UNH) is co-PI on NSF/NVIDIA $152M award to Ai2 for open AI ecosystem
  - **Models**: OLMo (text), Molmo (multimodal) - fully reproducible with open data, code, evaluations
  - **Strategic Fit**: Aligns with CSSS emphasis on open-source, supports NSF funding objectives
  - **Reference**: [NSF/NVIDIA Ai2 Partnership](https://allenai.org/blog/nsf-nvidia)

**Cost Estimate**: $100-500/month for proprietary APIs; open models require compute infrastructure (covered by existing GCP allocation)

**Evaluation Criteria**: Response quality, aquaculture domain performance, cost per query, reproducibility, alignment with funding requirements

- **RAG Infrastructure**: Retrieval-Augmented Generation
  - **Vector DB Options**: Chroma (open-source), Pinecone (managed)
  - **Knowledge Graph**: GCP Enterprise KG vs. Neo4j AuraDB vs. open-source GraphDB
  - **Status**: Architecture design in progress

### Edge Deployment Infrastructure

**Decision Driver**: Offshore IMTA sites may have limited cloud connectivity; need local processing capability

- **PostgreSQL + TimescaleDB**: Time-series database for edge scenarios
  - **Deployment Target**: Raspberry Pi 4/5, NVIDIA Jetson
  - **Status**: Architecture planned, not yet implemented

---

## Technology Decision Framework

### Selection Criteria

When evaluating new technologies, we assess:

- **Cost**: Bootstrap budget constraints (~$500-1000/month for all services)
- **Scalability**: Clear path from prototype to production
- **Vendor Lock-in**: Can we migrate if needed? Export data easily?
- **Edge Readiness**: Can it run on resource-constrained devices?
- **Academic Reproducibility**: Open data formats, documented APIs
- **Community Support**: Active development, good documentation
- **Integration Effort**: Time to first value vs. complexity

### Cost Tiers

- **Tier 1 (Essential)**: Core tools we can't operate without
  - Python environment, Git, basic cloud storage
  - Operational cost: $50-100/month

- **Tier 2 (High Value)**: Tools that significantly accelerate development
  - BigQuery, LLM APIs, managed ML services
  - Operational cost: $300-500/month

- **Tier 3 (Nice to Have)**: Tools that enhance but aren't critical
  - Commercial satellite data, premium monitoring
  - Operational cost: $500+ (pending funding)

---

## Domain-Specific Stack

### Data Science & ML

| Category | Current | Evaluating | Future Consideration |
|----------|---------|------------|---------------------|
| **Core Libraries** | NumPy, Pandas, Scikit-learn | Polars (faster DataFrames) | Dask (distributed) |
| **Deep Learning** | - | PyTorch, TensorFlow/Keras | JAX |
| **Time Series** | Pandas | statsmodels, Prophet | NeuralProphet, LSTM/GRU |
| **Optimization** | SciPy | Optuna (hyperparameter tuning) | DEAP (genetic algorithms) |

### Geospatial & Remote Sensing

| Category | Current | Evaluating | Future Consideration |
|----------|---------|------------|---------------------|
| **Processing** | - | GDAL, Rasterio | Google Earth Engine API |
| **Analysis** | - | GeoPandas, Shapely | H3 (Uber hexagonal grid) |
| **Visualization** | Matplotlib | Folium (interactive maps) | Kepler.gl |
| **Database** | - | PostGIS | Cloud-native geospatial (BigQuery GIS) |

### AI & NLP

| Category | Current | Evaluating | Future Consideration |
|----------|---------|------------|---------------------|
| **LLMs** | Claude Sonnet 4.5, Gemini 2.5 Pro | Ai2 OLMo/Molmo (UNH co-PI), Azure OpenAI | Llama 3, other open models |
| **Vector DB** | - | Chroma, Pinecone | Weaviate, Qdrant |
| **Knowledge Graphs** | - | GCP Enterprise KG, Neo4j AuraDB, GraphDB | RDFlib, Apache Jena |
| **Orchestration** | - | LangChain | LlamaIndex, custom |

### Data Infrastructure

| Category | Current | Evaluating | Future Consideration |
|----------|---------|------------|---------------------|
| **Data Warehouse** | - | GCP BigQuery | Snowflake, Databricks |
| **Time-Series DB** | - | TimescaleDB | InfluxDB, QuestDB |
| **Stream Processing** | - | - | Apache Kafka, Flink |
| **Data Versioning** | Git | DVC (Data Version Control) | MLflow, Weights & Biases |

### Web & APIs

| Category | Current | Evaluating | Future Consideration |
|----------|---------|------------|---------------------|
| **Backend** | - | FastAPI | Flask, Django |
| **Frontend** | - | Plotly Dash | React, Streamlit |
| **API Gateway** | - | GCP API Gateway | Kong, Tyk |

### DevOps & Deployment

| Category | Current | Evaluating | Future Consideration |
|----------|---------|------------|---------------------|
| **Containerization** | - | Docker, docker-compose | Podman |
| **Orchestration** | - | - | Kubernetes (production) |
| **CI/CD** | GitHub Actions (planned) | - | GitLab CI, CircleCI |
| **Monitoring** | - | GCP Cloud Monitoring | Prometheus, Grafana |
| **Data Pipelines** | - | - | Apache Airflow, Prefect |

---

## Decision Log

### 2025-11-12: Cloud-First Strategy (GCP)

**Decision**: Adopt Google Cloud Platform as primary infrastructure during bootstrap phase

**Rationale**:

- Turn-key GCP access via catalyzed partner eliminates initial infrastructure costs
- Managed services (BigQuery, Vertex AI) reduce DevOps burden with limited team resources
- Pay-per-use pricing aligns with variable early-stage workloads
- Enterprise Knowledge Graph native integration (vs. separate Neo4j AuraDB layer)
- Azure available as secondary option if GCP limitations arise
- Clear migration path to edge deployment (PostgreSQL/TimescaleDB) if needed

**Trade-offs**:

- Higher per-query costs vs. self-hosted infrastructure
- Vendor lock-in risk (mitigated by open data formats, standard SQL)
- Requires internet connectivity (addressed by planned edge deployment architecture)

**Estimated Cost**: $500-1000/month at operational scale

**Alternatives Considered**:

- Self-hosted PostgreSQL/TimescaleDB on VPS: Lower cost but higher maintenance
- AWS: No direct access via catalyzed partner; would require separate account setup
- Neo4j AuraDB on GCP: Additional service layer vs. native GCP Enterprise KG integration

**Status**: Active evaluation in progress

---

### 2025-11-12: Knowledge Graph Technology Selection (Pending)

**Options Under Consideration**:

1. **Google Cloud Enterprise Knowledge Graph**
   - **Pros**: Native GCP integration, managed service, entity extraction built-in
   - **Cons**: Cost TBD, newer service with less community knowledge
   - **Cost**: Pricing inquiry in progress

2. **Neo4j AuraDB (hosted on GCP)**
   - **Pros**: Industry-standard graph database, excellent tooling (Bloom visualization)
   - **Cons**: Additional service layer, higher cost (~$65-500/month), less team experience
   - **Cost**: ~$65/month minimum (AuraDB Professional)

3. **Open-Source GraphDB** (e.g., Apache Jena, Blazegraph)
   - **Pros**: Free, full control, academic reproducibility
   - **Cons**: Self-hosted maintenance burden, limited managed features
   - **Cost**: Hosting only (~$10-50/month)

**Decision Criteria**:

- Cost vs. capability balance given bootstrap budget
- Integration effort with GCP Vertex AI and LangChain
- Ontology management workflow (can domain experts contribute?)
- Query performance for RAG use case (sub-second response time required)

**Next Steps**:

- Complete GCP Enterprise KG pricing inquiry
- Prototype RAG architecture with Chroma vector DB + simple knowledge graph
- Evaluate query performance with sample aquaculture ontology

**Status**: Decision pending technical evaluation (target: December 2025)

---

## Notes

- This document is a **living record** - update as technologies are adopted, evaluated, or rejected
- Link to benchmark notebooks when performance testing tools (e.g., `notebooks/benchmarks/bigquery-vs-timescaledb.ipynb`)
- Include date-stamped decision log entries for major technology choices
- Cost estimates based on November 2025 pricing and projected usage patterns

---

## Related Documentation

- [README.md](../README.md) - Project overview and research goals
- [PACKAGE.md](../PACKAGE.md) - Package structure and development guidelines
- [docs/planning/](planning/) - System design documents
- [environment.yml](../environment.yml) - Current Python dependencies
