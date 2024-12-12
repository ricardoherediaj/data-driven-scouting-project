# ⚽️📊 Data-Driven Scouting Project

Full-cycle data scouting project that aims to identify top 5 midfielders and top 5 forwards using Championship, League One and League Two players data for a hypothetical signing for Sheffield United. 

The project leverages the use of the following pipelines and modules:

-  ETL pipelines using web scraping to obtain football metrics and information pertaining players transfers from English tier 2, 3 and 4 leagues.
- Feature Engineering pipeline to preprocess the information from FBRef and Transfermarkt, cleanses it, and create football metrics for training.
- Training pipeline using unsupervised machine learning to identify the players. 
- Frontend application built with Streamlit to visualize the scouted players with radar charts that display their main performant metrics. 


## App Demo

Try the live app on Streamlit Cloud.

URL: https://data-driven-scouting.streamlit.app

## Setup and usage

You should have installed Python 3.12.2


### Clone the repository

```
git clone https://github.com/ricardoherediaj/data-driven-scouting-project.git
cd data-driven-scouting-project
```
### Create the environment

```
conda env create -f environment.yml
conda activate scouting_project
```

### Run the app

```
streamlit run src/app.py
```

## Project Structure

```
├── README.md
├── assets
│   ├── Alexander Robertson_radar_chart.png
│   ├── Ante Crnac_radar_chart.png
│   ├── Emiliano Marcondes_radar_chart.png
│   ├── Isaiah Jones_radar_chart.png
│   ├── Jaidon Anthony_radar_chart.png
│   ├── Josh Laurent_radar_chart.png
│   ├── Josh Murphy_radar_chart.png
│   ├── Rami Al Hajj_radar_chart.png
│   ├── Ryan Hedges_radar_chart.png
│   ├── Victor Torp_radar_chart.png
│   └── categories.json
├── data
│   ├── cache
│   ├── labeled_results
│   │   ├── df_training_scaled_labeled.csv
│   │   └── df_training_unscaled_labeled.csv
│   ├── raw
│   │   ├── championship_team_updated_data.csv
│   │   ├── league_one_team_updated_data.csv
│   │   └── league_two_team_updated_data.csv
│   └── transformed
│       ├── df_championship_transformed.csv
│       ├── df_combined_fbref_leagues.csv
│       ├── df_combined_leagues.csv
│       ├── df_fbref_transfermarkt_transformed.csv
│       ├── df_league_one_transformed.csv
│       ├── df_league_two_transformed.csv
│       ├── df_training.csv
│       ├── merged_dataframe_championship.csv
│       ├── merged_dataframe_league_one.csv
│       └── merged_dataframe_league_two.csv
├── environment.yml
├── models
│   └── kmeans_model_3_clusters_updated.pkl
└── src
    ├── __pycache__
    │   ├── constants.cpython-312.pyc
    │   ├── fbref_data_scraper.cpython-312.pyc
    │   ├── parsers.cpython-312.pyc
    │   ├── paths.cpython-312.pyc
    │   ├── transfermarkt_data_scraper.cpython-312.pyc
    │   └── utils.cpython-312.pyc
    ├── app.py
    ├── constants.py
    ├── fbref_data_cleaning_pipeline.py
    ├── fbref_data_scraper.py
    ├── fbref_transfermarkt_merge.py
    ├── kmeans_pipeline.py
    ├── main_fbref.py
    ├── main_transfermarkt.py
    ├── parsers.py
    ├── paths.py
    ├── radar_chart.py
    ├── transfermarkt_data_scraper.py
    ├── unsupervised_modeling.py
    └── utils.py         
```

## Disclaimer

The scrapers were functional at the time of development. However, due to potential changes in the HTML or CSS structure of League Two tables on the FBRef side, these tables are currently not being scraped correctly (Playing Time and Miscellaneous). 

This issue will be addressed in future updates to ensure compatibility of the pipelines workflow.

For the purposes of the Streamlit demo, the app was built using data collected up until match day 19 from the Championship (previously on the three leagues), which was enough to demonstrate the end-to-end functionality of the project. 

## Roadmap 

There are some improvements in the mid-long term that aims to enhance the project's scalability: 

- Focus on using data from players from the Championship rather than League One or Two. Still, I'll try to solve the scraping issue. 
- Create an automated pipeline to obtain events data from WhoScored and create relevant plots for the shortlisted players such as heat maps, pass maps and shooting maps.
- Build automated reports using these plots and the radar charts, adding a brief description of the scouted player.
- Use GitHub Actions to automate scripts (data pipelines, model training, charts generation).
- Reimplement the project with Metaflow for a smoother data flow.

## Contact

You can always find me at:

- LinkedIn: https://www.linkedin.com/in/ricardo-heredia-9b97b0181/

- Medium: https://ricardoheredia94.medium.com

- X/Twitter: @thenetpass / https://x.com/thenetpass?lang=es

- Bluesky: @thenetpass.bsky.social

## Contributing

Contributions are welcome! If you find an issue or have suggestions, feel free to open an issue, submit a pull request or get in contact with me.

## Authors and acknowledgment

I'd like to mention a couple or persons who inspired me to give it a try to this project: 

- Pol Marin, who's project made me want to replicate the clustering idea and extend his approach: https://towardsdatascience.com/using-clustering-algorithms-for-player-recruitment-98208d3a6cb4

- Conal Henderson who did a great job automating the Transfermarkt scraping for the Premier League, it helped replicate it for the other three leagues. Check it out in this article: https://medium.com/@conalhenderson/how-to-build-a-custom-web-scraper-to-extract-premier-league-player-market-data-3b8e5378cca2

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Project status

Ongoing development