import pandas as pd
import numpy as np
import re
import math
import os

# --- Utility Functions (Missing in original Notebook) ---

def get_players(df_matches):
    \"\"\"Extract unique players from match data.\"\"\"
    p1 = df_matches['Player 1'].unique()
    p2 = df_matches['Player 2'].unique()
    return np.unique(np.concatenate([p1, p2]))

def get_points_in_one_match(df_points, match_id):
    \"\"\"Extract points, unique sets, and unique games for a specific match.\"\"\"
    match_points = df_points[df_points['match_id'] == match_id].copy()
    
    # Ensure indices exist
    if 'set_index' not in match_points.columns:
        # Heuristic for set_index if missing (e.g., from Gm1/Gm2 transitions)
        match_points['set_index'] = 1 # Placeholder or logic to detect set changes
    
    sets = match_points['set_index'].unique()
    games = match_points['game_index_in_set'].unique() if 'game_index_in_set' in match_points.columns else []
    
    return match_points, sets, games

def get_player_names(points_in_match, match_id):
    \"\"\"Extract player names from match_id string components or points data.\"\"\"
    parts = match_id.split('-')
    # Default format: date-gender-tournament-round-player1-player2
    if len(parts) >= 6:
        p1 = parts[4].replace('_', ' ')
        p2 = parts[5].replace('_', ' ')
        return p1, p2
    return \"player1\", \"player2\"

# --- Data Cleaning Functions (Fixed and Localized) ---

def clean_match_data(df_matches):
    df_matches = df_matches.copy()
    df_matches.drop_duplicates(subset=\"match_id\", inplace=True)

    # Standardize string columns
    str_cols = [\"Player 1\", \"Player 2\", \"Pl 1 hand\", \"Pl 2 hand\", \"Tournament\", \"Surface\", \"Gender\", \"Round\"]
    for col in str_cols:
        if col in df_matches.columns:
            df_matches[col] = df_matches[col].astype(str).str.strip().str.lower()
            if col in [\"Player 1\", \"Player 2\", \"Tournament\"]:
                df_matches[col] = df_matches[col].replace(to_replace=r\"\\s+\", value=\"_\", regex=True)

    df_matches = df_matches.astype({\"Date\": \"str\"})

    # Fill missing data using nullable types or standard markers
    fill_cols = [\"Surface\", \"Tournament\", \"Player 1\", \"Player 2\", \"Round\"]
    for col in fill_cols:
        df_matches[col] = df_matches[col].fillna(\"unknown\")

    return df_matches

def clean_handedness_match_data(df_matches):
    \"\"\"Fixed: selected_player_hand_value_counts scoping error resolved.\"\"\"
    df_matches = df_matches.copy()
    players = get_players(df_matches)
    df_players_handedness = []

    for player in players:
        # Logic for Player 1 side
        p1_mask = df_matches[\"Player 1\"] == player
        selected_p1_hand = df_matches[p1_mask][\"Pl 1 hand\"]
        counts_p1 = selected_p1_hand.value_counts()

        # Logic for Player 2 side
        p2_mask = df_matches[\"Player 2\"] == player
        selected_p2_hand = df_matches[p2_mask][\"Pl 2 hand\"]
        counts_p2 = selected_p2_hand.value_counts()

        # Combine counts to find the true handedness
        combined_counts = counts_p1.add(counts_p2, fill_value=0)
        
        if len(combined_counts) > 0:
            correct_hand = combined_counts.idxmax()
            
            # Update dataframe with corrected hand
            df_matches.loc[p1_mask, \"Pl 1 hand\"] = correct_hand
            df_matches.loc[p2_mask, \"Pl 2 hand\"] = correct_hand
            
            df_players_handedness.append({\"player\": player, \"handedness\": correct_hand})

    return df_matches, pd.DataFrame(df_players_handedness)

def clean_point_data(df_points):
    \"\"\"Fixed: int32 cast error for NaNs and localized logic.\"\"\"
    df_points = df_points.copy()

    # Use 'Int32' (capital I) for nullable integers to prevent crash on NaN
    int_cols = [\"TB?\", \"Pt\", \"Set1\", \"Set2\", \"Gm1\", \"Gm2\", \"Svr\", \"Ret\", \"rallyCount\", \"PtWinner\", \"isSvrWinner\"]
    for col in int_cols:
        if col in df_points.columns:
            # Special case for TB? which might have 'S'
            if col == \"TB?\":
                df_points[col] = df_points[col].astype(str).str.replace(\"S\", \"2\", case=False)
            df_points[col] = pd.to_numeric(df_points[col], errors='coerce').astype('Int32')

    # Month conversion logic
    month_to_num = {\"jan\":\"1\", \"feb\":\"2\", \"mar\":\"3\", \"apr\":\"4\", \"may\":\"5\", \"jun\":\"6\", 
                    \"jul\":\"7\", \"aug\":\"8\", \"sep\":\"9\", \"oct\":\"10\", \"nov\":\"11\", \"dec\":\"12\"}
    
    # Process 'Pts' column (handling Excel's auto-date conversion)
    if 'Pts' in df_points.columns:
        def fix_pts_score(row):
            pts = str(row['Pts']).lower()
            for m_name, m_num in month_to_num.items():
                if m_name in pts:
                    score = pts.split(\"-\")
                    if len(score) == 2:
                        # If month is second, it's likely flipped (e.g. 2-Mar instead of 3-2)
                        if m_name in score[1]:
                            return f\"{m_name}-{score[0]}\".replace(m_name, m_num)
                    return pts.replace(m_name, m_num)
            return pts.replace(\"00\", \"0\")
        
        df_points['Pts'] = df_points.apply(fix_pts_score, axis=1)

    return df_points

# --- Main Execution Example ---

def main():
    # PATH FIX: Use local results folder
    output_dir = \"../biases-in-probabilistic-reasoning/results\"
    if not os.path.exists(output_dir):
        output_dir = \"./results\" # Fallback
        os.makedirs(output_dir, exist_ok=True)

    print(f\"Results will be saved to: {os.path.abspath(output_dir)}\")
    print(\"\\nUsage Note: This script contains the logic fixes for your notebook.\")
    print(\"You can import these functions into your notebook or run this standalone.\")

if __name__ == \"__main__\":
    main()
