from urllib.error import URLError, HTTPError

from bs4 import BeautifulSoup


def parse(url):
    try:

        soup = BeautifulSoup(url, 'html.parser')
        soup.prettify()

        return soup

    except HTTPError as e:
        print(e.status, e.reason)

    except URLError as e:
        print(e.reason)


def treat_html(input):
    return " ".join(input.split()).replace('> <', '><')
