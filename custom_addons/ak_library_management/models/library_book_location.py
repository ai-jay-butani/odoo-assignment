#-*- coding: utf-8 -*-
from odoo import models,fields,api


class LibraryBookLocation(models.Model):
    """
    We can add Library name, location, capacity of library, and note
    In Library Book Location model we can select books from product menu and don't add the new book.
    """
    _name = "library.book.location"
    _description = "library book location"
    _inherit = 'mail.thread'

    name = fields.Char(string="Library Name",required=True)
    location = fields.Char(string="Library Location",tracking=True)
    capacity = fields.Integer(string="Capacity")
    notes = fields.Text(string="Note")
    book_ids = fields.Many2many(comodel_name="product.template",
                                domain=[('is_library_book','=',True)],string="Book Id",tracking=True)
    count_borrowed_book = fields.Integer(compute="_compute_count_borrowed_book")
    librarian_id = fields.Many2one(comodel_name='res.users', string='Librarian')

    _sql_constraints = [("name_unique","unique(name)","The library is unique.")]

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

    @api.constrains('book_ids')
    def _check_book_ids(self):
        """
        send notification to librarian if books is add or delete in many2many field.
        """
        self.env['bus.bus']._sendone(self.librarian_id.partner_id, 'simple_notification', {
            'type': 'success',
            'message': f"In library[{self.name}] books list are updated.",
        })
