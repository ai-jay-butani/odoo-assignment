# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectProject(models.Model):
    _inherit = 'project.project'

    job_name = fields.Char(string='Job Name', compute='_compute_job_from_sale_order')

    @api.depends('sale_order_id.job_name')
    def _compute_job_from_sale_order(self):
        """
        compute job name from sale order job name

        return: None
        """
        for rec in self:
            rec.job_name = rec.sale_order_id.job_name

