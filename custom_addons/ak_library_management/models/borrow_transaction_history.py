# -*- coding: utf-8 -*-
from odoo import models,fields,api
from datetime import datetime
from odoo.exceptions import ValidationError


class BorrowTransactionHistory(models.Model):
    """
    This form is open in wizard in product model and add some fields.
    we can add borrow books, start date, end date, deposit amount and customer name.
    """
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
        """
        check end date is grater than start date or not.
        param: none
        """
        if self.borrow_end_date < self.borrow_start_date:
            raise ValidationError("Borrow end date should be higher than start date.")

    def custom_wizard(self,message):
        """
        repeated part in code when we check any condition then return custom wizard.
        param: none
        """
        return {
           'name': 'ValidationError',
           'type': 'ir.actions.act_window',
           'res_model': 'borrow.transaction.history.wizard',
           'view_mode': 'form',
           'target': 'new',
           'context': {'default_message': message}
        }

    def action_confirm(self):
        """
        when we click confirm button then check conditions like customer is trustworthy or not,
        check product quantity,check books count
        param: none
        """
        if self.customer_id.not_trust_worthy:
            message = "Customer is not trustworthy. Are you sure you want to continue?"
            return self.custom_wizard(message)

        product_list = [rec.name for rec in self.book_ids if rec.qty_available == 0]
        if product_list:
            message = f"The following books are out of stock: {product_list}. Are you sure you want to continue?"
            return self.custom_wizard(message)

        if len(self.book_ids) > 5:
            search_recd = self.search([('customer_id.name',"=",self.customer_id.name)])
            books_name = []
            [books_name.append(book.name) for rec in search_recd[:-1] for book in rec.book_ids if book.name not in books_name]

            if books_name:
                message = f"Customer already has [{self.customer_id.name}] open borrow transactions with {books_name} books. Are you sure you want to borrow more books?"
                return self.custom_wizard(message)
            else:
                message = f"Are you sure you want to allow borrowing more than 5 books for this customer?"
                return self.custom_wizard(message)

        for rec in self.book_ids:
            if rec.qty_available:
                rec.qty_available -= 1



