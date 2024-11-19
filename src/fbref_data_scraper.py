# fbref_data_scraper.py

import requests
import pandas as pd
from janitor import clean_names
import io
import random
from paths import *
from constants import tables_info, columns_to_retain

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

def get_clean_table(url, table_id):
    """ Fetch and clean table from FBRef given a URL and table ID. """
    response = requests.get(url, headers=HEADERS)
    html = response.text.replace('<!--', '').replace('-->', '')

    try:
        # Wrap HTML content in StringIO to avoid FutureWarning
        html_io = io.StringIO(html)
        df = pd.read_html(html_io, attrs={'id': table_id})[0]
        df = clean_columns(df)
        df = df.fillna(0).reset_index(drop=True)
        print(f"Table '{table_id}' extracted successfully!")
        return df
    except (ValueError, IndexError):
        print(f"No tables found for table_id '{table_id}' in URL: {url}")
        return pd.DataFrame()


def clean_columns(df):
    """ Clean and flatten columns of a DataFrame. """
    df.columns = [' '.join(col).strip() if isinstance(col, tuple) else col for col in df.columns]
    new_columns = [col.split()[-1] if 'level_0' in col else col for col in df.columns]
    df.columns = new_columns
    return df


def process_dataframe(df):
    """ Apply additional processing to DataFrame. """
    if 'Age' in df.columns:
        df['Age'] = df['Age'].astype(str).str[:2]

    if 'Pos' in df.columns:
        df['Position_2'] = df['Pos'].astype(str).str[3:]
        df['Position'] = df['Pos'].astype(str).str[:2]

    if 'Nation' in df.columns:
        df['Nation'] = df['Nation'].astype(str).str.split(' ').str.get(1)

    df = df.drop(columns=['Rk', 'Matches'], errors='ignore')
    position_mapping = {'MF': 'Midfielder', 'DF': 'Defender', 'FW': 'Forward', 'GK': 'Goalkeeper'}
    df['Position'] = df['Position'].replace(position_mapping)
    df['Position_2'] = df['Position_2'].replace(position_mapping)
    
    return df


def merge_dataframes(dataframes_dict, columns_dict):
    """ Merge dataframes and retain specified columns. """
    filtered_dfs = []
    for key, df in dataframes_dict.items():
        if key in columns_dict:
            columns_to_retain = [col for col in columns_dict[key] if col in df.columns]
            df_filtered = df[columns_to_retain].copy()
            df_filtered.columns = [f"{col}_{key}" if col not in ['Player', 'Squad'] else col for col in df_filtered.columns]
            filtered_dfs.append(df_filtered)
    merged_df = pd.concat(filtered_dfs, axis=1).loc[:, ~pd.concat(filtered_dfs, axis=1).columns.duplicated()]
    return merged_df


def save_dataframe(df, league_name):
    """ Save merged dataframe to CSV. """
    save_path = TRANSFORMED_DATA_DIR / f"merged_dataframe_{league_name}.csv"
    df.to_csv(save_path, index=False)
    print(f"Data for {league_name} saved successfully at {save_path}")


def scrape_league(league):
    """ Perform scraping for a given league. """
    dataframes = {}
    for url, table_id in tables_info[league]:
        print(f"Scraping {url} for table_id '{table_id}'...")
        df = get_clean_table(url, table_id)
        if not df.empty:
            print(df.head())  
            df = process_dataframe(df)
            dataframes[table_id] = df
        else:
            print(f"Table '{table_id}' is empty for {league}. Skipping...")
    merged_df = merge_dataframes(dataframes, columns_to_retain[league])
    merged_df = clean_names(merged_df)
    return merged_df