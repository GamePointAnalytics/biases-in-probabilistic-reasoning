# Biases in Probabilistic Reasoning

Exploration and research into common cognitive biases that affect probabilistic reasoning, specifically applied to tennis match analytics.

## Project Structure

### 📄 [`paper/`](paper/)
Contains the primary research paper and related literature.
- **`zhu_biases_probabilistic_reasoning_2024.pdf`**: The main research paper.
- Stephen Zhu (2024). Biases in Micro-level Probabilistic Reasoning and Its Impact on the Spectators’ Enjoyment of Tennis Games, Intelligent Technologies for Interactive Entertainment, Lecture Notes of the Institute for Computer Sciences, Social Informatics and Telecommunications Engineering, vol 560, Springer. https://doi.org/10.1007/978-3-031-55722-4_9

### 🐍 [`scripts/python/`](scripts/python/)
Python scripts and notebooks for analysis and modeling.
- **`Tennis_Analytics.ipynb`**: The core analysis notebook. Handles data cleaning, match statistics, and handedness analysis. Corrected and optimized for local execution.
- **`tennis_probabilities.py`**: A Python implementation of the tennis win probability model (originally in C#). Uses memoized recursion to calculate game, set, and tiebreak probabilities.

### 📂 [`data/`](data/)
Cleaned and processed match datasets.
- Contains point-by-point and match-level data for both Men's (ATP) and Women's (WTA) tennis.
- *See [`data/README.md`](data/README.md) for detailed file descriptions.*

### 📊 [`results/`](results/)
Output files and verification benchmarks.
- Contains CSV comparisons of win probabilities used to verify the Python model against theoretical baselines.
- *See [`results/README.md`](results/README.md) for details.*

## Getting Started
1.  **Data**: Ensure dataset files are in `data/`.
2.  **Analysis**: Run `scripts/python/Tennis_Analytics.ipynb` using Jupyter Notebook or VS Code.
3.  **Modeling**: Run `scripts/python/tennis_probabilities.py` to see probability scenarios.
