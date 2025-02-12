# -*- coding: utf-8 -*-
from odoo import models,fields,api


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
    status = fields.Selection([
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('reserved', 'Reserved')
    ],string="Status")

    def mark_as_available(self):
        """
        If status is borrowed then mark as available button is display
        and when we click that button then this method is call
        """
        self.status = "available"

    def mark_as_borrowed(self):
        """
        If status is available then mark as borrowed button is display
        and when we click that button then this method is call
        """
        self.status = "borrowed"

    @api.model_create_multi
    def create(self,vals):
        """
        inherit the create method and update sequence number.
        """
        res = super().create(vals)
        res.default_code = self.env["ir.sequence"].next_by_code('product.template')
        return res
