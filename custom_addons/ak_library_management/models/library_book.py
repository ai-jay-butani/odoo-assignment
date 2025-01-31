# -*- coding: utf-8 -*-
from odoo import models,fields


class Book(models.Model):
    _name = 'library.book'
    _description = 'library management'

    name = fields.Char(string='Book Title')
    author = fields.Char(string='Author Name')
    isbn = fields.Char(string='ISBN')
    publication_date = fields.Date(string='Date of Publication')
    state = fields.Selection(selection= [('available','Available'),('borrowed','Borrowed')],
                             string = 'Book Availability')
    description = fields.Text(string='Book Summary')
    category_ids = fields.Many2one('library.book.category',string='Category')
    tags_ids = fields.Many2many('library.book.tags',string='Tags', related='category_ids.tag_ids')
