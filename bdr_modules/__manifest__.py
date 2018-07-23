# coding: utf-8
# Copyright (C) 2018-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'BdR - All Modules',
    'version': '10.0.1.0.0',
    'category': 'Custom',
    'summary': 'Install all modules required for BdR project',
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        # Odoo SA Modules
        'purchase',
        'sale',
        # OCA - Server Tools
        'auth_admin_passkey',
        'admin_technical_features',
        'disable_odoo_online',
        'mass_editing',
        'mass_sorting',
        # OCA - Web
        'web_export_view',
        'web_no_bubble',
        'web_searchbar_full_width',
        'web_sheet_full_width',
        'web_widget_float_formula',
    ],
    'installable': False,
    'auto_install': True,
}
