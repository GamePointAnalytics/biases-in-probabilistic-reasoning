import functools

def to_traditional_score(score):
    """Converts numeric score (0-4) to traditional tennis notation."""
    mapping = {0: "0", 1: "15", 2: "30", 3: "40", 4: "Ad"}
    return mapping.get(score, "")

@functools.lru_cache(maxsize=None)
def player1_game_winning_probability(score1, score2, point_won_pct1):
    """
    Calculate the probability of player1 winning a game from the current score.
    Uses recursion with memoization.
    """
    # Handle the special case where 40-Ad returns to deuce (3-3)
    if score1 == 4 and score2 == 4:
        score1, score2 = 3, 3

    # Deuce case: Use the closed-form formula for the infinite series
    if score1 == 3 and score2 == 3:
        p = point_won_pct1
        return (p * p) / (1 - (2 * p * (1 - p)))

    # Win condition: scored 4+ points and leading by 2+
    if score1 > 3 and (score1 - score2) >= 2:
        return 1.0
    
    # Loss condition: opponent scored 4+ and leading by 2+
    if score2 > 3 and (score2 - score1) >= 2:
        return 0.0

    # Recursive step
    return (point_won_pct1 * player1_game_winning_probability(score1 + 1, score2, point_won_pct1)) + \
           ((1 - point_won_pct1) * player1_game_winning_probability(score1, score2 + 1, point_won_pct1))

@functools.lru_cache(maxsize=None)
def tiebreak_game_winning_probability(tb_score1, tb_score2, p1_serve_prob, p1_return_prob, p1_serving_first, tb_target=7):
    """
    Calculate probability of player1 winning a tiebreak.
    Accounts for alternating serves.
    """
    if tb_score1 >= tb_target and (tb_score1 - tb_score2) >= 2:
        return 1.0
    if tb_score2 >= tb_target and (tb_score2 - tb_score1) >= 2:
        return 0.0
    
    # Depth limit similar to C# (prevent infinite recursion in theoretical edge cases)
    if tb_score1 == tb_score2 and (tb_score1 + tb_score2) > 30:
        return 0.5

    total_points = tb_score1 + tb_score2
    
    # Logic for who serves:
    # Point 0: Server A
    # Points 1-2: Server B
    # Points 3-4: Server A
    # etc.
    if total_points == 0:
        p1_serving = p1_serving_first
    else:
        # Every 2 points effective alternation after the first point
        # (total_points + 1) // 2 determines the "pair" index
        p1_serving = p1_serving_first if ((total_points + 1) // 2) % 2 == 0 else not p1_serving_first

    prob_win_point = p1_serve_prob if p1_serving else p1_return_prob
    
    return (prob_win_point * tiebreak_game_winning_probability(tb_score1 + 1, tb_score2, p1_serve_prob, p1_return_prob, p1_serving_first, tb_target)) + \
           ((1 - prob_win_point) * tiebreak_game_winning_probability(tb_score1, tb_score2 + 1, p1_serve_prob, p1_return_prob, p1_serving_first, tb_target))

@functools.lru_cache(maxsize=None)
def player1_set_winning_probability(score1, score2, p1_serve_prob, p1_return_prob, p1_serving_first):
    """
    Calculate the probability of player1 winning a set.
    """
    # 6 games and 2+ lead = win
    if score1 == 6 and (score1 - score2) >= 2:
        return 1.0
    # 7 games (won tiebreak or 7-5) = win
    if score1 == 7 and score2 < 7:
        return 1.0
    # Opponent wins
    if score2 == 6 and (score2 - score1) >= 2:
        return 0.0
    if score2 == 7 and score1 < 7:
        return 0.0

    # 6-6: Tiebreak
    if score1 == 6 and score2 == 6:
        return tiebreak_game_winning_probability(0, 0, p1_serve_prob, p1_return_prob, p1_serving_first)

    # Determine who serves next game
    # Alternates every game.
    is_even_game = (score1 + score2) % 2 == 0
    p1_serving_game = p1_serving_first if is_even_game else not p1_serving_first
    
    p1_win_game_prob = player1_game_winning_probability(0, 0, p1_serve_prob if p1_serving_game else p1_return_prob)

    return (p1_win_game_prob * player1_set_winning_probability(score1 + 1, score2, p1_serve_prob, p1_return_prob, p1_serving_first)) + \
           ((1 - p1_win_game_prob) * player1_set_winning_probability(score1, score2 + 1, p1_serve_prob, p1_return_prob, p1_serving_first))

def run_scenarios():
    p1_serve = 0.59
    p1_return = 0.44
    
    print(f"Player1 point winning prob on serve: {p1_serve}")
    print("-" * 30)
    print("Game Winning Probabilities:")
    for s1 in range(4):
        for s2 in range(4):
            prob = player1_game_winning_probability(s1, s2, p1_serve)
            print(f"{to_traditional_score(s1)},{to_traditional_score(s2)},{prob:.4f}")

    # Advantage cases
    print(f"Ad,40,{player1_game_winning_probability(4, 3, p1_serve):.4f}")
    print(f"40,Ad,{player1_game_winning_probability(3, 4, p1_serve):.4f}")

    print("\nSet Winning Probability (0-0):")
    set_prob = player1_set_winning_probability(0, 0, p1_serve, p1_return, True)
    print(f"P1 serving first: {set_prob:.4f}")

if __name__ == "__main__":
    run_scenarios()
