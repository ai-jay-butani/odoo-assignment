# -*- coding: utf-8 -*-
{
    'name': 'Product Out of stock Page',
    'version': '18.0.0.0.0',
    'author': 'Jay Butani',
    'sequence': 5,
    'summary': 'Product Customisation Module',
    'description': "Add product out of stock page",
    'website': 'https://www.aktivsoftware.com',
    'data': [
        'views/product_template_views.xml',
        'views/product_stock_template.xml',
    ],
    'depends': ['sale_management', 'website_sale'],
    'application': True,
    'license': 'LGPL-3',
}
