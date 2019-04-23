# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _


class PortalWizard(models.TransientModel):
    _inherit = 'portal.wizard'

    def _default_user_ids(self):
        users = super(PortalWizard, self)._default_user_ids()

        default_password = self.env['portal.wizard.user']._default_password()
        for user in users:
            vals = user[2]['password'] = default_password
        return users

    user_ids = fields.One2many(default=_default_user_ids)


class PortalWizardUser(models.TransientModel):
    _inherit = 'portal.wizard.user'

    @api.model
    def _default_password(self):
        return self.env['ir.config_parameter'].sudo().get_param('portal.default_password', 'password')

    password = fields.Char('Password', default=_default_password)

    @api.multi
    def action_apply(self):
        res = super(PortalWizardUser, self).action_apply()
        for wizard_user in self.sudo().with_context(active_test=False).filtered(lambda u: u.in_portal):
            wizard_user.user_id.password = wizard_user.password
        return res
