#-*- coding: utf-8 -*-
from odoo import models,fields

class BookLocation(models.Model):
    _name = "library.book.location"
    _description = "library management"

    name = fields.Char(string="Library Name")
    location = fields.Char(string="Library Location")
    capacity = fields.Integer(string="Capacity")
    notes = fields.Text(string="Note")
    book_ids = fields.One2many(comodel_name="library.book",inverse_name='library_ids',string="Book_id")