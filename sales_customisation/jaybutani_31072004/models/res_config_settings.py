# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    def add_managers(self):
        """
        In setting we click add managers button then we can add sales manager approval in many2many
        field

        return: dictionary
        """
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'sales.managers',
            'view_mode': 'form',
            'target': 'new',
        }
