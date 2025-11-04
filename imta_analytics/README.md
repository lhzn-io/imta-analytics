# IMTA Analytics Python Package

This directory contains the `imta_analytics` Python package for loading, analyzing, and visualizing data from Integrated Multi-Trophic Aquaculture (IMTA) monitoring systems.

## Installation

### Development Installation

For local development, install the package in editable mode:

```bash
# From the project root
pip install -e .
```

This allows you to import the package in notebooks and scripts while still being able to edit the source code.

### Production Installation

```bash
pip install .
```

## Package Structure

```
imta_analytics/
├── __init__.py           # Package initialization, version info
├── data/                 # Data loading and parsing
│   ├── __init__.py
│   └── loaders.py        # TOA5 and other format loaders
├── quality/              # Data quality checks (future)
├── analysis/             # Analysis functions (future)
└── web/                  # Web application components (future)
```

## Usage

### Loading TOA5 Files

```python
from imta_analytics.data import load_toa5_file

# Load Campbell Scientific TOA5 format data
df, metadata, units = load_toa5_file('data/UNH-G2000B_EXO2SumData.dat')

# Access metadata
print(f"Station: {metadata['station']}")
print(f"Logger: {metadata['logger_model']}")

# Access units
print(f"Temperature units: {units[5]}")  # Depends on column index
```

### Data Quality Filtering

```python
from imta_analytics.data.loaders import apply_marine_quality_filters

# Remove sensor error codes and physically impossible values
df_clean = apply_marine_quality_filters(df)

print(f"Removed {len(df) - len(df_clean)} invalid records")
```

## Development

### Running Tests

```bash
pytest tests/
```

### Code Formatting

```bash
black imta_analytics/
```

### Type Checking

```bash
mypy imta_analytics/
```

## Contributing

This package is part of the UNH Aquafort IMTA monitoring project. For questions or contributions, please contact the UNH CSSS team.

## License

[To be determined]
