# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class Controller(http.Controller):

    @http.route('/customer', type="http", auth="public", website=True, csrf=False)
    def input_customer_data(self):
        """
        return customer form page

        param: None
        return: None
        """
        return request.render('ak_library_management.customer_form_page')

    @http.route('/customer/email', type="json", auth="public", website=True, csrf=False)
    def fetch_customer_data(self, **args):
        """
        Using email search particular customer and then return details of that customer

        param: email(string)
        return: dictionary
        """
        customer = request.env['res.partner'].sudo().search([('email', '=', args.get('email'))])
        vals = {
            'name': customer.name,
            'address': customer.contact_address,
            'phone': customer.phone
        }
        return vals
