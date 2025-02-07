# -*- coding: utf-8 -*-
from odoo import models,fields


class ProductTemplate(models.Model):
    """
    I inherit product.template model and add some custom fields and
    also change the label of barcode field.
    """
    _inherit = "product.template"

    is_library_book = fields.Boolean(string="Is Library Book")
    author = fields.Char(string="Author")
    publisher = fields.Char(string="Publisher")
    edition = fields.Char(string="Edition")
    published_date = fields.Date(string="Published Date")
    pages = fields.Integer(string="Pages")
    available = fields.Boolean(string="Available")
    barcode = fields.Char(string="Isbn number")
