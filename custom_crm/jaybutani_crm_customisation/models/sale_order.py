# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    job_name = fields.Char(string='Job Name', compute='_compute_job_from_opportunity', store=True)

    def _get_action_view_picking(self, pickings):
        """
        inherit sale order Delivery smart button method and add context of
        default_job_name and return that action

        param: pickings(String)
        return: action(dict)
        """
        action = super()._get_action_view_picking(pickings)
        action['context']['default_job_name'] = self.job_name
        return action

    @api.depends('opportunity_id')
    def _compute_job_from_opportunity(self):
        """
        If opportunity id is change than job name is change this method are
        depends on crm name

        param: None
        return: None
        """
        for rec in self:
            rec.job_name = rec.job_name
            if rec.opportunity_id:
                rec.job_name = rec.opportunity_id.name

    def _prepare_invoice(self):
        """
        Inherit prepare invoice and add job name value to invoice job name

        param: None
        return: vals(dict)
        """
        vals = super()._prepare_invoice()
        vals['job_name'] = self.job_name
        return vals
