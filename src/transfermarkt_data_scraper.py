# transfermarkt_scraper.py
import logging
import time
import pandas as pd
import httpx
from bs4 import BeautifulSoup
from dataclasses import dataclass
from parsers import PlayerNames, PlayerAges, PlayerCountries, PlayerValues, PlayerPositions
from utils import get_teams_from_league
from typing import List

logging.basicConfig(level=logging.INFO)

@dataclass
class Team:
    id: str
    name: str

@dataclass
class Scraper:
    team: Team
    parsers: List
    year: int
    url: str = "https://www.transfermarkt.co.uk/{name}/kader/verein/{id}/saison_id/{year}/plus/1"
    
    def run(self) -> pd.DataFrame:
        url = self.url.format(name=self.team.name, id=self.team.id, year=self.year)
        logging.info(f"Scraping: {self.team.name} - {self.year}")
        soup = self._get_soup_content(url)
        data = pd.concat([parser.parse(soup) for parser in self.parsers], axis=1)
        data["season"] = self.year
        data['team'] = self.team.name
        return data

    def _get_soup_content(self, url: str) -> BeautifulSoup:
        resp = self._make_request(url)
        return BeautifulSoup(resp.content, "html.parser")

    def _make_request(self, url: str) -> httpx.Response:
        try:
            response = httpx.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=60)
            response.raise_for_status()
            return response
        except httpx.HTTPError as e:
            logging.error(f"HTTP error occurred: {e}")
            raise e

if __name__ == "__main__":
    from constants import championship_url, league_one_url, league_two_url
    championship_teams = get_teams_from_league(championship_url)
    scrape(championship_teams, "data/championship_updated_data.csv", 2024)
