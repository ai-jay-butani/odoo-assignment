# -*- coding: utf-8 -*-
from odoo import models,fields,api


class BorrowTransactionHistory(models.TransientModel):
    _name = 'borrow.transaction.history.wizard'
    _description = 'borrow transaction history wizard'

    message = fields.Text()

    def action_cancel(self):
        rec_id = self.env.context.get('active_id')
        self.env["borrow.transaction.history"].browse(rec_id).unlink()
