import requests

REMOTE_API = 'https://www.pro-football-reference.com'

def fetch_pgl_stats(options):
    response = requests.get(
        '{0}/play-index/pgl_finder.cgi'.format(REMOTE_API),
        params=options
    )
    response.raise_for_status()

    return response.content