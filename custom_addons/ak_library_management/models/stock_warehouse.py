# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    library_assistant = fields.Many2one(string='Library Assistant', comodel_name='hr.employee')
    library_worker = fields.Many2many(string='Library Worker', comodel_name='hr.employee')

    @api.constrains('library_assistant','library_worker')
    def _check_name_of_assistant_worker(self):
        if self.library_assistant in self.library_worker:
            raise ValidationError(f'library assistant({self.library_assistant.name}) is not take as a library worker')