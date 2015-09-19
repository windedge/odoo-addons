# -*- coding: utf-8 -*-

from openerp import models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    attachment_ids = fields.Many2many(
        comodel_name="ir.attachment", relation="sale_order_line_ir_attachment_relation",
        column1="sale_order_line_id", column2="attachment_id", string="Attachments", )
