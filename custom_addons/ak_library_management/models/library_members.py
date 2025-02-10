# -*- coding: utf-8 -*-
from odoo import models,fields


class LibraryMembers(models.Model):
    """
    We can add library members name, email, phone no and membership date.
    """
    _name = 'library.members'
    _description = 'library management'

    name = fields.Char(string='Member Name',required=True)
    email = fields.Char(string='Email ID')
    phone = fields.Char(string='Contact Number')
    membership_date = fields.Date(string='Membership Start Date')
