# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductReview(models.Model):
    _name = 'product.review'
    _rec_name = "product_id"

    product_id = fields.Many2one(comodel_name="product.template", string='Product Id')
    user_id = fields.Many2one(comodel_name='res.users', string="reviewer")
    rating = fields.Selection([('1', '1'),
                               ('2', '2'),
                               ('3', '3'),
                               ('4', '4'),
                               ('5', '5')
                               ], string="Rating")
    description = fields.Text(string="Description")
    create_date = fields.Datetime(string="Submission timestamp")
