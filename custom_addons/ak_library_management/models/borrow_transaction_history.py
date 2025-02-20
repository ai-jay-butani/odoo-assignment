# -*- coding: utf-8 -*-
from odoo import models,fields,api
from datetime import datetime

from odoo.exceptions import ValidationError


class BorrowTransactionHistory(models.Model):
    _name = 'borrow.transaction.history'
    _description = 'borrow transaction history'

    customer_id = fields.Many2one(comodel_name='res.partner',string='Customer')
    book_ids = fields.Many2many(comodel_name='product.template',string='Books')
    borrow_start_date = fields.Date(string="Start Date",default=datetime.now())
    borrow_end_date = fields.Date(string='End Date',required=True)
    deposit_amount = fields.Float(string="Deposit")
    is_member = fields.Boolean(related='customer_id.is_member')

    @api.constrains('borrow_start_date','borrow_end_date')
    def _check_end_date(self):
        if self.borrow_end_date < self.borrow_start_date:
            raise ValidationError("Borrow end date should be higher than start date.")