# -*- coding: utf-8 -*-
from datetime import date,timedelta
from odoo import models,fields,api
from odoo.exceptions import ValidationError


class BorrowTransactionHistory(models.Model):
    """
    This form is open in wizard in product model and add some fields.
    we can add borrow books, start date, end date, deposit amount and customer name.
    """
    _name = 'borrow.transaction.history'
    _description = 'borrow transaction history'
    _rec_name = 'customer_id'

    customer_id = fields.Many2one(comodel_name='res.partner',string='Customer',required=True)
    book_ids = fields.Many2many(comodel_name='product.template',string='Books')
    borrow_start_date = fields.Date(string="Start Date",default=date.today())
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
        return: wizard
        """
        if self.customer_id.not_trust_worthy:
            message = "Customer is not trustworthy. Are you sure you want to continue?"
            return self.custom_wizard(message)

        product_list = [rec.name for rec in self.book_ids if rec.qty_available == 0]
        if product_list:
            message = (f"The following books are out of stock: {product_list}."
                       f" Are you sure you want to continue?")
            return self.custom_wizard(message)

        if len(self.book_ids) > 5:
            search_recd = self.search([('customer_id',"=",self.customer_id)])
            books_name = []
            [books_name.append(book.name) for rec in search_recd[:-1]
             for book in rec.book_ids if book.name not in books_name]

            if books_name:
                message = (f"Customer already has [{len(search_recd)-1}] open borrow transactions "
                           f"with {books_name} books. "
                           f"Are you sure you want to borrow more books?")
                return self.custom_wizard(message)

            message = ("Are you sure you want to allow "
                       "borrowing more than 5 books for this customer?")
            return self.custom_wizard(message)

    def reminder_borrow_book(self):
        """
        Borrow book remainder for customer if the borrow end date is within next 2 days
        param: None
        return: None
        """
        all_recd = self.search([])
        for record in all_recd:
            date_deadline = record.borrow_start_date + timedelta(days=2)
            if record.borrow_end_date == date_deadline:
                self.env['bus.bus']._sendone(record.customer_id, 'simple_notification', {
                    'type': 'warning',
                    'message': f"reminder: your book return date is {record.borrow_end_date}",
                })

    def automated_action(self):
        """
        If customer has not return book before due date so that customer can't borrow
        more books.
        param: None
        return: Exception
        """
        search_rec = self.search([('customer_id', "=", self.customer_id)])
        for rec in search_rec[:-1]:
            for book in rec.book_ids:
                if rec.borrow_end_date < date.today() and book.status == "borrowed":
                    raise ValidationError(f"{rec.customer_id.name} with overdue books "
                                          f"cannot new ones until"
                                          f" you return the overdue items.")
