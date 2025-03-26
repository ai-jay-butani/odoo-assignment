# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class ContactsController(http.Controller):

    @http.route('/contacts', type="http", auth="public", website=True)
    def display_contacts(self, **kw):
        contacts = request.env['res.partner'].search([])
        values = {
            'records': contacts
        }
        return request.render('ak_library_management.contact_kanban_template', values)

    @http.route('/contacts/<slug>', type="http", auth="public", website=True)
    def individual_contact(self, slug):
        contact = request.env['res.partner'].search([('contact_slug', '=', slug)])
        values = {
            'contact': contact
        }
        return request.render('ak_library_management.contact_detail_form_template', values)
