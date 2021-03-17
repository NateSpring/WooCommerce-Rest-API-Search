import os
from woocommerce import API

find_text = 'text to find in product description'

wcapi = API(url="http://yourdomain.com",
            consumer_key="ck_XXXXXXXXXXXXXXXXXXXXXXX",
            consumer_secret="cs_XXXXXXXXXXXXXXXXXXXX",
            version="wc/v3")

prod_count = 0
for x in range(7):
    try:
        r = wcapi.get('products', params={
            'page': x + 1,
            'per_page': 100
        }).json()
        for product in r:
            prod_count += 1
            if find_text in product['description']:
                print('Found:{}'.format(product['sku']))

    except Exception as e:
        print(e)

print('Total Products Scanned:{}'.format(prod_count))
