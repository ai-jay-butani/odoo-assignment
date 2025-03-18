# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockWarehouse(models.TransientModel):
    _inherit = 'res.config.settings'

    borrow_limit = fields.Integer(string="Borrowing limit", config_parameter="ak_library_management.borrow_limit")