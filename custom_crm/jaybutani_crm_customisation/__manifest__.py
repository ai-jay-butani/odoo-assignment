# -*- coding: utf-8 -*-
{
    'name': 'CRM Customisation',
    'version': '18.0.0.0.0',
    'author': 'Jay Butani',
    'sequence': 5,
    'summary': 'CRM Customisation Module',
    'description': "Custom CRM",
    'website': 'https://www.aktivsoftware.com',
    'data': [
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
        'views/mrp_production_views.xml',
        'views/stock_move_views.xml',
    ],
    'depends':['sale_management','contacts','stock','crm', 'purchase','mrp', 'project'],
    'application': True,
    'license': 'LGPL-3',
}
