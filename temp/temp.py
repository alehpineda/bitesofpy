import requests
from requests import HTTPError, Timeout


def google_query(query):
    """
    trivial function that does a GET request
    against google, checks the status of the
    result and returns the raw content
    """
    try:
        url = "https://www.google.com"
        params = {"q": query}
        resp = requests.get(url, params=params, timeout=1)
        resp.raise_for_status()
        return resp.content
    except HTTPError:
        return False
    except Timeout:
        return True