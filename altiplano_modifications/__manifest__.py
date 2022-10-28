# -*- coding: utf-8 -*-
{
    "name": "Altiplano Custom Modifications (Addval)",
    "summary": "Compilation of all altiplano custom modifications (Addval)",
    "description": """This module adds the following modifications:
    - Replace <Receptor>/<Contacto> with move.contact_override in DTE if set""",
    "author": "Addval Connect",
    "website": "http://www.addval.cl",
    "category": "Accounting",
    "version": "0.2",
    "license": "Other proprietary",
    "depends": ["l10n_cl_edi", "l10n_cl_edi_stock", "account"],
    "data": [
        "template/dte_template.xml",
        "views/account_move_views.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
