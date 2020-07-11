import src.pro_football as api


if __name__ == "__main__":
    print(api.fetch_pgl_stats({
        'request': 1,
        'match': 'game',
        'year_min': 2018,
        'year_max': 2019,
        'season_start': 1,
        'season_end': -1,
        'pos': ['QB', 'WR', 'RB', 'TE', 'OL', 'DL', 'LB', 'DB'],
        'is_starter': 'E',
        'game_type': 'R',
        'game_num_min': 0,
        'game_num_max': 99,
        'week_num_min': 0,
        'week_num_max': 99,
        'c5val': 1.0,
        'order_by': 'fantasy_points',
    }))
