# -*- coding: utf-8 -*-

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
        """
        rec_id = self.env.context.get('active_id')
        self.env["borrow.transaction.history"].browse(rec_id).unlink()

    def action_continue(self):
        """
        if whenever click continue button then decrease on hand quantity by one.
        """
        books = self.env.context.get('book_ids')
        for rec in self.env["product.template"].browse(books).filtered(lambda book:
                                                                       book.qty_available):
            loc = self.env['stock.quant'].search([('product_tmpl_id.id', '=', rec.id)], limit=1)
            self.env['stock.quant']._update_available_quantity(loc.product_id, loc.location_id,
                                                               quantity=-1)
