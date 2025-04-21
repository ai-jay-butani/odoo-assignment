# -*- coding: utf-8 -*-
{
    'name': 'Product Catalog',
    'version': '18.0.1.0.0',
    'author': 'Jay Butani',
    'sequence': 5,
    'summary': 'Product Catalog generator Module',
    'description': "Product Catalog",
    'website': 'https://www.aktivsoftware.com',
    'data': [
        'security/ir.model.access.csv',
        'report/product_catalog_report_template.xml',
        'report/ir_actions_report.xml',
        'views/sale_menus.xml'
    ],
    'depends':['sale_management','contacts'],
    'application': True,
    'license': 'LGPL-3',
}
