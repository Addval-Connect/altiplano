# -*- coding: utf-8 -*-
from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    contact_override = fields.Char(
        default="",
        string="Sobre-escribir contacto en DTE",
        help="Definir este campo para sobre-escribir el contacto en el DTE",
    )
