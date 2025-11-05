# UNH Aquafort IMTA Case Study: Literature Review & Learning Phase

**Project:** UNH Aquafort IMTA Deployment - Phase 0 Knowledge Foundation  
**Case Study Focus:** Steelhead trout + Blue mussel + Sugar kelp floating platform system  
**Phase:** Phase 0 - Literature Review & Knowledge Acquisition (Weeks 1-4)  
**Partners:** University of New Hampshire (Chambers et al. 2024), UNH-CSSS Analytics Team  
**Date:** October 29, 2025  
**Status:** Literature Review Phase - In Progress  
**Next Phase:** [IMTA Analytics Platform Strategy](imta-analytics-platform-strategy.md) for implementation (Phases 1-4)

---

## Executive Summary

This document guides the **initial learning phase** (Phase 0) for developing an AI-enabled precision aquaculture system for the UNH Aquafort IMTA deployment. This case study serves as the concrete foundation for the broader [IMTA Analytics Platform Strategy](imta-analytics-platform-strategy.md).

**Purpose:** Before designing and building the technical platform, we must deeply understand:

1. Scientific literature on IMTA systems, predictive modeling, and AI decision support
2. Existing precision aquaculture platforms (especially Aquasafe)
3. UNH Aquafort's specific operational context (Chambers et al. 2024)
4. Technical requirements for the three target species (steelhead trout, blue mussels, sugar kelp)

Following discussions with UNH Aquafort IMTA deployment maintainers, this roadmap prioritizes literature review to inform system design. The system will ultimately feature a Copilot interface providing assistance across the full lifecycle:

1. **Site Selection** - Environmental suitability analysis
2. **Configuration** - Species selection, infrastructure design, sensor deployment
3. **Deployment** - Installation optimization, initial stocking strategies
4. **Maintenance** - Daily feeding optimization, infrastructure resilience monitoring

---

## 1. Priority Literature Review

### 1.1 Immediate Deep-Dive Papers (Week 1-2)

Based on our project requirements and available literature, we should absorb these papers in detail **first**:

#### **Tier 1: System Foundation (Must Read Immediately)**

1. **Chambers et al. (2024)** - *Integrated multi-trophic aquaculture of steelhead trout, blue mussel and sugar kelp from a floating ocean platform*
   - **Why:** This IS the UNH Aquafort deployment we're supporting
   - **Key Data:** Actual production data (416 kg trout, 3,072 kg mussels, 638 kg kelp), 16.4 kg net N reduction
   - **Extract:** Species performance, environmental conditions, operational challenges, infrastructure design
   - **Action:** Extract all quantitative data for baseline model calibration

2. **Chatziantoniou et al. (2023)** - *Aquasafe: A Remote Sensing Web-Based Platform for the Support of Precision Fish Farming*
   - **Why:** Most directly relevant reference architecture for our DSS
   - **Key Features:** Alert system design (DO, chl-a, SST thresholds), DEB model integration, multi-source data fusion
   - **Extract:** System architecture, API design, alert logic, user feedback (82% found interface clear, but 45% wanted simplification)
   - **Action:** Adapt their three-tier architecture and alert framework

3. **Føre et al. (2024)** - *Digital Twins in intensive aquaculture - Challenges, opportunities and future prospects*
   - **Why:** Cutting-edge framework for predictive modeling in aquaculture
   - **Key Concepts:** Digital twin architecture, real-time data integration, what-if scenario simulation
   - **Extract:** Implementation challenges, data requirements, model calibration approaches
   - **Action:** Design our system as a digital twin of Aquafort deployment

4. **Chatziantoniou et al. (2022)** - *Dissolved oxygen estimation in aquaculture sites using remote sensing and machine learning*
   - **Why:** DO is critical limiting factor; R² = 0.67 using SVR models
   - **Key Methods:** Support Vector Regression, Sentinel-3 SLSTR (SST), Sentinel-2 MSI (chl-a), temporal lags
   - **Extract:** Feature engineering approach, model performance metrics, seasonal patterns
   - **Action:** Replicate methodology for New England waters

#### **Tier 2: Species-Specific Modeling (Week 2)**

5. **Venolia et al. (2020)** - *Modeling the Growth of Sugar Kelp (Saccharina latissima) in Aquaculture Systems using Dynamic Energy Budget Theory*
   - **Why:** Sugar kelp is one of the three species at Aquafort; DEB model for growth prediction
   - **Key Data:** Temperature effects (optimal 10-15°C), nutrient uptake kinetics, seasonality (0.77 cm/day winter → 3.52 cm/day spring)
   - **Extract:** DEB parameters for S. latissima, model equations, validation data
   - **Action:** Integrate kelp growth model into our predictive framework

6. **Stavrakidis-Zachou et al. (2019)** - *A DEB model for European sea bass (Dicentrarchus labrax): Parameterisation and application in aquaculture*
   - **Why:** DEB methodology applicable to steelhead trout with species-specific calibration
   - **Key Methods:** Parameter estimation from controlled experiments, temperature corrections (Arrhenius), feed conversion
   - **Extract:** Model structure, calibration procedure, sensitivity analysis
   - **Action:** Adapt for O. mykiss (steelhead trout) using Chambers' data

7. **Andika et al. (2024)** - *Growth and survival of milkfish, tiger prawns, and oysters in IMTA system with varying stocking densities*
   - **Why:** Only recent paper examining stocking density optimization in multi-species IMTA
   - **Key Findings:** Treatment B (15 fish, 20 prawns, 30 oysters/300m³) achieved 100% survival, highest SGR (2.67%/day)
   - **Extract:** Density-growth relationships, DO consumption patterns, species interactions
   - **Action:** Inform optimal stocking recommendations for Aquafort configuration

#### **Tier 3: ML/AI Decision Support (Week 2-3)**

8. **Barzegar et al. (2020)** - *Short-term water quality variable prediction using a hybrid CNN-LSTM deep learning model*
   - **Why:** Time-series prediction for DO, temperature, pH; hybrid CNN-LSTM outperformed standalone models
   - **Key Architecture:** 1D CNN for feature extraction + LSTM for temporal dependencies
   - **Extract:** Network architecture, hyperparameters, training strategy, performance comparisons
   - **Action:** Implement hybrid model for 24-72 hour water quality forecasts

9. **Ta et al. (2018)** - *Research on a dissolved oxygen prediction method for recirculating aquaculture systems based on a convolution neural network*
   - **Why:** CNN-based DO prediction with "reverse-understanding" architecture
   - **Key Innovation:** Uses spatial patterns in multi-sensor data for better predictions
   - **Extract:** CNN architecture for DO prediction, comparison with traditional methods
   - **Action:** Evaluate against LSTM approach for our application

10. **Channa et al. (2023)** - *Optimisation of Small-Scale Aquaponics Systems Using Artificial Intelligence and the IoT: Current Status, Challenges, and Opportunities*
    - **Why:** Comprehensive review of IoT sensor selection, ML applications, energy optimization
    - **Key Insights:** 67% use Arduino, WiFi dominant (85%), energy is primary bottleneck (56 kWh/kg vegetables)
    - **Extract:** Sensor recommendations (DHT22 for temp, Atlas Scientific for pH/DO), communication protocols, optimization strategies
    - **Action:** Design sensor network and edge computing architecture

### 1.2 Secondary Priority (Week 3-4)

#### **Economic Viability & Adoption**

11. **Knowler et al. (2020)** - *The Economics of Integrated Multi-Trophic Aquaculture*
    - **Why:** Comprehensive economic analysis; B/C ratios 1.1-1.7, 10-36% price premiums
    - **Focus:** Profitability modeling, sensitivity analysis, market considerations
    - **Action:** Build economic optimization module for our DSS

12. **Carras et al. (2019)** - *A discounted cash-flow analysis of salmon monoculture and IMTA in eastern Canada*
    - **Why:** DCF methodology for IMTA, comparison with monoculture, price premium scenarios
    - **Focus:** NPV calculations, risk modeling, financial decision support
    - **Action:** Adapt DCF framework for Aquafort deployment scenarios

#### **System Design & Infrastructure**

13. **Føre et al. (2018)** - *Precision fish farming: A new framework to improve production in aquaculture*
    - **Why:** Foundational paper defining precision fish farming concept
    - **Focus:** Sensor technologies, real-time monitoring, automated control systems
    - **Action:** Align our system design with precision farming principles

14. **Buck et al. (2018)** - *State of the Art and Challenges for Offshore IMTA*
    - **Why:** Addresses infrastructure challenges for offshore deployments (relevant to Aquafort's floating platform)
    - **Focus:** Engineering requirements, environmental exposure, operational logistics
    - **Action:** Inform infrastructure resilience monitoring module

#### **Site Selection & Configuration**

15. **Widowati et al. (2020)** - *Ecological and Economical Analysis for Implementing IMTA*
    - **Why:** Multi-criteria site suitability scoring (temperature, DO, pH weighted at 5; salinity at 4; nutrients at 3)
    - **Focus:** Suitability index methodology, GIS-based site selection
    - **Action:** Implement weighted suitability scoring algorithm

16. **Kerrigan et al. (2016)** - *A meta-analysis of IMTA: extractive species growth is most successful within close proximity to open-water fish farms*
    - **Why:** Spatial configuration optimization; proximity effects on nutrient capture
    - **Focus:** Optimal distances between fed species and extractives, spatial arrangement
    - **Action:** Inform configuration recommendations for cage/line placement

### 1.3 Emerging Research & Adjacent Technologies (Ongoing)

17. **Rusco et al. (2024)** - *Can IMTA System Improve the Productivity and Quality Traits of Aquatic Organisms*
    - **Why:** Recent analysis of IMTA benefits beyond sustainability (product quality improvements)
    - **Focus:** Quality metrics, comparative analysis

18. **Stavrakidis-Zachou et al. (2021)** - *Projecting climate change impacts on Mediterranean finfish production*
    - **Why:** Climate adaptation modeling methodology
    - **Focus:** Long-term forecasting under climate scenarios
    - **Action:** Build climate adaptation planning module

19. **Zupa et al. (2021)** - *Calibrating Accelerometer Tags with Oxygen Consumption Rate of Rainbow Trout*
    - **Why:** Novel sensor approach for metabolic monitoring (accelerometry as proxy for O₂ consumption)
    - **Focus:** Individual fish monitoring, stress detection
    - **Action:** Explore for advanced fish welfare monitoring

### 1.4 Important References Cited in Primary Papers

From our literature review synthesis, these frequently-cited works should be consulted:

**From Chambers et al. (2024):**

- **Myrick & Cech (2005)** - Steelhead trout temperature optima (9-15°C)
- **Maar et al. (2015)** - Blue mussel growth rates under varying salinity/temperature

**From Chatziantoniou et al. (2023):**

- **Claireaux & Lagardère (1999)** - DO thresholds and fish physiological impacts
- **EFSA (2008, 2020)** - Regulatory guidance on fish welfare (5.5 mg/L DO minimum)

**From Economic Papers:**

- **Ridler et al. (2007)** - First comprehensive IMTA economic analysis ($3.3M NPV vs. $2.7M monoculture)
- **Nobre et al. (2010)** - Social accounting framework for IMTA ecosystem services ($1.1-3.0M annual benefit)

**Foundational IMTA Concepts:**

- **Chopin et al. (2001)** - *Integrating Seaweeds into Marine Aquaculture Systems* (seminal paper)
- **Chopin (2006)** - *What is IMTA and why you should care* (definitional clarity)

---

## 2. Strategic Reading Plan

### Week 1: Foundation & Context

- **Day 1-2:** Chambers et al. (2024) - Deep extraction of all data, methods, challenges
- **Day 3-4:** Chatziantoniou et al. (2023) - System architecture, alert design, user feedback
- **Day 5-7:** Føre et al. (2024) - Digital twin framework, implementation strategy

### Week 2: Predictive Modeling

- **Day 8-9:** Chatziantoniou et al. (2022) + Barzegar et al. (2020) - DO prediction models
- **Day 10-11:** Venolia et al. (2020) + Stavrakidis-Zachou et al. (2019) - Species growth models
- **Day 12-14:** Andika et al. (2024) + Channa et al. (2023) - Density optimization, IoT systems

### Week 3: Decision Support & Economics

- **Day 15-17:** Ta et al. (2018) - CNN architectures for prediction
- **Day 18-19:** Knowler et al. (2020) + Carras et al. (2019) - Economic modeling
- **Day 20-21:** Føre et al. (2018) + Buck et al. (2018) - Precision farming, offshore challenges

### Week 4: Configuration & Site Selection

- **Day 22-24:** Widowati et al. (2020) + Kerrigan et al. (2016) - Site selection, spatial config
- **Day 25-28:** Secondary papers + reference chaining for gaps

---

## 3. Key Questions to Answer From Literature

As we read, we need to extract answers to these specific questions:

### 3.1 Site Selection Module

- [ ] What environmental parameters are critical for steelhead trout / blue mussel / sugar kelp co-culture?
- [ ] What are the validated threshold ranges (optimal, tolerance limits)?
- [ ] How do we integrate multi-source data (satellite, in-situ, models) for site assessment?
- [ ] What GIS-based scoring methodology should we use?

### 3.2 Configuration Module

- [ ] What stocking densities optimize growth while maintaining survival (density-dependent effects)?
- [ ] What spatial arrangements maximize nutrient capture efficiency?
- [ ] What sensor suite is required (types, quantities, placements, costs)?
- [ ] What is the minimum viable IoT infrastructure?

### 3.3 Deployment Module

- [ ] What is the optimal stocking schedule across species (temporal sequencing)?
- [ ] How do we predict initial conditions (pre-deployment site assessment)?
- [ ] What contingency plans are needed for adverse conditions?

### 3.4 Maintenance Module - Feeding

- [ ] How do we predict daily feed requirements based on:
  - Current biomass (growth model outputs)
  - Environmental conditions (temperature, DO)
  - Fish behavior (feeding response)
- [ ] What FCR optimization strategies exist?
- [ ] How do we detect overfeeding (waste) vs. underfeeding (growth loss)?

### 3.5 Maintenance Module - Resilience

- [ ] What infrastructure failure modes are most critical?
- [ ] How do we predict DO hypoxia events 24-72 hours ahead?
- [ ] What early warning indicators exist for harmful algal blooms?
- [ ] How do we model storm impacts on infrastructure?

### 3.6 AI/ML Implementation

- [ ] CNN vs. LSTM vs. Hybrid for time-series water quality prediction?
- [ ] How to handle sparse/irregular in-situ measurements?
- [ ] How to integrate physics-based models (DEB) with ML predictions?
- [ ] What edge computing architecture for real-time processing?

### 3.7 User Experience

- [ ] What are the primary user tasks (based on Aquasafe usability study)?
- [ ] How do we design conversational AI (Copilot) for aquaculture domain?
- [ ] What alert fatigue mitigation strategies work?
- [ ] How do we enable human-in-the-loop learning?

---

## 4. Data Extraction Framework

For each priority paper, we'll systematically extract:

### 4.1 Quantitative Data

- **Environmental Parameters:** Measured ranges, optimal values, critical thresholds
- **Species Performance:** Growth rates (SGR, FCR), survival rates, biomass yields
- **Model Performance:** R², RMSE, MAE, accuracy metrics
- **Economic Metrics:** Costs, revenues, NPV, B/C ratios, price premiums

### 4.2 Methodologies

- **Modeling Approaches:** Equations, parameters, assumptions, validation methods
- **Sensor Technologies:** Types, specifications, costs, accuracy, maintenance
- **System Architectures:** Data flows, processing pipelines, APIs, databases
- **Alert Logic:** Thresholds, compound indicators, notification strategies

### 4.3 Lessons Learned

- **What Worked:** Successful implementations, validated approaches, positive outcomes
- **What Failed:** Documented challenges, limitations, unsuccessful attempts
- **User Feedback:** Adoption barriers, usability issues, feature requests
- **Economic Barriers:** Cost prohibitive elements, energy consumption, market challenges

### 4.4 Research Gaps

- **Missing Models:** What phenomena lack predictive models? (e.g., kelp yield forecasting)
- **Data Limitations:** What measurements are sparse/unavailable?
- **Technology Gaps:** What sensors/tools don't exist yet?
- **Integration Challenges:** What data sources are incompatible?

---

## 5. Parallel Activities While Reading

As we absorb literature, we should simultaneously:

### 5.1 Stakeholder Engagement

- **Action:** Schedule follow-up meeting with UNH Aquafort maintainers
- **Questions to Ask:**
  - What are your top 3 operational pain points?
  - What decisions do you make daily/weekly/seasonally?
  - What data do you currently collect? (sensors, manual measurements)
  - What would make you trust an AI recommendation?
  - What's your budget envelope for sensors/infrastructure?

### 5.2 Data Inventory

- **Action:** Request access to any existing Aquafort data:
  - Historical production records (harvest weights, survival rates)
  - Environmental measurements (temperature, salinity, DO, pH)
  - Feeding logs (quantities, schedules, FCR)
  - Infrastructure incidents (equipment failures, weather events)
  - Financial records (costs, revenues, if shareable)

### 5.3 Environmental Data Acquisition

- **Action:** Begin pulling baseline environmental data for Aquafort site:
  - Sentinel-2/3 satellite imagery (Copernicus Open Access Hub)
  - NOAA buoy data (nearest station to deployment site)
  - CMEMS biogeochemical model outputs for Gulf of Maine
  - Historical weather data (OpenWeatherMap, NOAA)
  - Oceanographic data (temperature, salinity, currents)

### 5.4 Technology Stack Exploration

- **Action:** Prototype core technical components:
  - Satellite data API integration (Sentinel Hub, Google Earth Engine)
  - Time-series database setup (InfluxDB, TimescaleDB)
  - ML model training pipeline (PyTorch/TensorFlow)
  - Conversational AI framework (LangChain + domain-specific RAG)
  - Dashboard prototype (Streamlit, Plotly Dash, or React)

---

## 6. Success Criteria for Literature Phase

We'll know we're ready to move to system design when we can:

- [ ] Draw a complete data flow diagram from sensors → models → alerts → user actions
- [ ] Specify exact sensor requirements (types, quantities, costs, placements)
- [ ] Define alert thresholds for top 5 critical parameters (with confidence intervals)
- [ ] Estimate growth rates for all three species under varying environmental conditions
- [ ] Predict DO concentrations 24-72 hours ahead with R² > 0.60
- [ ] Recommend optimal stocking densities for Aquafort configuration
- [ ] Calculate expected ROI for AI system investment vs. operational improvements
- [ ] Design conversational prompts for top 10 user queries

**Phase Completion Criteria:**

- [x] Literature review findings synthesized (see [Literature Review](../../refs/Literature%20Review%20-%20Data%20Science%20%26%20AI%20Applications%20in%20Sustainable%20Aquaculture%20Systems.md))
- [ ] All Tier 1 papers read and extracted (Chambers, Chatziantoniou x2, Føre)
- [ ] Data extraction framework populated with quantitative parameters
- [ ] Ready to proceed with [Platform Strategy](imta-analytics-platform-strategy.md) (Phases 1-4)
- [ ] This document serves as reference for UNH Aquafort case study context

---

## 7. Next Steps

### Immediate Actions (This Week)

1. **Create detailed notes templates** for each Tier 1 paper (structured data extraction)
2. **Set up reference management** (Zotero/Mendeley) with our 50+ papers
3. **Begin deep read of Chambers et al. (2024)** - Extract all quantitative data into spreadsheet
4. **Contact UNH Aquafort team** - Schedule 1-hour technical discussion
5. **Set up development environment** - Python, Jupyter, data science libraries

### Short-Term Milestones (2-4 Weeks)

1. Complete Tier 1 literature deep-dive (7 papers)
2. Draft system architecture document
3. Build proof-of-concept DO prediction model
4. Create interactive site suitability map prototype
5. Design conversational AI prompts for top use cases

### Medium-Term Goals (1-3 Months)

1. Deploy minimum viable product (MVP) with core features
2. Integrate with real Aquafort sensor data (if available)
3. Conduct user testing with UNH operators
4. Iterate based on feedback
5. Prepare for field validation study

---

## 8. Document Control

**Authors:** UNH-CSSS Analytics Team  
**Created:** October 29, 2025  
**Last Updated:** November 4, 2025  
**Version:** 0.2 (Clarified as Phase 0 - Learning Phase)  
**Phase:** Phase 0 (Literature Review & Knowledge Acquisition)  
**Next Phase Document:** `imta-analytics-system-design.md` (Phase 1-4: Implementation)  
**Next Review:** Upon completion of Tier 1 literature review

**Document Purpose:**  
This is the Phase 0 learning roadmap specific to the UNH Aquafort IMTA case study. Once literature review is complete, proceed to `imta-analytics-system-design.md` for comprehensive technical implementation planning applicable to any IMTA deployment.

---

## Appendix A: Paper Inventory Matrix

| Paper | Focus Area | Data Type | Priority | Status |
|-------|-----------|-----------|----------|---------|
| Chambers 2024 | UNH System | Production, Environmental | **CRITICAL** | 🔴 Not Started |
| Chatziantoniou 2023 | DSS Architecture | System Design, UX | **CRITICAL** | 🔴 Not Started |
| Føre 2024 | Digital Twins | Methodology | **CRITICAL** | 🔴 Not Started |
| Chatziantoniou 2022 | DO Prediction | ML Models | **HIGH** | 🔴 Not Started |
| Venolia 2020 | Kelp Growth | DEB Models | **HIGH** | 🔴 Not Started |
| Stavrakidis-Zachou 2019 | Fish Growth | DEB Models | **HIGH** | 🔴 Not Started |
| Andika 2024 | Stocking Density | Production Data | **HIGH** | 🔴 Not Started |
| Barzegar 2020 | Water Quality Prediction | CNN-LSTM | **MEDIUM** | 🔴 Not Started |
| Ta 2018 | DO Prediction | CNN | **MEDIUM** | 🔴 Not Started |
| Channa 2023 | IoT Systems | Hardware, Energy | **MEDIUM** | 🔴 Not Started |

*(Status codes: 🔴 Not Started, 🟡 In Progress, 🟢 Complete, ✅ Extracted to DB)*

---

## Appendix B: Preliminary Feature List

Based on literature review synthesis, our AI system should include:

### Core Capabilities

- **Real-time monitoring dashboard** (multi-parameter visualization)
- **24-72 hour predictive alerts** (DO, temperature, chl-a)
- **Growth forecasting** (species-specific, DEB-based)
- **Feeding optimization** (adaptive recommendations)
- **Economic tracking** (costs, revenues, profitability projections)

### Conversational AI (Copilot Interface)

- **Natural language queries** ("Why is my oxygen dropping?")
- **Scenario simulation** ("What if I harvest 100 kg early?")
- **Educational explanations** ("Teach me about nitrogen cycling")
- **Decision support** ("Should I reduce feeding based on forecast?")

### Advanced Features (Phase 2)

- **Site selection tool** (GIS-based suitability mapping)
- **Configuration optimizer** (species selection, density, spatial layout)
- **Climate adaptation planner** (long-term scenario modeling)
- **Market intelligence** (price forecasting, demand trends)
