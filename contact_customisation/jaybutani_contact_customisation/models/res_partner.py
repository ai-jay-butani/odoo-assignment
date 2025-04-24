# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    contact_slug = fields.Char(string="contact slug", compute="_compute_contact_slug", store=True)

    @api.depends('name')
    def _compute_contact_slug(self):
        """
        Slugify the record set and convert into string and write in compute field

        rtype: None
        """
        for rec in self:
            rec_slug = self.env['ir.http']._slugify(str(rec))
            rec.contact_slug = rec_slug