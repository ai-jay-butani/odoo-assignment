# -*- coding: utf-8 -*-
from odoo import models,fields


class LibraryBook(models.Model):
    """
    one library_book model is create and add some fields.
    We can add book title, author, reference number, publication date, state, description and
    add some fields has relation with other model.
    """
    _name = 'library.book'
    _description = 'library management'

    name = fields.Char(string='Book Title')
    author = fields.Char(string='Author Name')
    isbn = fields.Char(string='ISBN')
    publication_date = fields.Date(string='Date of Publication')
    state = fields.Selection(selection= [('available','Available'),('borrowed','Borrowed')],
                             string = 'Book Availability')
    description = fields.Text(string='Book Summary')
    category_ids = fields.Many2one(comodel_name='library.book.category',string='Category')
    tags_ids = fields.Many2many(comodel_name='library.book.tags',string='Tags',
                                related='category_ids.tag_ids')
    library_ids = fields.Many2one(comodel_name='library.book.location', string='Location')
