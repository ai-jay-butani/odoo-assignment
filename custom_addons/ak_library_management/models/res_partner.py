# -*- coding: utf-8 -*-

from odoo import models, fields, api


# from odoo.addons.website.models.website import slug


class Partner(models.Model):
    _inherit = 'res.partner'

    not_trust_worthy = fields.Boolean(string="Not Trust Worthy")
    is_member = fields.Boolean(string="Is Member")
    contact_slug = fields.Char(string="contact slug", compute="_compute_contact_slug", store=True)

    @api.depends('name')
    def _compute_contact_slug(self):
        for rec in self:
            rec_slug = self.env['ir.http']._slugify(rec.name + '#' + str(rec.id))
            rec.contact_slug = rec_slug
