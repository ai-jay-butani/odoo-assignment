# -*- coding: utf-8 -*-

from odoo import models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _prepare_procurement_values(self, group_id):
        """
        Inherit prepare procurement values method and redirect job name to stock.rule

        param: group_id(record_set)
        return: values(dict)
        """
        values = super()._prepare_procurement_values(group_id)
        values['job_name'] = self.order_id.job_name
        return values

    def _timesheet_create_project_prepare_values(self):
        """
        Inherit project prepare values and redirect sale order job name to project job name

        param: None
        return: values(dict)
        """
        values = super()._timesheet_create_project_prepare_values()
        values['name'] = '%s - %s' % (
            self.order_id.name, self.order_id.job_name) if self.order_id.job_name else self.order_id.name
        values["job_name"] = self.order_id.job_name
        return values
