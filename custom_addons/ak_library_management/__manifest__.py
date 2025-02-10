# -*- coding: utf-8 -*-
{
    'name': 'Library Management',
    'version': '18.0.1.0.0',
    'author': 'Jay Butani',
    'sequence': 5,
    'summary': 'Library Management Module',
    'description': "LMS",
    'website': 'https://www.aktivsoftware.com',
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_view.xml',
        'views/library_members_view.xml',
        'views/library_book_tags_view.xml',
        'views/library_book_category_view.xml',
        'views/library_book_location_view.xml',
        'views/product_template_view.xml',
        'views/product_template_barcode_view.xml',
        'views/sale_menus.xml'
    ],
    'depends':['sale_management','product'],
    'application': True,
    'license': 'LGPL-3',
}
