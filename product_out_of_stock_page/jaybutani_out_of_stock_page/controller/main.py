# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class ProductOutOfStock(WebsiteSale):

    def sitemap_products(env,rule,qs):
        """
        Inherit base sitemap_products method
        """
        return super().sitemap_products(env,rule,qs)

    @http.route(['/shop/<model("product.template"):product>'], type='http', auth="public", website=True,
          sitemap=sitemap_products, readonly=True)
    def product(self, product, **kwargs):
        """
        Inherit product detail controller and if product is out of stock then render customize
        out of stock page otherwise working base flow
        """
        product_out_of_stock = request.env['product.template'].search([('id','=',product.id),('is_out_of_stock', '=', True)])
        if product_out_of_stock:
            vals = {
                'product': product_out_of_stock
            }
            return request.render("jaybutani_out_of_stock_page.product_out_of_stock",vals)
        return super().product(product, **kwargs)
