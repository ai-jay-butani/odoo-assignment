# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class ContactsController(http.Controller):

    @http.route('/contacts', type="http", auth="public", website=True)
    def fetch_all_contacts(self, **kw):
        contacts = request.env['res.partner'].search([])
        values = {
            'records': contacts
        }
        return request.render('ak_library_management.contact_kanban_template', values)

    @http.route('/contacts/<slug>', type="http", auth="public", website=True)
    def fetch_individual_contact(self, **args):
        contact = request.env['res.partner'].search([('contact_slug', '=', args['slug'])])
        values = {
            'contact': contact
        }
        return request.render('ak_library_management.contact_detail_form_template', values)

    @http.route('/customer', type="http", auth="public", website=True, csrf=False)
    def input_customer_data(self, **args):
        return request.render('ak_library_management.customer_form_page')

    @http.route('/customer/email', type="json", auth="public", website=True, csrf=False)
    def fetch_customer_data(self, **args):
        customer = request.env['res.partner'].search([('email', '=', args.get('email'))])
        vals = {
            'name': customer.name,
            'address': customer.contact_address,
            'phone': customer.phone
        }
        return vals
