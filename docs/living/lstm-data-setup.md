# LSTM Baseline Data Setup

This page describes the inputs for `scripts/run_lstm_baseline.py` and `notebooks/baseline_do_prediction_lstm.ipynb`. See [data-sources.md](data-sources.md) for the wider data catalogue.

## Source Data

The model trains on the YSI EXO2 summary table logged by the Campbell Scientific CR1000X at the UNH Aquafort buoy station (`UNH-G2000B_EXO2SumData.dat`, TOA5 format, 15-minute sampling). The field PC uploads it to the `gs://unh-aquafort-data` bucket.

Access requires authorization from UNH-CSSS, through either:

- a Google account granted read access to the bucket, or
- the UNH-CSSS `aquafort-access` web portal, whose credentials are issued by UNH-CSSS.

Never commit credentials, signed URLs or portal links containing a password to this repository; it is public.

## Setup

1. Copy the raw file into the expected location (with an authorized Google account):

   ```bash
   mkdir -p data/aquafort-buoy-station
   gcloud storage cp gs://unh-aquafort-data/UNH-G2000B_EXO2SumData.dat data/aquafort-buoy-station/
   ```

2. Run the pipeline from the repository root, inside the `imta-analytics` environment:

   ```bash
   python scripts/run_lstm_baseline.py
   ```

   The script loads the file with `imta_analytics.data.load_toa5_file()`, applies physical bounds filtering, writes `data/processed/exo2_data.feather`, and saves the model to `models/` and figures to `results/`.

The notebook reads `data/processed/exo2_data.feather`, so run the script (or `notebooks/01_initial_data_exploration.ipynb`) first.

## Requirements

- At least 2,000 samples after cleaning; six to nine months of data covers the seasonal cycle.
- Columns: `TIMESTAMP`, `EXO2Temp`, `EXO2Salinity`, `EXO2pH`, `EXO2Chlor`, `EXO2Turb`, `EXO2Depth`, `EXO2DO` (% saturation, the target).

`data/`, trained models (`*.keras`, `*.h5`) and `results/` are not tracked in git.

## Related Documentation

- [20260929-lstm-baseline-implementation.md](../analysis/20260929-lstm-baseline-implementation.md): model design and results
- [20251113-data-exploration-findings.md](../analysis/20251113-data-exploration-findings.md): data exploration
