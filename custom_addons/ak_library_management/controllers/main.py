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