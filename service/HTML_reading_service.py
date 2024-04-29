from bs4 import BeautifulSoup

from service.HTML_parsing_service import parse


def read():
    url = 'pages/content.html'
    try:
        with open(url, 'r', encoding='utf-8') as f:
            unicode_text_contents = f.read()
        soup = parse(unicode_text_contents)
        assert isinstance(soup, BeautifulSoup)
        return soup
    except Exception:
        unicode_text_contents = url
        soup = parse(unicode_text_contents)
        assert isinstance(soup, BeautifulSoup)
        return soup
