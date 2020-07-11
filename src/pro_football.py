import requests
from bs4 import BeautifulSoup

REMOTE_API = 'https://www.pro-football-reference.com'

def fetch_pgl_stats(options):
    response = requests.get(
        '{0}/play-index/pgl_finder.cgi'.format(REMOTE_API),
        params=options
    )
    response.raise_for_status()

    return response.content


def parse_pgl(response):
    soup = BeautifulSoup(response, 'html.parser')
    results_tbl = soup.find(id='results')
    results_thead = results_tbl.find('thead')
    results_body = results_tbl.find('tbody')

    return results_tbl
