import pandas as pd
from paths import RAW_DATA_DIR, TRANSFORMED_DATA_DIR

def load_transfermarkt_data(files):
    """Load and concatenate Transfermarkt league data."""
    return pd.concat([pd.read_csv(RAW_DATA_DIR / file) for file in files], ignore_index=True)

def clean_transfermarkt_data(df):
    """Clean Transfermarkt data by normalizing and converting the value column."""
    return (
        df
        # Eliminate rows with missing 'value'
        .dropna(subset=['value'])
        # Clean and convert 'value' column
        .assign(
            value=lambda df: df['value']
            .str.replace('€', '', regex=False)  # Remove euro symbol
            .str.replace('k', 'e3', regex=False)  # Replace 'k' with 'e3' (scientific notation)
            .str.replace('m', 'e6', regex=False)  # Replace 'm' with 'e6' (scientific notation)
            .map(pd.eval)  # Evaluate to numeric
            .apply(lambda x: int(x) if x.is_integer() else x)  # Convert integers to int type
        )
        # Normalize player names for consistent merging
        .assign(name_normalized=lambda df: df['name'].str.lower().str.strip())
    )

def load_fbref_data(file_path):
    """Load FBRef combined league data."""
    return pd.read_csv(file_path)

def merge_datasets(df_fbref, df_transfermarkt):
    """Merge FBRef and Transfermarkt datasets."""
    return (
        df_fbref
        # Normalize player names for consistent merging
        .assign(player_normalized=lambda df: df['player'].str.lower().str.strip())
        .merge(
            df_transfermarkt[['name_normalized', 'value']],
            left_on='player_normalized',
            right_on='name_normalized',
            how='left'
        )
        # Drop auxiliary normalized columns
        .drop(columns=['player_normalized', 'name_normalized'])
        # Replace NaN values in 'value' column with 0
        .assign(value=lambda df: df['value'].fillna(0))
    )

def save_dataset(df, file_path):
    """Save the final cleaned dataset."""
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    # Transfermarkt file list
    transfermarkt_files = [
        'championship_league_updated_data.csv'
        #'league_one_team_updated_data.csv',
        #'league_two_team_updated_data.csv'
    ]

    # Load data
    df_transfermarkt = load_transfermarkt_data(transfermarkt_files)
    df_cleaned_transfermarkt = clean_transfermarkt_data(df_transfermarkt)
    df_fbref = load_fbref_data(TRANSFORMED_DATA_DIR / 'df_championship_league_cleaned.csv')

    # Merge datasets
    df_training = merge_datasets(df_fbref, df_cleaned_transfermarkt)

    # Save final dataset
    save_dataset(df_training, TRANSFORMED_DATA_DIR / 'df_training_championship.csv')
    print(f"Dataset saved to {TRANSFORMED_DATA_DIR / 'df_training_championship.csv'}")
