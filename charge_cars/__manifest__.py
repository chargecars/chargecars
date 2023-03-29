# -*- coding: utf-8 -*-
{
    "name": "Charge-Cars",
    "version": "16.0.1",
    "author": "Smart IT Ltd",
    "category": "Other",
    "summary": "Charge Cars Customizations",
    'description': "Custom module for Charge Cars developed by Smart IT Ltd",
    'maintainer': "Smart IT Ltd",
    'website': 'smart-ltd.co.uk',
    'images': [],
    "depends": [
        'purchase'
    ],
    "init_xml": [],
    "demo_xml": [],
    "data": [
        'security/ir.model.access.csv',
        'views/res_config_settings.xml',
        'report/report_template.xml',
        'report/purchase_order_template.xml',
        'wizard/purchase_general_terms_and_condition_wizard.xml'
    ],
    'assets': {
    },
    "auto_install": False,
    "application": False,
    "installable": True,
}
