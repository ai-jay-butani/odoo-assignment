# -*- coding: utf-8 -*-

from datetime import date, timedelta
from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class ProductTemplate(models.Model):
    """
    I inherit product.template model and add some custom fields and
    also change the label of barcode field.
    """
    _inherit = ["product.template"]

    is_library_book = fields.Boolean(string="Is Library Book")
    author = fields.Char(string="Author")
    publisher = fields.Char(string="Publisher")
    edition = fields.Char(string="Edition")
    published_date = fields.Date(string="Published Date")
    pages = fields.Integer(string="Pages")
    available = fields.Boolean(string="Available")
    barcode = fields.Char(string="Isbn number")
    status = fields.Selection([
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned')
    ], string="Status", tracking=True)

    def mark_as_available(self):
        """
        If status is borrowed then mark as available button is display
        and when we click that button then this method is call
        param: none
        """
        self.status = "available"

    def mark_as_borrowed(self):
        """
        If status is available then mark as borrowed button is display
        and when we click that button then this method is call
        param: none
        """
        self.status = "borrowed"
        date_deadline = date.today() + timedelta(days=10)
        return super().activity_schedule(date_deadline=date_deadline,
                                         summary=f'book borrowed by {self.env.user.name} '
                                                 f'and return date {date_deadline}')

    @api.model_create_multi
    def create(self, vals_list):
        """
        inherit the create method and update sequence number.
        param: vals_list
        type: list of dictionary
        """
        for val in vals_list:
            val['default_code'] = self.env["ir.sequence"].next_by_code('product.template')
        return super().create(vals_list)

    def _compute_display_name(self):
        """
        override compute display name and change book name format to
        [author_name]book_name.
        param: none
        """
        for rec in self:
            if self._context.get('add_author') and rec.author:
                rec.display_name = '[' + rec.author + ']' + rec.name
            else:
                rec.display_name = rec.name

    @api.model
    @api.readonly
    def name_search(self, name='', args=None, operator='ilike', limit=None):
        """
        override name_search method to search book by author name.
        param: name, args, operator, limit
        """
        args = list(args or [])
        if name:
            args += [('author', operator, name)]
        return super().name_search(args=args, limit=limit)

    def borrowed_books(self):
        """
        when we click borrow books button then redirect wizard action
        param: none
        """
        return {
            'name': 'Borrow Books',
            'type': 'ir.actions.act_window',
            'res_model': 'borrow.transaction.history',
            'view_mode': 'form',
            'target': 'new'
        }

    @api.constrains('status')
    def _check_return_book(self):
        """
        if status is changed to returned then check the due date and give validation error
        else pass log note in chatter and if status is borrowed then also pass log note in chatter
        if all condition is false then send notification to the current user to status is changed.
        param: none
        """
        date_deadline = date.today()
        if self.status == 'returned':
            if date.today() < date_deadline:
                raise ValidationError(f"return date is {date_deadline} "
                                      f"so you can't return book.")
            self.message_post(body=f"{self.env.user.name} is returned the book.")
        if self.status == 'borrowed':
            self.message_post(body=f"{self.env.user.name} is borrowed the book and "
                                   f"the borrow date is {date.today()}")
        self.env['bus.bus']._sendone(self.env.user.partner_id, 'simple_notification', {
            'type': 'warning',
            'message': f"{self.name} book status is changed to {self.status}",
        })

    def mark_as_returned(self):
        """
        this method is called when we click server action change book status then change the
        status borrowed to return.
        return: None
        """
        self.write({'status': 'returned'})

    def _automated_action_duplicate_product_name(self):
        """
        raise validation error if product name is duplicate so we can not use same product name.
        return: ValidationError
        """
        if self.name:
            existing_product = self.env['product.template'].search([
                ('id', '!=', self.id), ('name', '=', self.name)])
            if existing_product:
                raise UserError("You can't have the same Product Name twice!  "
                                "(" + self.name + ")")
