# -*- coding: utf-8 -*-
{
    'name': 'Shop Customisation',
    'version': '18.0.1.0.1',
    'author': 'Jay Butani',
    'sequence': 5,
    'summary': 'Shop Customisation Module',
    'description': "Shop Customisation",
    'website': 'https://www.aktivsoftware.com',
    'data': [
        'views/product_custom_add_to_cart_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'jaybutani_shop_customisation/static/src/js/add_to_cart.js'
        ]
    },
    'depends':['sale_management','website','website_sale','stock','contacts'],
    'application': True,
    'license': 'LGPL-3',
}
