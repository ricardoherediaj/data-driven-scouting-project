# constants.py


# Transfermarkt URLs
championship_url = "https://www.transfermarkt.co.uk/championship/startseite/wettbewerb/GB2/plus/?saison_id=2024"
league_one_url = "https://www.transfermarkt.co.uk/league-one/startseite/wettbewerb/GB3/plus/?saison_id=2024"
league_two_url = "https://www.transfermarkt.co.uk/league-two/startseite/wettbewerb/GB4/plus/?saison_id=2024"


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
    ],
    'league_one': [
        ('https://fbref.com/en/comps/15/stats/League-One-Stats', 'stats_standard'),
        ('https://fbref.com/en/comps/15/shooting/League-One-Stats', 'stats_shooting'),
        ('https://fbref.com/en/comps/15/playingtime/League-One-Stats', 'stats_playing_time'),
        ('https://fbref.com/en/comps/15/misc/League-One-Stats', 'stats_misc')
    ],
    'league_two': [
        ('https://fbref.com/en/comps/16/stats/League-Two-Stats', 'stats_standard'),
        ('https://fbref.com/en/comps/16/shooting/League-Two-Stats', 'stats_shooting'),
        ('https://fbref.com/en/comps/16/playingtime/League-Two-Stats', 'stats_playing_time'),
        ('https://fbref.com/en/comps/16/misc/League-Two-Stats', 'stats_misc')
    ]
}

# Championship columns
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

# League One and League Two Columns
columns_to_retain_league_one_two = {
    'stats_standard': ['Player', 'Nation', 'Squad', 'Age', 'Born', 'Playing Time 90s', 'Position_2', 'Position'],
    'stats_playing_time': ['Player', 'Squad', 'Playing Time 90s', 'Playing Time MP', 'Playing Time Min'],
    'stats_shooting': ['Player', 'Squad', 'Standard Gls', 'Standard Sh', 'Standard SoT', 'Standard SoT%', 'Standard Sh/90', 'Standard SoT/90'],
    'stats_misc': ['Player', 'Squad', 'Performance Off', 'Performance Crs', 'Performance Int', 'Performance TklW',
                   'Performance Recov', 'Aerial Duels Won', 'Aerial Duels Lost', 'Aerial Duels Won%']
}

columns_to_retain = {
    'championship': columns_to_retain_championship,
    'league_one': columns_to_retain_league_one_two,
    'league_two': columns_to_retain_league_one_two
}