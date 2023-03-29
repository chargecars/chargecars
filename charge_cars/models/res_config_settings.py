# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    purchase_general_terms_condition = fields.Html(related='company_id.purchase_general_terms_condition',
                                                   string='Terms and Conditions')

    def open_general_term_condition(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Terms and Condition'),
            'res_model': 'purchase.general.terms.condition',
            'view_mode': 'form',
            'target': 'new',
            'context': {'active_id': self.id,
                        'default_purchase_general_terms_condition': self.purchase_general_terms_condition if self.purchase_general_terms_condition else ''},
            'views': [[False, 'form']]
        }


