# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SalesManagerApproval(models.Model):
    _name = 'sales.manager.approval'
    _rec_name = 'user_id'

    user_id = fields.Many2one(comodel_name="res.users", string="Sales Manager", required=True)
    approval_threshold = fields.Integer(string="Approval Threshold")

    @api.constrains('approval_threshold')
    def _check_approval_threshold(self):
        """
        This method is check the threshold amount is grater than or not

        return: None
        """
        if self.approval_threshold < 0:
            raise ValidationError("Approval threshold Amount should be greater than 0")

    @api.model_create_multi
    def create(self, vals):
        """
        Override create method and return validation error if approval_threshold already in records

        return: object
        """
        approval_record = self.search(
            [('approval_threshold', '=', vals[0].get('approval_threshold'))])

        if approval_record:
            raise ValidationError("You are already create same approval threshold")
        return super().create(vals)
