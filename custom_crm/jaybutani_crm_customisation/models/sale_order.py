# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    job_name = fields.Char(string='Job Name')

    def _get_action_view_picking(self, pickings):
        action = super()._get_action_view_picking(pickings)
        action['context']['default_job_name'] = self.job_name
        return action

    @api.onchange('opportunity_id')
    def _onchange_job_from_opportunity(self):
        for rec in self:
            if rec.opportunity_id:
                rec.job_name = rec.opportunity_id.name

    def _prepare_invoice(self):
        vals = super()._prepare_invoice()
        vals['job_name'] = self.job_name
        return vals
