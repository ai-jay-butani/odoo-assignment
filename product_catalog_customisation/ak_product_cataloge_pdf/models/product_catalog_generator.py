# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProductCatalogGenerator(models.TransientModel):
    _name = "product.catalog.generator"
    _description = "Product Catalog"

    catalog_style = fields.Selection([('style1', 'Style1'), ('style2', 'Style2')], string="Catalog Style", required=True)
    page_break_after = fields.Integer(string="Page Break After", default=1)
    product_ids = fields.Many2many(comodel_name='product.product', string='Product')

    @api.constrains('page_break_after')
    def _check_page_break_after(self):
        """
        set maximum and minimum limit of product in one page, then condition is check and raise validation
        """
        if self.page_break_after > 5 or self.page_break_after < 1:
            raise ValidationError("Maximum 5 and Minimum 1 products are include in one page")