# -*- coding: utf-8 -*-
{
    'name': 'Sale Order Approval',
    'version': '18.0.1.0.0',
    'author': 'Jay Butani',
    'sequence': 5,
    'summary': 'Sale Order Approval Module',
    'description': "sale oder approval",
    'website': 'https://www.aktivsoftware.com',
    'data': [
        'security/ir.model.access.csv',
        'data/mail_template_sale_order.xml',
        'data/ir_cron_data_for_sale_order_approval.xml',
        'report/report_custom_sale_orders.xml',
        'views/sales_manager_approval_views.xml',
        'views/res_config_settings_views.xml',
        'views/sale_mamagers_views.xml',
        'views/sale_order_views.xml',
        'views/sale_order_approval_views.xml',
    ],
    'depends': ['sale_management'],
    'application': True,
    'license': 'LGPL-3',
}
