# -*- coding: utf-8 -*-
from odoo import models,fields

class FreelanceJobPost(models.Model):
    _name = 'freelance.job.post'
    _description = 'job post'

    name = fields.Char(string='Job Title', required=True)
    author = fields.Char(string='Author Name')
    isbn = fields.Char(string='ISBN')
    publication_date = fields.Date(string='Date of Publication')