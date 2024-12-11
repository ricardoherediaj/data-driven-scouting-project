import json
import pandas as pd
from mplsoccer import Radar, grid, FontManager
import matplotlib.pyplot as plt
from paths import *

# ---------------- FONT MANAGER ----------------
# URLs for fonts
FONT_URLS = {
    'serif_regular': 'https://raw.githubusercontent.com/googlefonts/SourceSerifProGFVersion/main/fonts/SourceSerifPro-Regular.ttf',
    'serif_extra_light': 'https://raw.githubusercontent.com/googlefonts/SourceSerifProGFVersion/main/fonts/SourceSerifPro-ExtraLight.ttf',
    'rubik_regular': 'https://raw.githubusercontent.com/google/fonts/main/ofl/rubikmonoone/RubikMonoOne-Regular.ttf',
    'robotto_thin': 'https://raw.githubusercontent.com/googlefonts/roboto/main/src/hinted/Roboto-Thin.ttf',
    'robotto_bold': 'https://raw.githubusercontent.com/google/fonts/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf'
}

def load_fonts():
    """
    Load fonts using mplsoccer's FontManager.
    """
    fonts = {
        name: FontManager(url)
        for name, url in FONT_URLS.items()
    }
    return fonts

# ---------------- CONSTANTS ----------------
METRIC_NAMES_MAP = {
    'total_cmp%_stats_passing_per_90': 'Total % Pass Comp.',
    'ppa_stats_passing_per_90': 'PPA Passes',
    'sca_sca_stats_gca_per_90': 'SCA',
    'gca_gca_stats_gca_per_90': 'GCA',
    'touches_mid_3rd_stats_possession_per_90': 'Mid 3rd Touches',
    'touches_att_3rd_stats_possession_per_90': 'Att 3rd Touches',
    'receiving_prgr_stats_possession_per_90': 'Progressive Rec.',
    'tackles_mid_3rd_stats_defense_per_90': 'Mid 3rd Tackles',
    'aerial_duels_won%_stats_misc_per_90': 'Aerial Duels Won %',
    'tackles_tkl_stats_defense_per_90': 'Tackles',
    'int_stats_defense_per_90': 'Interceptions',
    'performance_recov_stats_misc_per_90': 'Recoveries',
    'ast_stats_passing_per_90': 'Assists',
    'standard_gls_stats_shooting_per_90': 'Goals',
    'standard_sot%_stats_shooting_per_90': 'Shots on Target %',
    'take_ons_succ_stats_possession_per_90': 'Successful Take-Ons',
    'carries_prgc_stats_possession_per_90': 'Progressive Carries',
    'performance_crs_stats_misc_per_90': 'Crosses'
}

# ---------------- FUNCTIONS ----------------
def calculate_percentiles_by_position(df, metrics, position):
    df = df.copy()
    df = df[df['position_stats_standard'] == position]
    for metric in metrics:
        df.loc[:, f'{metric}_percentile'] = df[metric].rank(pct=True) * 100
    return df

def select_top_5_players(df, metrics):
    df = df.copy()
    percentile_columns = [f'{metric}_percentile' for metric in metrics]
    df['average_percentile'] = df[percentile_columns].mean(axis=1)
    return df.nlargest(5, 'average_percentile')[
        ['player', 'squad', 'position_stats_standard', 'value', 'average_percentile'] + percentile_columns
    ]

def generate_custom_radar_chart(player_df, metrics, renamed_metrics, player_name, squad, position, fonts):
    font_bold = fonts['robotto_bold']
    font_thin = fonts['robotto_thin']

    player_data = player_df[player_df['player'] == player_name].iloc[0]

    radar = Radar(
        params=renamed_metrics,
        min_range=[0] * len(metrics),
        max_range=[100] * len(metrics)
    )
    values = [player_data[f'{metric}_percentile'] for metric in metrics]

    fig, axs = grid(figheight=14, grid_height=0.915, title_height=0.06, endnote_height=0.025,
                    title_space=0, endnote_space=0, grid_key='radar', axis=False)

    radar.setup_axis(ax=axs['radar'], facecolor='None')
    radar.draw_circles(ax=axs['radar'], facecolor='#28252c', edgecolor='#39353f', lw=1.5)
    radar.draw_radar(values, ax=axs['radar'],
                     kwargs_radar={'facecolor': '#d0667a', 'alpha': 0.6},
                     kwargs_rings={'facecolor': '#1d537f', 'alpha': 0.3})
    radar.draw_range_labels(ax=axs['radar'], fontsize=15, color='#fcfcfc', fontproperties=font_thin.prop)
    radar.draw_param_labels(ax=axs['radar'], fontsize=15, color='#fcfcfc', fontproperties=font_thin.prop)

    axs['title'].text(0.01, 0.65, player_name, fontsize=25, fontproperties=font_bold.prop,
                      ha='left', va='center', color='#e4dded')
    axs['title'].text(0.01, 0.25, squad, fontsize=20, fontproperties=font_thin.prop,
                      ha='left', va='center', color='#cc2a3f')
    axs['title'].text(0.99, 0.65, 'Radar Chart', fontsize=25, fontproperties=font_bold.prop,
                      ha='right', va='center', color='#e4dded')
    axs['title'].text(0.99, 0.25, position, fontsize=20, fontproperties=font_thin.prop,
                      ha='right', va='center', color='#cc2a3f')
    axs['endnote'].text(0.99, 0.5, 'Created by: Ricardo Heredia @thenetpass / Inspired By: StatsBomb / Rami Moghadam',
                        fontsize=15, fontproperties=font_thin.prop,
                        ha='right', va='center', color='#fcfcfc')

    fig.set_facecolor('#121212')
    return fig

# ---------------- EXECUTION EXAMPLE ----------------
if __name__ == "__main__":
    path = LABELED_DATA_DIR / 'df_training_championship_unscaled_labeled.csv'
    df = pd.read_csv(path)

    # Drop unnecessary columns
    columns_to_drop = ['playing_time_min_stats_playing_time'] #'nation_stats_standard', 'playing_time_90s'
    df_cleaned = df.drop(columns=columns_to_drop)

    # Load fonts
    fonts = load_fonts()

    # Metrics for midfielders and forwards
    metrics_midfielders = [
        'total_cmp%_stats_passing_per_90', 'ppa_stats_passing_per_90', 
        'sca_sca_stats_gca_per_90', 'touches_mid_3rd_stats_possession_per_90', 
        'touches_att_3rd_stats_possession_per_90', 'receiving_prgr_stats_possession_per_90', 
        'tackles_mid_3rd_stats_defense_per_90', 'aerial_duels_won%_stats_misc_per_90', 
        'tackles_tkl_stats_defense_per_90', 'int_stats_defense_per_90', 
        'performance_recov_stats_misc_per_90'
    ]
    renamed_metrics_midfielders = [METRIC_NAMES_MAP[metric] for metric in metrics_midfielders]

    metrics_forwards = [
        'total_cmp%_stats_passing_per_90', 'ast_stats_passing_per_90', 
        'ppa_stats_passing_per_90', 'standard_gls_stats_shooting_per_90', 
        'standard_sot%_stats_shooting_per_90', 'sca_sca_stats_gca_per_90', 
        'gca_gca_stats_gca_per_90', 'touches_mid_3rd_stats_possession_per_90', 
        'touches_att_3rd_stats_possession_per_90', 'take_ons_succ_stats_possession_per_90', 
        'carries_prgc_stats_possession_per_90', 'receiving_prgr_stats_possession_per_90', 
        'tackles_mid_3rd_stats_defense_per_90','aerial_duels_won%_stats_misc_per_90',
        'performance_recov_stats_misc_per_90','performance_crs_stats_misc_per_90'
    ]
    renamed_metrics_forwards = [METRIC_NAMES_MAP[metric] for metric in metrics_forwards]

    # Calculate percentiles
    midfielders_percentiles = calculate_percentiles_by_position(
        df_cleaned[df_cleaned['cluster'] == 0], metrics_midfielders, 'Midfielder'
    )
    forwards_percentiles = calculate_percentiles_by_position(
        df_cleaned[df_cleaned['cluster'] == 2], metrics_forwards, 'Forward'
    )

    # Select top 5 players
    top_5_midfielders = select_top_5_players(midfielders_percentiles, metrics_midfielders)
    top_5_forwards = select_top_5_players(forwards_percentiles, metrics_forwards)

    # Save categories
    player_categories = {}

    # Generate radar charts for midfielders
    for _, row in top_5_midfielders.iterrows():
        player_name = row['player']
        output_path = ASSETS_DIR / f"{player_name}_radar_chart.png"
        fig = generate_custom_radar_chart(
            midfielders_percentiles,
            metrics_midfielders,
            renamed_metrics_midfielders,
            player_name,
            row['squad'],
            row['position_stats_standard'],
            fonts
        )
        fig.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
        plt.close(fig)

        # Register player as "Midfielder"
        player_categories[player_name] = "Midfielder"

    # Generate radar charts for forwards
    for _, row in top_5_forwards.iterrows():
        player_name = row['player']
        output_path = ASSETS_DIR / f"{player_name}_radar_chart.png"
        fig = generate_custom_radar_chart(
            forwards_percentiles,
            metrics_forwards,
            renamed_metrics_forwards,
            player_name,
            row['squad'],
            row['position_stats_standard'],
            fonts
        )
        fig.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
        plt.close(fig)

        # Register player as "Forward"
        player_categories[player_name] = "Forward"

    # Save in JSON file
    categories_path = ASSETS_DIR / "categories.json"
    with open(categories_path, 'w') as f:
        json.dump(player_categories, f, indent=4)