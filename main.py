import src.pro_football as api
from argparse import ArgumentParser


if __name__ == '__main__':
    parser = ArgumentParser(description='')
    # Request options
    parser.add_argument('--match', help='',
                        required=False, default='game')
    parser.add_argument('--year_min', help='',
                        required=False, default=2018)
    parser.add_argument('--year_max', help='',
                        required=False, default=2019)
    parser.add_argument('--season_start', help='',
                        required=False, default=1)
    parser.add_argument('--season_end', help='',
                        required=False, default=-1)
    parser.add_argument('--pos', '--position', nargs='+',
                        help='', required=False, default=['QB', 'WR', 'RB', 'TE', 'OL', 'DL', 'LB', 'DB'])
    parser.add_argument('--is_starter', help='',
                        required=False, default='E')
    parser.add_argument('--game_type', help='',
                        required=False, default='R')
    parser.add_argument('--game_num_min', help='',
                        required=False, default=0)
    parser.add_argument('--game_num_max', help='',
                        required=False, default=99)
    parser.add_argument('--week_num_min', help='',
                        required=False, default=0)
    parser.add_argument('--week_num_max', help='',
                        required=False, default=99)
    parser.add_argument('--c5val', help='',
                        required=False, default=1.0)
    parser.add_argument('--order_by', help='',
                        required=False, default='fantasy_points')

    args = vars(parser.parse_args())
    (headers, data) = api.parse_pgl(api.fetch_pgl_stats(args))

    print(headers, data)
