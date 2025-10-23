# Analysis Notebooks

This directory contains Jupyter notebooks for IMTA data analysis, visualization, and modeling.

## Organization

Notebooks are organized by analysis type and research focus area:

### Data Exploration
- `01_data_exploration.ipynb` - Initial data exploration and quality assessment
- `02_descriptive_statistics.ipynb` - Summary statistics and data distributions

### Ecosystem Analysis
- `10_nutrient_cycling.ipynb` - Nutrient flow and mass balance analysis
- `11_water_quality.ipynb` - Water quality parameter analysis and visualization
- `12_species_interactions.ipynb` - Multi-species interaction modeling

### Production Analysis
- `20_growth_analysis.ipynb` - Growth rate analysis and modeling
- `21_feed_efficiency.ipynb` - Feed conversion ratio and efficiency studies
- `22_yield_optimization.ipynb` - Harvest optimization and yield prediction

### Environmental Impact
- `30_carbon_footprint.ipynb` - Carbon footprint assessment
- `31_nutrient_balance.ipynb` - Nitrogen and phosphorus cycling analysis
- `32_sustainability_metrics.ipynb` - Environmental sustainability indicators

### Economic Analysis
- `40_cost_benefit.ipynb` - Economic cost-benefit analysis
- `41_market_analysis.ipynb` - Market trends and pricing analysis
- `42_risk_assessment.ipynb` - Risk analysis and management strategies

## Naming Convention

Notebooks follow the naming pattern: `[number]_[descriptive_name].ipynb`
- Numbers indicate the category and order
- Use descriptive, lowercase names with underscores
- Keep names concise but informative

## Best Practices

1. **Documentation**: Include markdown cells explaining the analysis objectives, methods, and findings
2. **Reproducibility**: 
   - Set random seeds for reproducible results
   - Document package versions
   - Include data sources and preprocessing steps
3. **Code Quality**:
   - Follow PEP 8 style guidelines
   - Use meaningful variable names
   - Add comments for complex operations
4. **Visualization**:
   - Label all axes clearly
   - Include titles and legends
   - Use appropriate color schemes
   - Save figures in appropriate formats (PNG for web, SVG for publications)
5. **Output Management**:
   - Clear outputs before committing (unless they are essential for documentation)
   - Save large outputs separately in the data directory

## Running Notebooks

```bash
# Start Jupyter Lab
jupyter lab

# Or Jupyter Notebook
jupyter notebook
```

## Dependencies

All required Python packages should be listed in the main `requirements.txt` file in the repository root.

## Contributing

When adding new notebooks:
1. Follow the naming convention
2. Include clear documentation
3. Test all cells run successfully
4. Clear sensitive or large outputs before committing
5. Update this README with a brief description
