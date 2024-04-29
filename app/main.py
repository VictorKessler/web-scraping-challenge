from fastapi import FastAPI

from controllers import main

app = FastAPI()


@app.get('/list_products')
def list_products():
    """Returns a list with all products in the page"""
    try:
        return main.list_products()
    except Exception as e:
        return e.__str__()


@app.get('/best_sellers')
def get_best_sellers():
    try:
        return main.get_best_sellers()
    except Exception as e:
        return e.__str__()


@app.get('/get_by_rating/{rating}')
def get_product_by_rating(rating):
    try:
        return main.get_product_by_rating(rating)
    except Exception as e:
        return e.__str__()


@app.get('/get_by_name/{name}')
def get_product_by_name(name):
    try:
        return main.get_product_by_name(name)
    except Exception as e:
        return e.__str__()