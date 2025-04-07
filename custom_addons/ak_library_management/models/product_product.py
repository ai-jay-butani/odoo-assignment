# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    # seller_ids = fields.One2many('product.supplierinfo','product_id')
    custom_variant_seller_ids = fields.One2many('product.supplierinfo','product_id')

    # @api.depends('vendor_on_variant')
    # def _compute_inverse_name(self):
    #     for rec in self:
    #         if not rec.vendor_on_variant:
    #             print('.......',rec.vendor_on_variant)
    #             rec.product_tmpl_id = rec.product_id

