# -*- coding: utf-8 -*-
{
    'name': 'Product Review',
    'version': '18.0.1.0.0',
    'author': 'Jay Butani',
    'sequence': 5,
    'summary': 'Product Review Module',
    'description': "product review submission",
    'website': 'https://www.aktivsoftware.com',
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/product_review_views.xml',
        'views/product_template_views.xml',
    ],
    'depends': ['sale_management', 'contacts', 'website_sale'],
    'application': True,
    'license': 'LGPL-3',
}
