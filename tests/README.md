# Test Suite for IMTA Analytics

This directory contains the test suite for the `imta_analytics` package.

## Structure

```text
tests/
├── conftest.py              # Shared pytest fixtures
├── unit/                    # Fast unit tests (~5-10s total)
│   ├── test_loaders.py      # TOA5 loading and quality filters
│   └── test_utils.py        # Utility function tests (future)
├── integration/             # Slower integration tests
│   └── test_data_pipeline.py  # End-to-end pipeline tests
└── fixtures/                # Sample data files for testing
```

## Running Tests

```bash
# Activate environment first
conda activate imta-analytics

# Run all tests
pytest tests/

# Run only fast unit tests
pytest tests/unit/

# Run with coverage report
pytest tests/ --cov=imta_analytics --cov-report=html

# Run specific test file
pytest tests/unit/test_loaders.py -v

# Run specific test class or function
pytest tests/unit/test_loaders.py::TestLoadTOA5File::test_basic_loading -v
```

## Pre-commit Hook

A git pre-commit hook automatically runs unit tests before each commit. This catches issues early.

**Location**: `.git/hooks/pre-commit`

To bypass (not recommended):

```bash
git commit --no-verify
```

## Writing Tests

### Test Organization

- **Unit tests**: Test individual functions in isolation
- **Integration tests**: Test complete workflows with real data
- **Fixtures**: Shared test data in `conftest.py`

### Example Test

```python
import pytest
from imta_analytics.data import load_toa5_file

def test_basic_loading(sample_toa5_file):
    """Test that basic TOA5 file loads correctly."""
    df, metadata, units = load_toa5_file(sample_toa5_file)
    
    assert len(df) > 0
    assert 'TIMESTAMP' in df.columns
    assert metadata['station'] == 'TestStation'
```

### Using Parametrize

Test multiple cases efficiently:

```python
@pytest.mark.parametrize("error_code", [143052, 193039, 91625, -86.48])
def test_error_codes_filtered(error_code):
    """Test that error codes are removed."""
    # Test implementation
```

## Test Guidelines

1. **Keep unit tests fast** - aim for <10 seconds total
2. **Mock external dependencies** - no network calls, minimal file I/O
3. **Test boundaries** - empty data, NaN, outliers, error codes
4. **Use descriptive names** - `test_sensor_errors_become_nan` not `test_1`
5. **One assertion per test** - makes failures easier to debug
6. **Use fixtures** - avoid code duplication across tests

## Coverage Goals

- **Unit tests**: >80% coverage for core data loading/cleaning functions
- **Integration tests**: Cover major workflows end-to-end
- **Focus on critical paths**: Prioritize TOA5 loading, quality filters, analysis functions

## Current Status

- ✅ Test infrastructure created
- ✅ Pre-commit hook configured
- ✅ Unit tests for TOA5 loaders
- ✅ Integration tests for data pipeline
- Planned: Utility function tests (future)
- Planned: Analysis function tests (future)
- Planned: Visualization tests (future)
