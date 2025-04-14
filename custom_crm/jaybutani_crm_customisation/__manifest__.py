# -*- coding: utf-8 -*-
{
    'name': 'CRM Customisation',
    'version': '18.0.1.0.1',
    'author': 'Jay Butani',
    'sequence': 5,
    'summary': 'CRM Customisation Module',
    'description': "Custom CRM",
    'website': 'https://www.aktivsoftware.com',
    'data': [
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
        'views/mrp_production_views.xml',
        'views/project_project_views.xml',
        'views/account_move_views.xml'
    ],
    'depends':['sale_management','contacts','stock','crm','mrp', 'project', 'sale_project','account'],
    'application': True,
    'license': 'LGPL-3',
}
