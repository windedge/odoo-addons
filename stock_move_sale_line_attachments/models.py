# -*- coding: utf-8 -*-

from openerp import models, fields, api


class StockMove(models.Model):
    _inherit = 'stock.move'

    sale_line_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment', relation='stock_move_sale_line_attchment_rel',
        string='Sale line attachments',
        compute='get_sale_line_attachments', readonly=True)

    @api.one
    @api.depends('procurement_id.sale_line_id')
    def get_sale_line_attachments(self):
        self.sale_line_attachment_ids = False
        if self.procurement_id and self.procurement_id.sale_line_id:
            ids = [a.id for a in self.procurement_id.sale_line_id.attachment_ids]
            self.sale_line_attachment_ids = [(6, 0, ids)]
