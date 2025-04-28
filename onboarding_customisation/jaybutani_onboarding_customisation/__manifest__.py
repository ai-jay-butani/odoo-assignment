# -*- coding: utf-8 -*-
{
    'name': 'User Onboarding',
    'version': '18.0.1.0.0',
    'author': 'Jay Butani',
    'sequence': 5,
    'summary': 'User Onboarding Module',
    'description': "User Onboarding",
    'website': 'https://www.aktivsoftware.com',
    'data': [
        'views/welcome_page_template.xml',
        'views/user_details_form_template.xml',
        'views/res_partner_views.xml',
        'views/success_page_template.xml',
    ],
    'depends': ['contacts','website'],
    'application': True,
    'license': 'LGPL-3',
}
