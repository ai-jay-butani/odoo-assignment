# -*- coding: utf-8 -*-

from datetime import date, timedelta
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class BorrowTransactionHistory(models.Model):
    """
    This form is open in wizard in product model and add some fields.
    we can add borrow books, start date, end date, deposit amount and customer name.
    """
    _name = 'borrow.transaction.history'
    _description = 'borrow transaction history'
    _rec_name = 'customer_id'

    cnt = fields.Integer(default=0, string='count')
    customer_id = fields.Many2one(comodel_name='res.partner', string='Customer', required=True)
    book_ids = fields.Many2many(comodel_name='product.template', string='Books')
    borrow_start_date = fields.Date(string="Start Date", default=date.today())
    borrow_end_date = fields.Date(string='End Date', required=True)
    deposit_amount = fields.Float(string="Deposit")
    is_member = fields.Boolean(related='customer_id.is_member')
    is_active = fields.Boolean(compute='_compute_active_transaction', store=True)
    is_higher_than_limit = fields.Boolean(compute='_compute_more_than_borrow_limit', store=True)

    @api.depends('book_ids')
    def _compute_more_than_borrow_limit(self):
        """
        check previously customer has open borrow transaction or not and check borrow limit
        customer can't borrow more than borrow limit.
        param: None
        rtype: None
        """
        for rec in self:
            rec.is_higher_than_limit = False
            borrow_transaction_ids = self.search([('customer_id.id', "=", self.customer_id.id)])
            books_name = [book.name for rec in borrow_transaction_ids
                          for book in rec.book_ids]
            if len(books_name) > int(rec.env['ir.config_parameter'].
                                             get_param('ak_library_management.borrow_limit')):
                rec.is_higher_than_limit = True

    @api.depends('borrow_end_date')
    def _compute_active_transaction(self):
        """
        check the transaction is active or not and set true or false in boolean field
        param: None
        rtype: None
        """
        for rec in self:
            rec.is_active = rec.borrow_end_date >= date.today()

    @api.constrains('borrow_start_date', 'borrow_end_date')
    def _check_end_date(self):
        """
        check end date is grater than start date or not.
        param: None
        rtype: None
        """
        if self.borrow_end_date < self.borrow_start_date:
            raise ValidationError("Borrow end date should be higher than start date.")

    def custom_wizard(self, message):
        """
        repeated part in code when we check any condition then return custom wizard.
        param: message(str)
        rtype: dict
        """
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'borrow.transaction.history.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_message': message,
                        'book_ids': [book.id for book in self.book_ids],
                        }
        }

    def check_confirm(self):
        """
        check conditions like customer is trustworthy or not,
        check product quantity,check books count
        param: None
        rtype: None
        """
        if self.customer_id.not_trust_worthy:
            message = "Customer is not trustworthy. Are you sure you want to continue?"
            yield self.custom_wizard(message)

        product_list = [rec.name for rec in self.book_ids if int(rec.qty_available) == 0]
        if product_list:
            message = (f"The following books are out of stock: {product_list}."
                       f" Are you sure you want to continue?")
            yield self.custom_wizard(message)

        if len(self.book_ids) > 5:
            borrow_transaction_ids = self.search([('customer_id', "=", self.customer_id.id)],
                                                 order='id desc', offset=1)
            books_name = []
            [books_name.append(book.name) for rec in borrow_transaction_ids
             for book in rec.book_ids if book.name not in books_name]

            if books_name:
                message = (f"Customer already has [{len(borrow_transaction_ids)}] open "
                           f"borrow transactions with {books_name} books. "
                           f"Are you sure you want to borrow more books?")
                yield self.custom_wizard(message)
            else:
                message = ("Are you sure you want to allow "
                           "borrowing more than 5 books for this customer?")
                yield self.custom_wizard(message)

    def action_custom_confirm(self):
        """
        when we click confirm button then call check_confirm method and check all validation
        and decrease on hand quantity by 1.
        param: None
        rtype: dict
        """
        action = self.check_confirm()
        list_action = list(action)
        if self.cnt > len(list_action) - 1:
            for rec in self.book_ids.filtered(lambda book: book.qty_available):
                loc = self.env['stock.quant'].search([('psearch_recdroduct_tmpl_id.id', '=', rec.id)], limit=1)
                self.env['stock.quant']._update_available_quantity(loc.product_id, loc.location_id,
                                                                   quantity=-1)
        else:
            return list_action[self.cnt]

    def _schedule_overdue_books(self):
        """
        Schedule action for overdue books and send mail to all that customer has not return the
        book after due date.
        param: None
        rtype: None
        """
        borrow_transaction_ids = self.search([('borrow_end_date', '<', date.today()),
                                              ('book_ids.status', '=', 'borrowed')])

        for rec in borrow_transaction_ids:
            template = self.env.ref('ak_library_management.email_template_book_overdue')
            template.send_mail(rec.id, force_send=True)

    def action_reminder_borrow_book(self):
        """
        Borrow book remainder for customer if the borrow end date is within next 2 days and
        send the mail to the customer
        param: None
        rtype: None
        """
        date_deadline = date.today() + timedelta(days=2)
        for rec in self.search([('borrow_end_date', '=', date_deadline),
                                ('book_ids.status', '=', 'borrowed')]):
            template = self.env.ref('ak_library_management.email_template_book_reminder')
            template.send_mail(rec.id, force_send=True)

    def action_overdue_borrowed_books(self):
        """
        If customer has not return book before due date so that customer can't borrow
        more books.
        param: None
        rtype: None
        """
        borrow_transaction_ids = self.search([('customer_id', "=", self.customer_id.id),
                                              ('borrow_end_date', '<', date.today()),
                                              ('book_ids.status', '=', 'borrowed')])
        for rec in borrow_transaction_ids:
            raise ValidationError(f"{rec.customer_id.name} with overdue books "
                                  f"cannot new ones until"
                                  f" you return the overdue items.")

    def action_change_borrowed_book_status(self):
        """
        change the book status from borrowed to returned using server action
        param: None
        rtype: None
        """
        for rec in self.search([('book_ids.status', '=', 'borrowed')]):
            for book in rec.book_ids:
                self.env['bus.bus']._sendone(rec.customer_id, 'simple_notification', {
                    'type': 'warning',
                    'message': f"{rec.customer_id.name} your return book has been recorded.",
                })
                book.mark_as_returned()
