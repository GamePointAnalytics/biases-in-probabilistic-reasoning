# Results Folder Documentation

This folder contains the output results from the tennis win probability models.

## Files

### Game Probability Comparisons
- **`game_prob_comparison_returning.csv`**: Comparison of game winning probabilities for Player 1 when receiving serve, across different point-winning probabilities.
- **`game_prob_comparison_serving.csv`**: Comparison of game winning probabilities for Player 1 when serving, across different point-winning probabilities.

### Set Probability Comparisons
- **`set_prob_comparison_not_serving_first.csv`**: Set winning probabilities for Player 1 when *not* serving the first game of the set.
- **`set_prob_comparison_serving_first.csv`**: Set winning probabilities for Player 1 when *serving* the first game of the set.

## Usage
These files are primarily used for:
1.  **Verification**: Validating the Python implementation (`tennis_probabilities.py`) against known baselines theoretical model outputs.
2.  **Analysis**: analyzing win probabilities for different game and set score scenarios.
