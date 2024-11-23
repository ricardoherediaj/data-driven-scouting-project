import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.cm as cm
from sklearn.preprocessing import StandardScaler

# Function to load data from pickle or CSV files
def load_data(ruta_cat: str = None, ruta_num: str = None, ruta_df: str = None) -> tuple:
    """
    Load files in pickle or CSV format for categorical, numerical, or general data.
    
    Parameters:
    - ruta_cat (str, optional): Path to the categorical file in pickle or CSV format.
    - ruta_num (str, optional): Path to the numerical file in pickle or CSV format.
    - ruta_df (str, optional): Path to a general file in pickle or CSV format.
    
    Returns:
    tuple: Loaded DataFrames. Returns None if no path is specified.
    """
    cat, num, df_general = None, None, None

    # Load categorical data if path is provided
    if ruta_cat is not None:
        ruta_cat = str(ruta_cat)  # Convert path to string
        if ruta_cat.endswith('.pkl'):
            cat = pd.read_pickle(ruta_cat)
        elif ruta_cat.endswith('.csv'):
            cat = pd.read_csv(ruta_cat)
        else:
            print(f"Unsupported file format for 'ruta_cat': {ruta_cat}")

    # Load numerical data if path is provided
    if ruta_num is not None:
        ruta_num = str(ruta_num)  # Convert path to string
        if ruta_num.endswith('.pkl'):
            num = pd.read_pickle(ruta_num)
        elif ruta_num.endswith('.csv'):
            num = pd.read_csv(ruta_num)
        else:
            print(f"Unsupported file format for 'ruta_num': {ruta_num}")

    # Load general data if path is provided
    if ruta_df is not None:
        ruta_df = str(ruta_df)  # Convert path to string
        if ruta_df.endswith('.pkl'):
            df_general = pd.read_pickle(ruta_df)
        elif ruta_df.endswith('.csv'):
            df_general = pd.read_csv(ruta_df)
        else:
            print(f"Unsupported file format for 'ruta_df': {ruta_df}")
    
    return cat, num, df_general

# Function to scale variables using StandardScaler
def scale_variables(df, variables_to_scale):
    scaler = StandardScaler()
    df_scaled = pd.DataFrame(
        scaler.fit_transform(df[variables_to_scale]), 
        columns=variables_to_scale
    )
    return df_scaled, scaler

# Function to evaluate K-Means and obtain metrics
def evaluate_kmeans(df, solutions, random_state=42, n_init=10):
    """
    Evaluates multiple KMeans models with different numbers of clusters and returns metrics for each solution.

    Parameters:
    - df (pd.DataFrame): DataFrame with the data to use.
    - solutions (list): List of cluster numbers to try.
    - random_state (int): Seed for reproducibility.
    - n_init (int): Number of initializations.

    Returns:
    - pd.DataFrame: DataFrame with calculated metrics for each number of clusters.
    """
    elbow, silhouette, calins, davies = [], [], [], [] 

    for solution in solutions:
        cluster = KMeans(random_state=random_state, n_clusters=solution, n_init=n_init)
        cluster.fit(df)
        elbow.append(cluster.inertia_)
        silhouette.append(silhouette_score(df, cluster.labels_))
        calins.append(calinski_harabasz_score(df, cluster.labels_))
        davies.append(davies_bouldin_score(df, cluster.labels_))
    
    metrics = pd.DataFrame({
        'Solution': solutions,
        'Elbow': elbow,
        'Silhouette': silhouette,
        'Calinski-Harabasz': calins,
        'Davies-Bouldin': davies
    }).set_index('Solution')
    
    # Plot metrics
    metrics.plot(subplots=True, figsize=(12, 8), layout=(2, 2), sharex=False)
    plt.show()

    return metrics

# Function to train and save KMeans
def train_save_kmeans(df, n_clusters, save_path, random_state=42, n_init=10):
    """
    Trains a KMeans model with the specified number of clusters and saves the model to the provided path.

    Parameters:
    - df (pd.DataFrame): DataFrame with the data to use.
    - n_clusters (int): Number of clusters for the KMeans model.
    - save_path (str): Path where the trained model will be saved.
    - random_state (int): Seed for reproducibility.
    - n_init (int): Number of initializations.

    Returns:
    - KMeans: Trained KMeans model.
    """
    # Train the model with the specified number of clusters
    cluster_model = KMeans(n_clusters=n_clusters, n_init=n_init, random_state=random_state)
    cluster_model.fit(df)

    # Save the model to the specified path
    joblib.dump(cluster_model, save_path)
    print(f'KMeans model with {n_clusters} clusters saved to: {save_path}')

    return cluster_model

# Function to assign clusters to DataFrame
def assign_clusters(df, cluster):
    df['cluster'] = cluster.predict(df)
    return df

# Function to save the DataFrame with assigned clusters
def save_dataframe(df, save_path):
    df.to_csv(save_path, index=False)
    
# Function to visualize clusters using PCA and KDE
def plot_clusters_pca_kde(df, model, n_clusters=4, sample_size=200):
    df_features = df.drop(columns=['cluster'], errors='ignore')
    pca = PCA(n_components=2)
    pca_df = pd.DataFrame(pca.fit_transform(df_features), columns=['PC1', 'PC2'])
    pca_df['cluster'] = model.labels_
    
    colors = ['red', 'blue', 'green', 'gold']
    plt.figure(figsize=(10, 8))

    for i in range(n_clusters):
        cluster_data = pca_df[pca_df['cluster'] == i]
        
        # Adjust sample size if the cluster has fewer points than sample_size
        current_sample_size = min(sample_size, len(cluster_data))
        
        if current_sample_size > 0:
            cluster_data_sample = cluster_data.sample(n=current_sample_size, random_state=42)
            sns.kdeplot(x=cluster_data_sample['PC1'], y=cluster_data_sample['PC2'], 
                        color=colors[i], fill=True, alpha=0.3, linewidth=1.5)
            plt.scatter(cluster_data_sample['PC1'], cluster_data_sample['PC2'], color=colors[i], label=f'Cluster {i+1}', s=40)

    centroids_pca = pca.transform(model.cluster_centers_)
    plt.scatter(centroids_pca[:, 0], centroids_pca[:, 1], s=200, c='black', marker='x', label='Centroids')
    plt.title('Visualization of BRFSS clusters with PCA')
    plt.legend()
    plt.grid(True)
    plt.show()
    
# Function to visualize t-SNE    
def plot_tsne(df, n_clusters=4, colors=['red', 'blue', 'green', 'gold'], perplexity=30, n_iter=1000, random_state=42):
    """
    Applies t-SNE to the complete DataFrame and visualizes clusters in 2D.
    
    Parameters:
    - df: DataFrame with features and the cluster column.
    - n_clusters: Number of clusters present in the data (default is 4).
    - colors: List of colors for each cluster (default is ['red', 'blue', 'green', 'gold']).
    - perplexity: t-SNE parameter to adjust the number of neighbors considered (default is 30).
    - n_iter: Number of iterations for t-SNE (default is 1000).
    - random_state: Seed for reproducibility (default is 42).
    
    Returns:
    - None (shows the plot).
    """
    # Extract features and cluster labels
    X = df.drop(columns='cluster', errors='ignore')
    clusters = df['cluster']
    
    # Apply t-SNE
    tsne = TSNE(n_components=2, random_state=random_state, perplexity=perplexity, n_iter=n_iter)
    X_tsne = tsne.fit_transform(X)

    plt.figure(figsize=(8, 6))

    # Assign color and label to each cluster
    for i in range(n_clusters):
        cluster_data = X_tsne[clusters == i]
        plt.scatter(cluster_data[:, 0], cluster_data[:, 1], s=50, color=colors[i], label=f'Cluster {i+1}')

    plt.title('t-SNE Cluster Visualization')
    plt.xlabel('Component 1')
    plt.ylabel('Component 2')

    # Place the legend outside the plot, on the right
    plt.legend(title='Clusters', bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.tight_layout()
    plt.show();
