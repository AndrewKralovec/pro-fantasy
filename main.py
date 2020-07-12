import sys
import src.pro_football as api
from argparse import ArgumentParser


def parse_args(args):
    parser = ArgumentParser(description='')
    parser.add_argument('--output', help='output format type',
                        choices=['csv', 'console', 'pdf'], required=False, default='pdf')
    parser.add_argument('--file_name', help='',
                        required=False, default='output')
    # Request options
    parser.add_argument('--year_min', help='starting value for the years range in the search query',
                        required=False, default=2018)
    parser.add_argument('--year_max', help='ending value for the years range in the search query',
                        required=False, default=2019)
    parser.add_argument('--pos', '--position', nargs='+',
                        help='positions for the search query. Defaults to all positions', required=False, default=['QB', 'WR', 'RB', 'TE', 'OL', 'DL', 'LB', 'DB'])
    parser.add_argument('--game_num_min', help='',
                        required=False, default=0)
    parser.add_argument('--game_num_max', help='',
                        required=False, default=99)
    parser.add_argument('--week_num_min', help='',
                        required=False, default=0)
    parser.add_argument('--week_num_max', help='',
                        required=False, default=99)
    parser.add_argument('--order_by', help='What score/points segment the query will be ordered by',
                        required=False, default='fantasy_points')
    return parser.parse_args(args)


def main(argv):
    query = vars(parse_args(argv))
    
    # Remove the non api query string options
    output = query['output']
    file_name = query['file_name']
    del query['output']
    del query['file_name']

    if output == 'console':
        print(api.to_console(api.parse_pgl(api.fetch_pgl_stats(query))))
    elif output == 'csv':
        return api.to_csv('{0}.{1}'.format(file_name, output), api.parse_pgl(
            api.fetch_pgl_stats(query)))
    elif output == 'pdf':
        return api.to_pdf('{0}.{1}'.format(file_name, output), api.parse_pgl(
            api.fetch_pgl_stats(query)))


if __name__ == '__main__':
    print(main(sys.argv[1:]))
