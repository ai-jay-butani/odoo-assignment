# -*- coding: utf-8 -*-

from odoo import models, fields


class StockMoveLine(models.Model):
    _inherit = 'stock.move'

    job_name = fields.Char(string='Job Name')