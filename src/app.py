import streamlit as st
import json
from pathlib import Path
from paths import *

# Page configuration
st.set_page_config(page_title="Football Radar Charts", layout="wide")
st.title("Scouted Players Radar Charts - Season 2024/2025")

# Load categories from the JSON file
categories_path = RADARS_DIR / "categories.json"
if categories_path.exists():
    with open(categories_path, 'r') as f:
        player_categories = json.load(f)
else:
    st.error("Categories file not found. Please generate radar charts first.")
    st.stop()

# Create dynamic lists of players by category
categories = {"Midfielder": [], "Forward": []}
for player, category in player_categories.items():
    if category in categories:
        categories[category].append(player)

# Dropdown to select a category
category = st.selectbox("Select position:", list(categories.keys()))

# Dropdown to select a player based on the chosen category
if categories[category]:
    player = st.selectbox("Select player:", categories[category])
else:
    st.warning(f"No players available for the selected category: {category}")
    st.stop()

# Display radar chart for the selected player
st.subheader(f"Radar Chart for {player}")

# Build the path for the radar chart image
image_path = RADARS_DIR / f"{player}_radar_chart.png"

if image_path.exists():
    st.image(image_path.as_posix(), caption=f"{player}'s Radar Chart", use_container_width=True)
else:
    st.error(f"Radar chart for {player} not found.")
