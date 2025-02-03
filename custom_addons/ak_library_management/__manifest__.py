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
        'views/library_book_location_view.xml'
    ],
    'depends':['base','web'],
    'application': True,
    'license': 'LGPL-3',
}
