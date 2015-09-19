# -*- coding: utf-8 -*-

from openerp import models, fields, api


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    sale_line_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment', relation='mrp_sale_line_attchment_rel',
        string='Sale line attachments',
        compute='get_sale_line_attachments', readonly=True)

    @api.one
    @api.depends('move_prod_id.procurement_id.sale_line_id')
    def get_sale_line_attachments(self):
        self.sale_line_attachment_ids = [(5)]
        if self.move_prod_id and self.move_prod_id.procurement_id \
                and self.move_prod_id.procurement_id.sale_line_id:
            ids = [a.id for a in self.move_prod_id.procurement_id.sale_line_id.attachment_ids]
            self.sale_line_attachment_ids = [(6, 0, ids)]



