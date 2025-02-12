# -*- coding: utf-8 -*-
from odoo import models,fields,api


class LibraryBulkBook(models.TransientModel):
    """
    In this model add multiple book names with comma separated value and
    also select author name from contacts model.
    """
    _name = "library.bulk.book"
    _description = "library bulk book"

    book_names = fields.Text(string="Book Names", required=True,default="")
    author_id = fields.Many2one(comodel_name="res.partner",string="Author",required=True)
    category = fields.Char(string="Category")
    price = fields.Float(string="Price",default=100)
    check = fields.Boolean("Check",default=False)
    count_created_product = fields.Integer(compute="_compute_count_created_product")

    def create_products(self):
        """
        When we click create products button than this method is call and create
        each product of current bulk books.
        """
        individual_book = self.book_names.split(',')
        val_list = []
        for book in individual_book:
            exist_book = self.env["product.template"].search([("name", "=", book)])
            if exist_book:
                continue
            val_list.append({"name":book, "author":self.author_id.name})

        if val_list:
            self.env['product.template'].create(val_list)
        self.check = True

    def revert_changes(self):
        """
        When we click revert changes button than this method is call and
        delete all current bulk books from product menu.
        """
        individual_book = self.book_names.split(',')
        for book in individual_book:
            exist_record = self.env["product.template"].search([("name", "=", book)])
            exist_record.unlink()
        self.check = False

    @api.depends("book_names")
    def _compute_count_created_product(self):
        """
        Count the current bulk books and display this count on smart button.
        """
        individual_book = self.book_names.split(',')
        if self.check:
            self.count_created_product = len(individual_book)
        elif not self.check and self.count_created_product != 0:
            self.count_created_product -= len(individual_book)
        else:
            self.count_created_product = 0

    def action_created_product(self):
        """
        When we click Products Count smart button then this method is call
        and return the list of that products.
        """
        if self.count_created_product == 1:
            product_id = self.env["product.template"].search([("name", "=", self.book_names)])
            return {
                'name': 'Product',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'product.template',
                'res_id': product_id.id,
            }
        return {
            'name': 'Product',
            'type': 'ir.actions.act_window',
            'view_mode': 'list,form',
            'res_model': 'product.template',
            'domain': [('name', 'in', self.book_names.split(','))],
        }

