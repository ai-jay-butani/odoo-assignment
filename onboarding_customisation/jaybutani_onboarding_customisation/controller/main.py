# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.home import Home
from odoo.exceptions import ValidationError
import re

class HomeInherit(Home):

    @http.route('/web/login', type='http', auth='public', readonly=False)
    def web_login(self, redirect=None, **kw):
        res = super().web_login(redirect=redirect, **kw)
        if request.httprequest.method == 'POST' and request.env.user.tour_enabled:
            return request.render('jaybutani_onboarding_customisation.welcome_page_template')
        return res

class ContactDetails(http.Controller):

    @http.route('/user/details', type="http", auth='user', website=True)
    def contact_form(self):
        return request.render('jaybutani_onboarding_customisation.user_detail_form_template')

    @http.route('/user/details/submit', type="http", auth="user", website=True, methods=['POST','GET'], csrf=False)
    def contact_form_submit(self, **args):

        pattern1 = r'(^[\(])(\+91\))(\s)*([0-9]{5,5})(\s)*([0-9]{5,5})'
        pattern2 = r'[0-9]{16,16}'
        error_list = {
            'errors':[],
        }
        if not re.match(pattern1,args.get('mobile')):
            error_list['errors'].append("Mobile Number is not valid")
        if not re.match(pattern2,args.get('passport_detail')):
            error_list['errors'].append("Passport Number is not valid")
        if error_list['errors']:
            return request.render('jaybutani_onboarding_customisation.user_detail_form_template', error_list)

        contact = request.env['res.partner'].sudo().search([('id', '=', request.env.user.partner_id.id)])
        contact.write(args)
        return request.render('jaybutani_onboarding_customisation.success_page_template')

    @http.route('/user/details/submit_successfully', type="http", auth="user", website=True)
    def contact_success_page(self):
        request.env.user.tour_enabled = False
        return request.redirect('/odoo')