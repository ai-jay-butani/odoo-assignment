# -*- coding: utf-8 -*-
from odoo import models,fields


class LibraryBookTags(models.Model):
    """
    We can add book tags and this tags is use in the category model.
    """
    _name = 'library.book.tags'
    _description = 'library book tags'

    name = fields.Char(string='Tags', required=True)
