# Biases in Probabilistic Reasoning

This research examines the winning probabilities across various scoring scenarios in tennis and reveals that the common-sense theoretical model makes accurate probability predictions at the macro level (set level) but inaccurate predictions at the micro level (game level). This suggests that our intuitive probabilistic estimates of tennis game outcomes are often incorrect.

## Project Structure

### 📄 [`paper/`](paper/)
Contains the primary research paper.
- **`zhu_biases_probabilistic_reasoning_2024.pdf`**: The main research paper.
- Stephen Zhu (2024). Biases in Micro-level Probabilistic Reasoning and Its Impact on the Spectators’ Enjoyment of Tennis Games, Intelligent Technologies for Interactive Entertainment, Lecture Notes of the Institute for Computer Sciences, Social Informatics and Telecommunications Engineering, vol 560, Springer. https://doi.org/10.1007/978-3-031-55722-4_9

**Abstract**

In sports games, the excitement and suspense felt by the spectators are essential to their entertainment experience. The level of excitement and suspense is linked to the spectators' reasoning about the probability of winning or losing. In tennis, as in many other sports, spectators' predictions of winning probabilities largely hinge on the scores. Given tennis's hierarchical scoring system, its probabilistic reasoning is multifaceted and complex. This research examines the winning probabilities across various scoring scenarios, using data from thousands of professional tennis matches and comparing them with theoretical models generally aligned with spectators' common beliefs. The analysis reveals that the theoretical model makes accurate probability predictions at the macro level but inaccurate predictions at the micro level, pointing to possible biases in micro-level probabilistic reasoning. A recent behavioral economic theory may help explain the causes of such biases. Biases are generally seen as undesirable errors, but this study offers a counterargument that biases in micro-level probabilistic reasoning actually enhance the enjoyment of tennis matches by creating expectations, anxiety, and surprises.

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
