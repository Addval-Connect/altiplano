# -*- coding: utf-8 -*-
{
    'name': "Calculadora de produccion",

    'summary': """
        Módulo que agrega campos especificos para poder calcular las concentraciones de minerales fabricadas""",

    'description': """
        Módulo que agrega campos especificos para poder calcular las concentraciones de minerales fabricadas
    """,

    "author": "Addval Connect",
    "website": "http://www.addval.cl",
    "category": "Product",
    "license": "Other proprietary",
    'version': '0.1',

    'depends': ['base','account','sale_management'],

    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/au_conc_grade.xml',
        'views/cu_price.xml',
        'views/fe_conc_grade.xml',
        'views/fe_conc_price.xml',
        'views/fe_grade.xml',
        'views/gold_price.xml',
        'views/mrp_production.xml',
        'views/plant_recovery.xml',        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}