# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class SaleOrder(models.Model):
    """
    Inherit sale_order model and add some fields on base of some conditions.
    """
    _inherit = 'sale.order'

    SALE_ORDER_STATE = [
        ('draft', "Quotation"),
        ('sent', "Quotation Sent"),
        ('approval', "Pending Approval"),
        ('sale', "Sales Order"),
        ('cancel', "Cancelled"),
    ]
    state = fields.Selection(
        selection_add=SALE_ORDER_STATE,
        string="Status",
        readonly=True, copy=False, index=True,
        tracking=3,
        default='draft')

    approval_required = fields.Boolean(string="confirmation approval", compute="_compute_amount_total",
                                       store=True)
    sale_manager = fields.Many2one(comodel_name='sales.manager.approval', string="Sale Manager")
    approve_date = fields.Date(string="Approve Date")
    approve_by = fields.Char(string="Approve By")

    @api.depends('amount_total')
    def _compute_amount_total(self):
        """
        if change amount_total field then call this method and check approval is required
        or not.

        return: None
        """
        for rec in self:
            rec.approval_required = False
            managers_approval_rec = rec.env['sales.managers'].search([], order='id desc', limit=1)
            if managers_approval_rec.sales_manager_ids.filtered(
                    lambda approval: rec.amount_total > approval.approval_threshold):
                rec.approval_required = True

    def action_send_approve(self):
        """
        If click send approval button then this method is call and send mail to sale manager
        who is assigned to that particular sale order

        return: None
        """
        managers_approval_rec = self.env['sales.managers'].search([], order='id desc', limit=1)
        cnt = self.amount_total
        manager = ''
        for managers in managers_approval_rec.sales_manager_ids.filtered(
                lambda approval: self.amount_total > approval.approval_threshold):
            if (self.amount_total - managers.approval_threshold) < cnt:
                cnt = self.amount_total - managers.approval_threshold
                manager = managers

        self.sale_manager = manager
        template = self.env.ref('jaybutani_31072004.email_template_sales_manager')
        template.send_mail(self.id, force_send=True)
        self.message_post(
            body=f"{self.sale_manager.user_id.name} is a assigned approver , Threshold is {self.sale_manager.approval_threshold} and amount is {self.amount_total}.")
        self.state = 'approval'

    def action_approve(self):
        """
        If sale manager is click approve button then call this method and sale order is go to
        confirm state and add log note in chatter

        return: None
        """
        self.approval_required = False
        self.state = 'sale'
        self.approve_date = datetime.date.today()
        self.approve_by = self.env.user.name
        self.message_post(
            body=f"your sale order is confirm by {self.approve_by} and time is {self.approve_date}")

    def action_reminder_sale_order_approval(self):
        """
        Schedule action for if sale order are pending for approval then send remainder that all
        assigned manager for approval

        return: None
        """

        orders = self.search([('state', '=', 'approval')])

        for order in orders:
            template = self.env.ref('jaybutani_31072004.email_template_sales_manager_remainder')
            template.send_mail(order.id, force_send=True)
