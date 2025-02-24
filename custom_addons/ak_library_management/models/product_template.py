# -*- coding: utf-8 -*-
from odoo import models,fields,api
from datetime import *

from odoo.exceptions import ValidationError


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
        ('reserved', 'Reserved')
    ],string="Status",tracking=True)

    def mark_as_available(self):
        """
        If status is borrowed then mark as available button is display
        and when we click that button then this method is call
        """
        self.status = "available"

    def mark_as_borrowed(self):
        """
        If status is available then mark as borrowed button is display
        and when we click that button then this method is call
        """
        self.status = "borrowed"
        date_deadline = date.today() + timedelta(days=10)
        return super().activity_schedule(date_deadline=date_deadline,summary=f'book borrowed by {self.env.user.name} and return date {date_deadline}')


    @api.model_create_multi
    def create(self,vals_list):
        """
        inherit the create method and update sequence number.
        """
        for val in vals_list:
            val['default_code'] = self.env["ir.sequence"].next_by_code('product.template')
        return super().create(vals_list)

    def _compute_display_name(self):
        for rec in self:
            if self._context.get('add_author') and rec.author:
                rec.display_name = '[' + rec.author + ']' + rec.name
            else:
                rec.display_name = rec.name

    @api.model
    @api.readonly
    def name_search(self, name='', args=None, operator='ilike', limit=None):
        args = list(args or [])
        if name:
            args += [('author', operator, name)]
        return super().name_search(args=args, limit=limit)

    def borrowed_books(self):
        return {
            'name':'Borrow Books',
            'type':'ir.actions.act_window',
            'res_model':'borrow.transaction.history',
            'view_mode':'form',
            'target':'new'
        }

    def return_book(self):
        date_deadline = date.today() + timedelta(days=10)
        if self.status == 'borrowed' and date.today() < date_deadline:
            raise ValidationError(f"return date is {date_deadline} so you can't return book.")

