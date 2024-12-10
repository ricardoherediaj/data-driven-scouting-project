import sys
import logging
from pathlib import Path
import pandas as pd
from unsupervised_modeling import scale_variables, evaluate_kmeans, train_save_kmeans, assign_clusters
from paths import TRANSFORMED_DATA_DIR, MODELS_DIR
from constants import VARIABLES_TO_SCALE

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("kmeans_pipeline_championship_data.log"),
        logging.StreamHandler()
    ]
)

# Main function to execute the K-Means pipeline
def main():
    # Define paths
    input_path = TRANSFORMED_DATA_DIR / 'df_training_championship.csv'
    model_save_path = MODELS_DIR / 'kmeans_model_updated_championship_data.pkl'
    labeled_results_path = TRANSFORMED_DATA_DIR / 'df_training_championship_scaled_labeled.csv'
    unscaled_results_path = TRANSFORMED_DATA_DIR / 'df_training_championship_unscaled_labeled.csv'

    try:
        # Step 1: Load dataset
        logging.info("Loading dataset...")
        df_training = pd.read_csv(input_path)
        logging.info(f"Dataset loaded successfully with shape: {df_training.shape}")

        # Step 2: Prepare data for K-Means
        logging.info("Preparing data for K-Means...")
        df_training_kmeans = df_training[VARIABLES_TO_SCALE]
        df_training_scaled, scaler = scale_variables(df_training_kmeans, VARIABLES_TO_SCALE)
        logging.info("Data scaled successfully.")

        # Step 3: Evaluate potential solutions
        logging.info("Evaluating K-Means solutions...")
        solutions = list(range(3, 7))
        metrics = evaluate_kmeans(df_training_scaled, solutions)
        logging.info(f"K-Means evaluation metrics:\n{metrics}")

        # Step 4: Train and save the K-Means model
        n_clusters = 3
        logging.info(f"Training K-Means with {n_clusters} clusters...")
        kmeans_model = train_save_kmeans(df_training_scaled, n_clusters, model_save_path)
        logging.info(f"K-Means model saved to {model_save_path}")

        # Step 5: Assign clusters to the DataFrame
        logging.info("Assigning clusters to data...")
        df_with_clusters = assign_clusters(df_training_scaled, kmeans_model)

        # Save the labeled scaled dataset
        logging.info(f"Saving scaled dataset with clusters to {labeled_results_path}...")
        df_with_clusters.to_csv(labeled_results_path, index=False)

        # Step 6: Add clusters to the original dataset
        logging.info("Adding clusters to the original dataset...")
        df_training['cluster'] = df_with_clusters['cluster']

        # Save the labeled original dataset
        logging.info(f"Saving original dataset with clusters to {unscaled_results_path}...")
        df_training.to_csv(unscaled_results_path, index=False)

        logging.info("K-Means pipeline completed successfully!")

    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)

# Entry point for the script
if __name__ == "__main__":
    main()