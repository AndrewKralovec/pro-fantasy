import requests
import pandas as pd
from bs4 import BeautifulSoup

REMOTE_API = 'https://www.pro-football-reference.com'


def fetch_pgl_stats(options):
    response = requests.get(
        '{0}/play-index/pgl_finder.cgi'.format(REMOTE_API),
        params={'request': 1, **options}
    )
    response.raise_for_status()

    return response.content


def parse_pgl(response):
    soup = BeautifulSoup(response, 'html.parser')
    results_tbl = soup.find(id='results')
    results_thead = results_tbl.find('thead')
    results_body = results_tbl.find('tbody')

    # NOTE: Ignore fist tr

    header = results_thead.find_all('tr')[1]
    columns = list(filter(lambda x: x != None, [
        try_get_text(item) for item in header]))

    data = []
    rows = results_body.find_all('tr')
    for row in rows:
        # They scope the PK value
        scope = row.find('th').contents
        cols = row.find_all('td')
        # HTML will repeast headers
        if not len(cols):
            continue

        content = scope + list(filter(lambda x: x != None, [
            try_get_text(item) for item in cols]))
        data.append(content)

    return (columns, data)


def to_csv(file_name, table):
    (columns, data) = table
    dataFrame = pd.DataFrame(data=data, columns=columns)
    dataFrame.to_csv(file_name)

def try_get_text(item):
    try:
        return None if item == '\n' else item.get_text()
    except:
        return None
