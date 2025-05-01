# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = ["product.template"]

    is_out_of_stock = fields.Boolean(string="Not Available (Out of Stock)")
    out_of_stock_message = fields.Html(string="Custom Out-of-Stock Message")