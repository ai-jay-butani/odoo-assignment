# -*- coding: utf-8 -*-
from odoo import models,fields,api,_


class LibraryMembers(models.Model):
    """
    We can add library members name, email, phone no and membership date.
    """
    _name = 'library.members'
    _description = 'library members'

    membership_no = fields.Char(string="Membership Id",default="New")
    name = fields.Char(string='Member Name',required=True)
    email = fields.Char(string='Email ID')
    phone = fields.Char(string='Contact Number')
    membership_date = fields.Date(string='Membership Start Date')

    @api.model_create_multi
    def create(self, vals_list):
        """
        inherit the create method and update sequence number.
        """
        for val in vals_list:
            val['membership_no'] = self.env["ir.sequence"].next_by_code('library.members')
        return super().create(vals_list)
