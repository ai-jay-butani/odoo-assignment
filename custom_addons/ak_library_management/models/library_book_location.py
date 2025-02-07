#-*- coding: utf-8 -*-
from odoo import models,fields


class LibraryBookLocation(models.Model):
    """
    We can add Library name, location, capacity of library, and note
    In Library Book Location model we can select books from product menu and don't add the new book.
    """
    _name = "library.book.location"
    _description = "library management"

    name = fields.Char(string="Library Name")
    location = fields.Char(string="Library Location")
    capacity = fields.Integer(string="Capacity")
    notes = fields.Text(string="Note")
    book_ids = fields.Many2many(comodel_name="product.template",domain=[('is_library_book','=','true')],string="Book_id")
