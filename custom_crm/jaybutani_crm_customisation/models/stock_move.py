# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockMoveLine(models.Model):
    _inherit = 'stock.move'

    job_name = fields.Char(string='Job Name', compute="_compute_job_from_sale")

    @api.depends('sale_line_id.order_id.job_name')
    def _compute_job_from_sale(self):
        for rec in self:
            rec.job_name = rec.sale_line_id.order_id.job_name
