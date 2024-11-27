# fbref_data_cleaning_pipeline.py

import pandas as pd
from paths import TRANSFORMED_DATA_DIR
from constants import METRICS, COLUMNS_TO_NORMALIZE  # Import global configurations


def clean_dataset(file_path, columns_to_normalize, metrics, filter_positions=None, exclude_team=None):
    """
    Cleans and transforms the dataset from the given file path.

    Args:
        file_path (str): Path to the CSV file to clean.
        columns_to_normalize (list): List of columns to normalize per 90 minutes.
        metrics (list): List of relevant columns to retain in the final dataset.
        filter_positions (list, optional): Positions to keep (e.g., 'Midfielder', 'Forward').
        exclude_team (str, optional): Team to exclude from the dataset.

    Returns:
        pd.DataFrame: Cleaned and transformed dataset.
    """
    df = pd.read_csv(file_path)
    
    df_cleaned = (
        df
        # Drop unnecessary column
        .drop(columns=['position_2_stats_standard'], errors='ignore')
        # Remove rows with missing player names
        .dropna(subset=['player'])
        # Convert relevant columns to numeric
        .assign(
            playing_time_min_stats_playing_time=pd.to_numeric(
                df['playing_time_min_stats_playing_time'], errors='coerce'
            ),
            **{col: pd.to_numeric(df[col], errors='coerce') for col in columns_to_normalize}
        )
        # Remove players with less than 400 minutes or defenders
        .loc[lambda df: (df['playing_time_min_stats_playing_time'] > 400)]
        .pipe(lambda df: df if filter_positions is None else df[df['position_stats_standard'].isin(filter_positions)])
        # Exclude specified team if provided
        .pipe(lambda df: df if exclude_team is None else df[df['squad'] != exclude_team])
        # Fill missing values in 'nation_stats_standard'
        .assign(nation_stats_standard=lambda df: df['nation_stats_standard'].fillna('ENG'))
        # Add column for per-90-minute normalization
        .assign(playing_time_90s=lambda df: df['playing_time_min_stats_playing_time'] / 90)
        # Normalize columns per 90 minutes
        .assign(
            **{f"{col}_per_90": lambda df, col=col: (df[col] / df['playing_time_90s']).fillna(0)
               for col in columns_to_normalize}
        )
        # Keep only relevant columns
        .filter(
            items=['player', 'nation_stats_standard', 'squad', 'age_stats_standard',
                   'position_stats_standard', 'playing_time_min_stats_playing_time',
                   'playing_time_90s'] + [f"{col}_per_90" for col in columns_to_normalize]
        )
    )
    return df_cleaned


def main():
    """
    Main function to clean datasets for Championship, League One, and League Two,
    and combine them into a single dataset.
    """
    # Define file paths for the datasets
    paths = {
        'championship': TRANSFORMED_DATA_DIR / 'merged_dataframe_championship.csv',
        'league_one': TRANSFORMED_DATA_DIR / 'merged_dataframe_league_one.csv',
        'league_two': TRANSFORMED_DATA_DIR / 'merged_dataframe_league_two.csv'
    }
    
    # Clean each league dataset
    df_championship_cleaned = clean_dataset(
        paths['championship'], 
        columns_to_normalize=COLUMNS_TO_NORMALIZE, 
        metrics=METRICS, 
        filter_positions=['Midfielder', 'Forward'], 
        exclude_team='Sheffield Utd'
    )
    df_league_one_cleaned = clean_dataset(
        paths['league_one'], 
        columns_to_normalize=[
            'standard_gls_stats_shooting', 'standard_sh_stats_shooting', 
            'standard_sot_stats_shooting', 'standard_sot%_stats_shooting',
            'standard_sh_90_stats_shooting', 'standard_sot_90_stats_shooting',
            'performance_off_stats_misc', 'performance_crs_stats_misc',
            'performance_int_stats_misc', 'performance_tklw_stats_misc'
        ], 
        metrics=[
            'player', 'nation_stats_standard', 'squad', 'age_stats_standard',
            'position_stats_standard', 'playing_time_min_stats_playing_time',
            'playing_time_90s_stats_playing_time'
        ] + [f"{col}_per_90" for col in [
            'standard_gls_stats_shooting', 'standard_sh_stats_shooting', 
            'standard_sot_stats_shooting', 'standard_sot%_stats_shooting',
            'standard_sh_90_stats_shooting', 'standard_sot_90_stats_shooting',
            'performance_off_stats_misc', 'performance_crs_stats_misc',
            'performance_int_stats_misc', 'performance_tklw_stats_misc'
        ]],
        filter_positions=['Midfielder', 'Forward']
    )
    df_league_two_cleaned = clean_dataset(
        paths['league_two'], 
        columns_to_normalize=[
            'standard_gls_stats_shooting', 'standard_sh_stats_shooting', 
            'standard_sot_stats_shooting', 'standard_sot%_stats_shooting',
            'standard_sh_90_stats_shooting', 'standard_sot_90_stats_shooting'
        ], 
        metrics=[
            'player', 'nation_stats_standard', 'squad', 'age_stats_standard',
            'position_stats_standard', 'playing_time_min_stats_playing_time',
            'playing_time_90s'
        ] + [f"{col}_per_90" for col in [
            'standard_gls_stats_shooting', 'standard_sh_stats_shooting', 
            'standard_sot_stats_shooting', 'standard_sot%_stats_shooting',
            'standard_sh_90_stats_shooting', 'standard_sot_90_stats_shooting'
        ]],
        filter_positions=['Midfielder', 'Forward']
    )

    # Combine cleaned datasets
    df_combined_fbref_leagues = (
        pd.concat([df_championship_cleaned, df_league_one_cleaned, df_league_two_cleaned], ignore_index=True)
        .reindex(columns=df_championship_cleaned.columns, fill_value=0)
        .fillna(0)
    )
    
    # Save combined dataset
    output_path = TRANSFORMED_DATA_DIR / "df_combined_fbref_leagues.csv"
    df_combined_fbref_leagues.to_csv(output_path, index=False)
    print(f"Combined dataset saved at: {output_path}")


if __name__ == "__main__":
    main()