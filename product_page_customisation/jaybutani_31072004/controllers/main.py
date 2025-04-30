# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from datetime import date


class ProductReviewController(http.Controller):

    @http.route('/review/submit/<product_id>', type="http", auth="user", website=True, csrf=False, methods=['POST'])
    def fetch_review_data(self, product_id, **args):
        """
        if user click form review submit button then create record of product_review
        and redirect to product detail page
        """
        product = request.env['product.template'].browse(int(product_id))
        request.env['product.review'].create({
            'product_id': product_id,
            'user_id': request.env.user.id,
            'rating': args.get('rating'),
            'description': args.get('description'),
            'create_date': date.today()
        })
        rec_slug = request.env['ir.http']._slugify(str(product))
        return request.redirect(f"/shop/{rec_slug}")
