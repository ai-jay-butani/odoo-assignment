# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LibraryMembers(models.Model):
    """
    We can add library members name, email, phone no and membership date.
    """
    _name = 'library.members'
    _description = 'library members'
    _rec_name = 'member_id'

    membership_no = fields.Char(string="Membership Id", default="New")
    member_id = fields.Many2one(comodel_name='res.partner', string='Member Name', required=True)
    email = fields.Char(related='member_id.email', string='Email ID')
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

    def send_renewal_mail(self):
        """
        only librarian can send the mail to the library member for renewal membership.
        return: wizard
        """
        mail_template = self.env.ref('ak_library_management.email_template_renewal_membership')
        ctx = {
            'default_template_id': mail_template.id
        }
        if self.env.user.is_librarian:
            return {
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'mail.compose.message',
                'target': 'new',
                'context': ctx
            }
        raise ValidationError("You don't have access this button contact librarian.")
