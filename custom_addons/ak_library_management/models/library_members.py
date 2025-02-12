# -*- coding: utf-8 -*-
from odoo import models,fields,api


class LibraryMembers(models.Model):
    """
    We can add library members name, email, phone no and membership date.
    """
    _name = 'library.members'
    _description = 'library members'

    name = fields.Char(string='Member Name',required=True)
    email = fields.Char(string='Email ID')
    phone = fields.Char(string='Contact Number')
    membership_date = fields.Date(string='Membership Start Date')
    membership_no = fields.Char(string="Member ID",default="New")

    @api.model_create_multi
    def create(self, vals):
        """
        inherit the create method and update sequence number.
        """
        res = super().create(vals)
        res.membership_no = self.env["ir.sequence"].next_by_code('library.members')
        return res
