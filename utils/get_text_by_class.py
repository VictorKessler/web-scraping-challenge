def get_text(tags_list):
    dict_products_list = []

    for tag in tags_list:
        name = tag.find('span', class_='a-size-base-plus a-color-base a-text-normal')
        price = tag.find('span', class_='a-price-whole')
        best_seller = tag.find('span', class_='a-badge-text')
        rating = tag.find('span', class_='a-icon-alt')

        product = {
            'name': str(name),
            'price': str(price),
            'best_seller': best_seller,
            'rating': str(rating)
        }

        dict_products_list.append(product)

    return dict_products_list
