# Data Folder Documentation

This folder contains cleaned and processed tennis match data used for analysis.

## Files

### Men's Tennis
- **`m_match_data_cleaned.csv`**: Cleaned match-level data for men's professional tennis matches. Contains match metadata (date, tournament, surface, players).
- **`m_point_data_cleaned_processed.csv`**: Detailed point-by-point data for men's matches.
    - **[Download]**: [INSERT GOOGLE DRIVE LINK HERE] (File exceeds 100MB)

### Women's Tennis
- **`w_match_data_cleaned.csv`**: Cleaned match-level data for women's professional tennis matches.
- **`w_point_data_cleaned_processed.csv`**: Detailed point-by-point data for women's matches.
    - **[Download]**: [INSERT GOOGLE DRIVE LINK HERE] (File exceeds 100MB)

### Documentation
- **`tennis_match_chart_symbols_col_description.xlsx`**: Reference file describing the columns and symbols used in the datasets (e.g., serve location codes, shot types).

## Source
Data is sourced from the [Tennis Match Charting Project](https://github.com/JeffSackmann/tennis_MatchChartingProject).

## Usage
These files are processed inputs for the analysis scripts in `../scripts/python/`. The notebook `Tennis_Analytics.ipynb` expects these files to be present or referenced during execution.
