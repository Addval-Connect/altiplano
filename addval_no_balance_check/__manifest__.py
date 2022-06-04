# -*- coding: utf-8 -*-
{
    'name': "addval_no_balance_check",

    'summary': """
        USE WITH CAUTION: This module disables balance credit-debit check.
        USAR CON PRECAUCION: Este módulo desactiva la comprobación de saldo crédito-débito.
        """,

    'description': """
        Disables balance credit-debit check. / Desactiva la comprobación de saldo crédito-débito.
    """,

    'author': "Addval Connect",
    'website': "http://www.addval.io",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'accounting']
}
