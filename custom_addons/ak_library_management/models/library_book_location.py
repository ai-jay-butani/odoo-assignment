#-*- coding: utf-8 -*-
from odoo import models,fields,api


class LibraryBookLocation(models.Model):
    """
    We can add Library name, location, capacity of library, and note
    In Library Book Location model we can select books from product menu and don't add the new book.
    """
    _name = "library.book.location"
    _description = "library management"

    name = fields.Char(string="Library Name",required=True)
    location = fields.Char(string="Library Location")
    capacity = fields.Integer(string="Capacity")
    notes = fields.Text(string="Note")
    book_ids = fields.Many2many(comodel_name="product.template",
                                domain=[('is_library_book','=','true')],string="Book Id")
    count_borrowed_book = fields.Integer(compute="_compute_count_borrowed_book")

    def action_borrowed_book(self):
        """
        When I click Book Borrowed smart button then this method is call
        and return action
        """
        return {
            'name': 'Borrowed Books',
            'type': 'ir.actions.act_window',
            'view_mode': 'list,form',
            'res_model': 'product.template',
            'domain': [('status', '=', 'borrowed'),('id','in',self.book_ids.ids)],
        }

    @api.depends("book_ids")
    def _compute_count_borrowed_book(self):
        """
        Count the borrowed books from libraries books
        """
        book_borrowed_list = [record for record in self.book_ids if record.status == 'borrowed']
        self.count_borrowed_book = len(book_borrowed_list)
