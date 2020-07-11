import sys
import src.pro_football as api
from argparse import ArgumentParser


def parse_args(args):
    parser = ArgumentParser(description='')
    # Request options
    parser.add_argument('--year_min', help='',
                        required=False, default=2018)
    parser.add_argument('--year_max', help='',
                        required=False, default=2019)
    parser.add_argument('--pos', '--position', nargs='+',
                        help='', required=False, default=['QB', 'WR', 'RB', 'TE', 'OL', 'DL', 'LB', 'DB'])
    parser.add_argument('--game_num_min', help='',
                        required=False, default=0)
    parser.add_argument('--game_num_max', help='',
                        required=False, default=99)
    parser.add_argument('--week_num_min', help='',
                        required=False, default=0)
    parser.add_argument('--week_num_max', help='',
                        required=False, default=99)
    parser.add_argument('--order_by', help='',
                        required=False, default='fantasy_points')
    return parser.parse_args(args)

def main(args):
    query = vars(parse_args(args))
    table = api.parse_pgl(api.fetch_pgl_stats(query))
    return table


if __name__ == '__main__':
    print(main(sys.argv))
