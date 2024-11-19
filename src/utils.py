# utils.py

import httpx
from bs4 import BeautifulSoup
from typing import List
from dataclasses import dataclass
import logging

# Define team strcuture
@dataclass
class Team:
    id: str
    name: str

def get_teams_from_league(league_url: str) -> List[Team]:
    """
    Obtains Transfermarkt teams from a league.
    """
    logging.info(f"Fetching teams from: {league_url}")
    
    try:
        response = httpx.get(
            league_url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=60
        )
        response.raise_for_status()
    except httpx.HTTPError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise e

    soup = BeautifulSoup(response.content, "html.parser")
    team_info = soup.find_all("td", {"class": "hauptlink no-border-links"})
    
    # Extraer nombres e IDs de los equipos
    team_names = [td.find("a").get("href").split("/")[1] if td.find("a") else None for td in team_info]
    team_ids = [td.find("a").get("href").split("/")[4] if td.find("a") else None for td in team_info]
    
    return [Team(id=id, name=name) for name, id in zip(team_names, team_ids)]

def save_dataframe_to_csv(df, output_path: str) -> None:
    """
    Saves DataFrame to CSV.
    """
    try:
        df.to_csv(output_path, index=False)
        logging.info(f"Data saved to {output_path}")
    except Exception as e:
        logging.error(f"Error saving data: {e}")
        raise e