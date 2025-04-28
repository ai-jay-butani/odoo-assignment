# -*- coding: utf-8 -*-

from odoo import models, fields


class Partner(models.Model):
    _inherit = 'res.partner'

    date_birth = fields.Date(string="Date Of Birth")
    place_birth = fields.Char(string="Place of Birth")
    gender = fields.Char(string="Gender")
    passport_detail = fields.Char(string="Passport")
    driving_license = fields.Char(string="Driving License")
    speaking_language = fields.Char(string="Language")
