# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = ["product.template"]

    product_review_ids = fields.One2many(comodel_name="product.review", inverse_name="product_id")
