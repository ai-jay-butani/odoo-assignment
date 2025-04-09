# -*- coding: utf-8 -*-

from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    job_name = fields.Char(string='Job Name')

    def _get_action_view_picking(self, pickings):
        action = super()._get_action_view_picking(pickings)
        action['context']['default_job_name'] = self.job_name
        return action

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _prepare_procurement_values(self, group_id):
        values = super()._prepare_procurement_values(group_id)
        values['job_name'] = self.order_id.job_name
        return values

