import logging
import time
import pandas as pd
from transfermarkt_data_scraper import Scraper
from parsers import PlayerNames, PlayerAges, PlayerCountries, PlayerValues, PlayerPositions
from utils import get_teams_from_league, save_dataframe_to_csv
from constants import championship_url #league_one_url, league_two_url
from paths import RAW_DATA_DIR  

# Configure the logging
logging.basicConfig(level=logging.INFO)

# Define parsers 
parsers = [PlayerNames(), PlayerAges(), PlayerCountries(), PlayerValues(), PlayerPositions()]

def scrape_teams(teams, year, output_path):
    dataframes = []
    for team in teams:
        logging.info(f"Scraping data for team: {team.name}")
        scraper = Scraper(team=team, parsers=parsers, year=year)
        df = scraper.run()
        dataframes.append(df)
        time.sleep(5)  # Pause to avoid blockage from Transfermarkt

    # Concat al DataFrames and save them as CSVs
    if dataframes:
        final_df = pd.concat(dataframes, ignore_index=True)
        save_dataframe_to_csv(final_df, output_path)

if __name__ == "__main__":
    # Define year and saving path
    year = 2024
    championship_output_path = RAW_DATA_DIR / 'championship_league_updated_data.csv'
    # league_one_output_path = RAW_DATA_DIR / 'league_one_team_updated_data.csv'
    # league_two_output_path = RAW_DATA_DIR / 'league_two_team_updated_data.csv'

    # Scrape teams and leagues
    championship_teams = get_teams_from_league(championship_url)
    # league_one_teams = get_teams_from_league(league_one_url)
    # league_two_teams = get_teams_from_league(league_two_url)

    scrape_teams(championship_teams, year, championship_output_path)
    # scrape_teams(league_one_teams, year, league_one_output_path)
    # scrape_teams(league_two_teams, year, league_two_output_path)
