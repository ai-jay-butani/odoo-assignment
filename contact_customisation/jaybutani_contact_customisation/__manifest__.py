# -*- coding: utf-8 -*-
{
    'name': 'Website Contact Menu Customisation',
    'version': '18.0.1.0.0',
    'author': 'Jay Butani',
    'sequence': 5,
    'summary': 'Contact Customisation Module',
    'description': "Contact Customisation",
    'website': 'https://www.aktivsoftware.com',
    'data': [
        'views/res_partner_custom_template.xml',
        'views/web_page_menus.xml'
    ],
    'assets':{
        'web.assets_frontend': [
                                'jaybutani_contact_customisation/static/src/js/contact_webcontroller.js',
                            ]
        },
    'depends':['contacts','website'],
    'application': True,
    'license': 'LGPL-3',
    }
