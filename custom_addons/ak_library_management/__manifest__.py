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
        'views/library_book_views.xml',
        'views/library_members_views.xml',
        'views/library_book_tags_views.xml',
        'views/library_book_category_views.xml',
        'views/library_book_location_views.xml',
        'views/product_template_views.xml',
        'views/product_template_barcode_views.xml',
        'views/sale_menus.xml',
        'views/library_bulk_book_views.xml',
        'data/ir_sequence_data.xml'
    ],
    'depends':['sale_management','product'],
    'application': True,
    'license': 'LGPL-3',
}
