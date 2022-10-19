# -*- coding: utf-8 -*-
{
    "name": "Altiplano Custom Modifications (Addval)",
    "summary": "Compilation of all altiplano custom modifications (Addval)",
    "description": """This module adds the following modifications:
    - Replace <Receptor>/<Contacto> with 44 in DTE when the partner is 61703000-4""",
    "author": "Addval Connect",
    "website": "http://www.addval.cl",
    "category": "Accounting",
    "version": "0.2",
    "license": "Other proprietary",
    "depends": ["l10n_cl_edi", "l10n_cl_edi_stock"],
    "data": [
        "template/dte_template.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
