import re
from types import NoneType

price_regex = r'\d.\d{3}|\d{3}\s*'
rating_regex = r'(\d+,\d+\sde\s5\s+estrelas)'
product_regex = r'<\/?span[^>]*>'


def sanitize(name, price, best_seller, rating):
    name = get_name(name)
    price = get_price(price)
    best_seller = get_best_seller(best_seller)
    rating = get_rating(rating)

    product = {
        'name': name,
        'price': price,
        'best_seller': best_seller,
        'rating': rating
    }

    return product


def get_name(name):
    formatted = re.sub(product_regex, '', name)
    return re.sub(r'\s{2}', '', formatted)


def get_price(price):
    return re.findall(price_regex, price).pop()


def get_best_seller(best_seller):
    if isinstance(best_seller, NoneType):
        best_seller = False
    else:
        best_seller = True

    return best_seller


def get_rating(rating):
    match_rating = re.search(rating_regex, rating).group()
    rating_a = re.search(r'\b\d+(?:,\d+)', match_rating).group()
    rating = float(rating_a.replace(",", "."))

    return rating
