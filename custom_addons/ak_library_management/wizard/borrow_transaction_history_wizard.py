# -*- coding: utf-8 -*-
from itertools import repeat

from odoo import models, fields


class BorrowTransactionHistory(models.TransientModel):
    """
    This is Transient model and redirect when confirm button is clicked.
    """
    _name = 'borrow.transaction.history.wizard'
    _description = 'borrow transaction history wizard'

    message = fields.Text(string='Error:')

    def action_cancel(self):
        """
        when click cancel button then current record is deleted.
        param: None
        rtype: None
        """
        rec = self.env["borrow.transaction.history"].search([], order='id desc', limit=1)
        rec.unlink()

    def action_continue(self):
        """
        if whenever click continue button then check other validation from that record.
        param: None
        rtype: function
        """
        rec = self.env["borrow.transaction.history"].search([], order='id desc', limit=1)
        rec.cnt += 1
        return rec.action_custom_confirm()
