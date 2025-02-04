# -*- coding: utf-8 -*-
from odoo import models,fields


class BookCategory(models.Model):
    """
    We can add book category and also give tags to that category.
    """
    _name = 'library.book.category'
    _description = 'library management'

    name = fields.Char(string='Book Category', required=True)
    tag_ids = fields.Many2many('library.book.tags', string='Tags')
