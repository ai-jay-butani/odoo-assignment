# -*- coding: utf-8 -*-
from odoo import models,fields


class BookTags(models.Model):
    _name = 'library.book.tags'
    _description = 'library management'

    name = fields.Char(string='Tags', required=True)
