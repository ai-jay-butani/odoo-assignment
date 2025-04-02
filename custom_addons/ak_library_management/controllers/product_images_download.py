# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request, content_disposition
import base64, zipfile, io


class ProductImageDownload(http.Controller):

    @http.route('/download_images/<product_id>', type='http', auth="public", website=True)
    def download_images(self, product_id, **args):
        product = request.env['product.template'].browse(int(product_id))
        image = [img for img in product.product_template_image_ids]

        if len(image) == 1:
            img_data = image[0].image_1920
            bin_data = base64.b64decode(img_data)
            return request.make_response(bin_data, [
                ('Content-Type', ''),
                ('Content-Disposition', content_disposition(f"{image[0].name}"))
            ])

        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for img in image:
                bin_data = base64.b64decode(img.image_1920)
                zip_file.writestr(img.name, bin_data)
        zip_buffer.seek(0)
        return request.make_response(zip_buffer.getvalue(), [
            ('Content-Type', 'application/zip'),
            ('Content-Disposition', content_disposition('images.zip'))
        ])
