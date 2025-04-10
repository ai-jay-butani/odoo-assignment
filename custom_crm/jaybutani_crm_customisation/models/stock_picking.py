# -*- coding: utf-8 -*-

from odoo import models, fields


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    job_name = fields.Char(related='move_ids.job_name', string='Job Name')
