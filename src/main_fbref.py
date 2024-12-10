# main_fbref.py

import sys
sys.path.append('../../src')
from fbref_data_scraper import scrape_league, save_dataframe

def main():
    leagues = ['championship'] #'league_one', 'league_two'
    
    for league in leagues:
        print(f"Scraping data for {league}...")
        merged_df = scrape_league(league)
        if not merged_df.empty:
            save_dataframe(merged_df, league)
        else:
            print(f"No data found for {league}. Skipping...")

if __name__ == "__main__":
    main()
