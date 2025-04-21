# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    custom_variant_seller_ids = fields.One2many('product.supplierinfo','product_id',store=True)
    variant_seller_ids = fields.One2many('product.supplierinfo',compute="_compute_inverse_name")

    @api.depends('vendor_on_variant')
    def _compute_inverse_name(self):
        for rec in self:
            if rec.vendor_on_variant:
                rec.variant_seller_ids = rec.product_tmpl_id.variant_seller_ids
            else:
                rec.variant_seller_ids = rec.custom_variant_seller_ids
