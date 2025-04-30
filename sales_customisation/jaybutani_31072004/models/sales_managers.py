# -*- coding: utf-8 -*-

from odoo import models, fields


class SalesManagerApproval(models.Model):
    _name = 'sales.managers'

    sales_manager_ids = fields.Many2many(comodel_name="sales.manager.approval", string="Sale Managers")
