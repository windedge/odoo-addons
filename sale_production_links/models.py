# -*- coding: utf-8 -*-

from openerp import models, fields, api


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    partner_id = fields.Many2one(
        comodel_name='res.partner', string='Customer', store=True,
        related='move_prod_id.procurement_id.sale_line_id.order_id.partner_id')
    sale_order_id = fields.Many2one(
        comodel_name='sale.order', string='Sale Order', store=True,
        related='move_prod_id.procurement_id.sale_line_id.order_id')
    sale_line_id = fields.Many2one(
        comodel_name='sale.order.line', string='Sale Line', store=True,
        related='move_prod_id.procurement_id.sale_line_id')


class Sale(models.Model):
    _inherit = 'sale.order'

    production_ids = fields.One2many(comodel_name='mrp.production', inverse_name='sale_order_id', string='Production')

    production_count = fields.Integer(compute="_get_production_count")

    @api.one
    def _get_production_count(self):
        if self.production_ids:
            self.production_count = len(self.production_ids)
