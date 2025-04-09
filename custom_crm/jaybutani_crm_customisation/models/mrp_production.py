# -*- coding: utf-8 -*-

from odoo import models, fields


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    job_name = fields.Char(related='move_dest_ids.job_name',string='Job Name', readonly=False)