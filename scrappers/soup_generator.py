import requests
from bs4 import BeautifulSoup as bs

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
}


def get_soup(url):
    print(f"URL: {url} >>> Requesting... ", end="")
    response = requests.get(url, headers=headers)
    if response.ok:
        print(f"Success! ({response.status_code} {response.reason})")
        return bs(response.text, "html.parser")
    else:
        print(f"Fail! - {response.status_code} {response.reason}")
        raise Exception("Request Failed!")
