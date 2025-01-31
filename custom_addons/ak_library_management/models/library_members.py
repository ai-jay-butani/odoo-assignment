# -*- coding: utf-8 -*-
from odoo import models,fields

class Members(models.Model):
    _name = 'library.members'
    _description = 'library management'

    name = fields.Char(string='Member Name')
    email = fields.Char(string='Email ID')
    phone = fields.Char(string='Contact Number')
    membership_date = fields.Date(string='Membership Start Date')
