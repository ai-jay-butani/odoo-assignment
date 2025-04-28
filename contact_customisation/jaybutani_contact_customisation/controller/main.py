# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from odoo.exceptions import ValidationError
import re


class ContactController(http.Controller):

    @http.route('/contacts', type="http", auth="public", website=True)
    def fetch_all_contacts(self):
        """
        search all contacts of res.partner model and return contact kanban
        template.

        param:None
        return: xml template
        """
        contacts = request.env['res.partner'].sudo().search([])
        values = {
            'records': contacts,
        }
        return request.render('jaybutani_contact_customisation.contact_kanban_template', values)

    @http.route('/contacts/<slug>', type="http", auth="public", website=True, csrf=False)
    def fetch_individual_contact(self, **args):
        """
        Using slug to search particular contact and return contact detail form

        param:slug(string)
        return:xml template
        """
        contact = request.env['res.partner'].sudo().search([('contact_slug', '=', args['slug'])])
        values = {
            'contact': contact
        }
        return request.render('jaybutani_contact_customisation.contact_detail_form_template', values)

    @http.route('/contact/save', type='json', auth='user', website=True)
    def save_contact_details(self, **args):
        """
        Form save button is click then this controller is call and check some validation
        and save that editable data in database

        return: None
        """
        regex = r'^[a-zA-Z][a-zA-Z0-9._]*@[a-zA-Z]*.[a-z]*$'
        # pattern1 = r'(^[\(])(\+91\))(\s)([0-9]{5,5})(\s)([0-9]{5,5})'
        digit_cnt = 0
        if not re.match(regex, args.get('email')):
            raise ValidationError("The email address is not valid")
        else:
            for i in args.get('phone'):
                if i.isdigit():
                    digit_cnt += 1

            if digit_cnt > 13 or digit_cnt < 10:
                raise ValidationError("The Mobile Number is not valid")
            elif request.env['res.partner'].search(
                    [('id', '!=', args.get('contact_id')), ('email', '=', args.get('email'))]):
                raise ValidationError("This email already in data")
            else:
                contact = request.env['res.partner'].search([('id', '=', args.get('contact_id'))])
                args.pop('contact_id')
                contact.write(args)
        return
