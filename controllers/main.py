from service.HTML_reading_service import read
from utils.get_text_by_class import get_text
from utils.string_sanitizer import sanitize
import pandas as pd
import numpy as np
import json


def list_products():
    """Documentation here"""

    json_of_products = df.to_json(orient='records')
    products = json.loads(json_of_products)

    return products


def get_best_sellers():
    best_sellers = df.query('best_seller == True')
    best_sellers_json = best_sellers.to_json(orient='records')
    best_sellers_products = json.loads(best_sellers_json)

    return best_sellers_products


def get_product_by_rating(rating):
    if float(rating) in np.arange(0, 5, 0.1):
        rating_results = df.query(f'rating > {rating}')
        rating_json = rating_results.to_json(orient='records')
        higher_ratings_products = json.loads(rating_json)

        return higher_ratings_products
    else:
        raise Exception('Illegal argument. rating might be greater than 0 or smaller than 5.')


def get_product_by_name(name):
    products = list_products()

    products_with_same_name = []

    for product in products:
        if name.lower() in product['name'].lower():
            products_with_same_name.append(product)

    return products_with_same_name


def create_df():
    list_of_products = []

    soup = read()

    products = soup.findAll('div',
                            {'class': 'sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20'})

    for product in get_text(products):
        product_obj = sanitize(product['name'],
                               product['price'],
                               product['best_seller'],
                               product['rating'])

        list_of_products.append(product_obj)

    df = pd.DataFrame(list_of_products)

    return df


if __name__ == '__main__' or 'list_products' or 'get_best_sellers':
    df = create_df()
