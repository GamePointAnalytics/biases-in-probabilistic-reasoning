# Python Scripts Documentation

This folder contains the core Python code for analysis and modeling.

## Files

### 1. `Tennis_Analytics.ipynb`
**Description**: A Jupyter Notebook for analyzing tennis match data.
**Key Features**:
- Data cleaning and preprocessing for match and point-level data.
- Handedness analysis (correction and impact).
- Generates statistics on match outcomes.
- **Note**: This notebook has been optimized for local execution (Google Drive dependencies removed).

### 2. `tennis_probabilities.py`
**Description**: A Python implementation of the Tennis Win Probability Model.
**Key Features**:
- Calculates the probability of winning a game, set, or tiebreak.
- Uses **memoization** (`functools.lru_cache`) to optimize recursive calculations.
- Based on the theoretical "common probability model" originally implemented in C#.

## Usage
- **Notebook**: Open `Tennis_Analytics.ipynb` in VS Code or Jupyter Lab. Ensure your kernel is set to the correct Python environment.
- **Script**: Run `python tennis_probabilities.py` to see sample probability outputs for different score scenarios.
