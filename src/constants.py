# constants.py

#========================# Transfermarkt & FBRef URLs #========================#
# Transfermarkt URLs
championship_url = "https://www.transfermarkt.co.uk/championship/startseite/wettbewerb/GB2/plus/?saison_id=2024"
# league_one_url = "https://www.transfermarkt.co.uk/league-one/startseite/wettbewerb/GB3/plus/?saison_id=2024"
# league_two_url = "https://www.transfermarkt.co.uk/league-two/startseite/wettbewerb/GB4/plus/?saison_id=2024"


# FBRef URLs and IDs dof tables for Championship, League One, and League Two
tables_info = {
    'championship': [
        ('https://fbref.com/en/comps/10/stats/Championship-Stats', 'stats_standard'),
        ('https://fbref.com/en/comps/10/shooting/Championship-Stats', 'stats_shooting'),
        ('https://fbref.com/en/comps/10/passing/Championship-Stats', 'stats_passing'),
        ('https://fbref.com/en/comps/10/passing_types/Championship-Stats', 'stats_passing_types'),
        ('https://fbref.com/en/comps/10/gca/Championship-Stats', 'stats_gca'),
        ('https://fbref.com/en/comps/10/defense/Championship-Stats', 'stats_defense'),
        ('https://fbref.com/en/comps/10/possession/Championship-Stats', 'stats_possession'),
        ('https://fbref.com/en/comps/10/playingtime/Championship-Stats', 'stats_playing_time'),
        ('https://fbref.com/en/comps/10/misc/Championship-Stats', 'stats_misc')
    ]
    # 'league_one': [
    #     ('https://fbref.com/en/comps/15/stats/League-One-Stats', 'stats_standard'),
    #     ('https://fbref.com/en/comps/15/shooting/League-One-Stats', 'stats_shooting'),
    #     ('https://fbref.com/en/comps/15/playingtime/League-One-Stats', 'stats_playing_time'),
    #     ('https://fbref.com/en/comps/15/misc/League-One-Stats', 'stats_misc')
    # ],
    # 'league_two': [
    #     ('https://fbref.com/en/comps/16/stats/League-Two-Stats', 'stats_standard'),
    #     ('https://fbref.com/en/comps/16/shooting/League-Two-Stats', 'stats_shooting'),
    #     ('https://fbref.com/en/comps/16/playingtime/League-Two-Stats', 'stats_playing_time'),
    #     ('https://fbref.com/en/comps/16/misc/League-Two-Stats', 'stats_misc')
    # ]
}

#========================# FBRef Columns to Scrape #========================#
# Columnas a extraer para Championship
columns_to_retain_championship = {
    'stats_standard': ['Player', 'Nation', 'Squad', 'Age', 'Born', 'Playing Time 90s', 'Position_2', 'Position'],
    'stats_passing_types': ['Player', 'Squad', 'Pass Types TB', 'Pass Types Sw', 'Pass Types Crs', 'Outcomes Cmp', 'Outcomes Blocks'],
    'stats_passing': ['Player', 'Squad', 'Total Cmp', 'Total Att', 'Total Cmp%', 'Short Cmp', 'Short Att', 'Short Cmp%',
                      'Medium Cmp', 'Medium Att', 'Medium Cmp%', 'Long Cmp', 'Long Att', 'Long Cmp%', 'Ast', '1/3', 'PPA', 'PrgP'],
    'stats_playing_time': ['Player', 'Squad', 'Playing Time 90s', 'Playing Time MP', 'Playing Time Min'],
    'stats_shooting': ['Player', 'Squad', 'Standard Gls', 'Standard Sh', 'Standard SoT', 'Standard SoT%', 'Standard Sh/90', 'Standard SoT/90'],
    'stats_gca': ['Player', 'Squad', 'SCA SCA', 'GCA GCA'],
    'stats_defense': ['Player', 'Squad', 'Tackles Tkl', 'Tackles TklW', 'Tackles Def 3rd', 'Tackles Mid 3rd',
                      'Tackles Att 3rd', 'Blocks Blocks', 'Blocks Sh', 'Blocks Pass', 'Int', 'Clr', 'Err'],
    'stats_possession': ['Player', 'Squad', 'Touches Touches', 'Touches Mid 3rd', 'Touches Att 3rd', 'Touches Att Pen',
                         'Take-Ons Att', 'Take-Ons Succ', 'Take-Ons Succ%', 'Carries Carries', 'Carries PrgC', 'Carries 1/3',
                         'Carries CPA', 'Carries Mis', 'Carries Dis', 'Receiving Rec', 'Receiving PrgR'],
    'stats_misc': ['Player', 'Squad', 'Performance Off', 'Performance Crs', 'Performance Int', 'Performance TklW',
                   'Performance Recov', 'Aerial Duels Won', 'Aerial Duels Lost', 'Aerial Duels Won%']
}

# Columnas a extraer para League One y League Two
# columns_to_retain_league_one_two = {
#     'stats_standard': ['Player', 'Nation', 'Squad', 'Age', 'Born', 'Playing Time 90s', 'Position_2', 'Position'],
#     'stats_playing_time': ['Player', 'Squad', 'Playing Time 90s', 'Playing Time MP', 'Playing Time Min'],
#     'stats_shooting': ['Player', 'Squad', 'Standard Gls', 'Standard Sh', 'Standard SoT', 'Standard SoT%', 'Standard Sh/90', 'Standard SoT/90'],
#     'stats_misc': ['Player', 'Squad', 'Performance Off', 'Performance Crs', 'Performance Int', 'Performance TklW',
#                    'Performance Recov', 'Aerial Duels Won', 'Aerial Duels Lost', 'Aerial Duels Won%']
# }

columns_to_retain = {
    'championship': columns_to_retain_championship,
    # 'league_one': columns_to_retain_league_one_two,
    # 'league_two': columns_to_retain_league_one_two
}

# Columns for Championship
FBREF_COLUMNS_CHAMPIONSHIP = [
    'player', 'nation_stats_standard', 'squad', 'age_stats_standard', 'born_stats_standard',
    'position_2_stats_standard', 'position_stats_standard', '90s_stats_shooting', 'standard_gls_stats_shooting',
    'standard_sh_stats_shooting', 'standard_sot_stats_shooting', '90s_stats_passing', 'total_cmp_stats_passing',
    'total_att_stats_passing', 'total_cmp%_stats_passing', 'short_cmp_stats_passing', 'short_att_stats_passing',
    'short_cmp%_stats_passing', 'medium_cmp_stats_passing', 'medium_att_stats_passing', 'medium_cmp%_stats_passing',
    'long_cmp_stats_passing', 'long_att_stats_passing', 'long_cmp%_stats_passing', 'ast_stats_passing',
    '1_3_stats_passing', 'ppa_stats_passing', 'prgp_stats_passing', '90s_stats_passing_types',
    'pass_types_tb_stats_passing_types', 'pass_types_sw_stats_passing_types', 'pass_types_crs_stats_passing_types',
    'outcomes_cmp_stats_passing_types', 'outcomes_blocks_stats_passing_types', '90s_stats_gca', 'sca_sca_stats_gca',
    'gca_gca_stats_gca', '90s_stats_defense', 'tackles_tkl_stats_defense', 'tackles_tklw_stats_defense',
    'tackles_def_3rd_stats_defense', 'tackles_mid_3rd_stats_defense', 'tackles_att_3rd_stats_defense',
    'blocks_blocks_stats_defense', 'blocks_sh_stats_defense', 'blocks_pass_stats_defense', 'int_stats_defense',
    'clr_stats_defense', 'err_stats_defense', '90s_stats_possession', 'touches_touches_stats_possession',
    'touches_mid_3rd_stats_possession', 'touches_att_3rd_stats_possession', 'touches_att_pen_stats_possession',
    'take_ons_att_stats_possession', 'take_ons_succ_stats_possession', 'carries_carries_stats_possession',
    'carries_prgc_stats_possession', 'carries_1_3_stats_possession', 'carries_cpa_stats_possession',
    'carries_mis_stats_possession', 'carries_dis_stats_possession', 'receiving_rec_stats_possession',
    'receiving_prgr_stats_possession', 'playing_time_90s_stats_playing_time', 'playing_time_mp_stats_playing_time',
    'playing_time_min_stats_playing_time', '90s_stats_misc', 'performance_off_stats_misc', 'performance_crs_stats_misc',
    'performance_int_stats_misc', 'performance_tklw_stats_misc', 'performance_recov_stats_misc',
    'aerial_duels_won_stats_misc', 'aerial_duels_lost_stats_misc', 'aerial_duels_won%_stats_misc'
]

# Columns for League One and League Two
# FBREF_COLUMNS_OTHER_LEAGUES = [
#     'player', 'nation_stats_standard', 'squad', 'age_stats_standard', 'born_stats_standard',
#     'playing_time_90s_stats_standard', 'position_2_stats_standard', 'position_stats_standard',
#     '90s_stats_shooting', 'standard_gls_stats_shooting', 'standard_sh_stats_shooting',
#     'standard_sot_stats_shooting', 'standard_sot%_stats_shooting', 'standard_sh_90_stats_shooting',
#     'standard_sot_90_stats_shooting', 'playing_time_90s_stats_playing_time',
#     'playing_time_mp_stats_playing_time', 'playing_time_min_stats_playing_time',
#     '90s_stats_misc', 'performance_off_stats_misc', 'performance_crs_stats_misc',
#     'performance_int_stats_misc', 'performance_tklw_stats_misc'
# ]

#========================# FBRef columns to clean on data cleaning script #========================#
# Relevant metrics to build dataframes
METRICS = [
    'player', 'nation_stats_standard', 'squad', 'age_stats_standard',
    'born_stats_standard', 'playing_time_90s_stats_standard',
    'position_stats_standard', 'playing_time_min_stats_playing_time',
    'total_cmp%_stats_passing', 'ast_stats_passing', 'ppa_stats_passing',
    'standard_gls_stats_shooting', 'standard_sot%_stats_shooting',
    'sca_sca_stats_gca', 'gca_gca_stats_gca', 'touches_mid_3rd_stats_possession',
    'touches_att_3rd_stats_possession', 'take_ons_succ_stats_possession',
    'carries_prgc_stats_possession', 'receiving_prgr_stats_possession',
    'tackles_mid_3rd_stats_defense', 'aerial_duels_won%_stats_misc',
    'performance_crs_stats_misc', 'tackles_tkl_stats_defense',
    'int_stats_defense', 'performance_recov_stats_misc'
]

# Columns for normalizing values per 90
COLUMNS_TO_NORMALIZE = [
    'total_cmp%_stats_passing', 'ast_stats_passing', 'ppa_stats_passing',
    'standard_gls_stats_shooting', 'standard_sot%_stats_shooting', 'sca_sca_stats_gca',
    'gca_gca_stats_gca', 'touches_mid_3rd_stats_possession', 'touches_att_3rd_stats_possession',
    'take_ons_succ_stats_possession', 'carries_prgc_stats_possession', 'receiving_prgr_stats_possession',
    'tackles_mid_3rd_stats_defense', 'aerial_duels_won%_stats_misc', 'performance_crs_stats_misc',
    'tackles_tkl_stats_defense', 'int_stats_defense', 'performance_recov_stats_misc'
]


#========================# KMeans Pipeline Script #========================#

# Variables to scale for K-Means clustering
VARIABLES_TO_SCALE = [
    'age_stats_standard', 
    'playing_time_min_stats_playing_time', 
    'value', 
    'total_cmp%_stats_passing_per_90', 
    'ast_stats_passing_per_90', 
    'ppa_stats_passing_per_90', 
    'standard_gls_stats_shooting_per_90', 
    'standard_sot%_stats_shooting_per_90', 
    'sca_sca_stats_gca_per_90', 
    'gca_gca_stats_gca_per_90', 
    'touches_mid_3rd_stats_possession_per_90', 
    'touches_att_3rd_stats_possession_per_90', 
    'take_ons_succ_stats_possession_per_90', 
    'carries_prgc_stats_possession_per_90', 
    'receiving_prgr_stats_possession_per_90', 
    'tackles_mid_3rd_stats_defense_per_90', 
    'aerial_duels_won%_stats_misc_per_90', 
    'performance_crs_stats_misc_per_90', 
    'tackles_tkl_stats_defense_per_90', 
    'int_stats_defense_per_90', 
    'performance_recov_stats_misc_per_90'
]


#========================# Radar Charts Script #========================#

# Font URLs for radar variables 
FONT_URLS = {
    'serif_regular': ('https://raw.githubusercontent.com/googlefonts/SourceSerifProGFVersion/main/fonts/'
                      'SourceSerifPro-Regular.ttf'),
    'serif_extra_light': ('https://raw.githubusercontent.com/googlefonts/SourceSerifProGFVersion/main/fonts/'
                          'SourceSerifPro-ExtraLight.ttf'),
    'rubik_regular': ('https://raw.githubusercontent.com/google/fonts/main/ofl/rubikmonoone/'
                      'RubikMonoOne-Regular.ttf'),
    'robotto_thin': 'https://raw.githubusercontent.com/google/fonts/main/apache/roboto/main/src/hinted/Roboto-Thin.ttf',
    'robotto_bold': ('https://raw.githubusercontent.com/google/fonts/main/apache/robotoslab/'
                     'RobotoSlab%5Bwght%5D.ttf')
}

# Metrics renaming map 
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
