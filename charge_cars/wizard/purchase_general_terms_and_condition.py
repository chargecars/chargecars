# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PurchaseGeneralTermsCondition(models.TransientModel):
    _name = 'purchase.general.terms.condition'

    purchase_general_terms_condition = fields.Html(string='Terms and Conditions')

    def update_terms(self):
        company_id = self.env.user.company_id
        company_id.sudo().write({'purchase_general_terms_condition': self.purchase_general_terms_condition})
        return {'type': 'ir.actions.act_window_close'}
