# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CuPrice(models.Model):
    _name = "cu.price"

    name = fields.Char(string='Nombre', compute='_compute_name')
    price = fields.Float(string='Precio')
    company_id = fields.Many2one('res.company', string='Compañía', default=lambda self: self.env.company)

    def _compute_name(self):
        self.name = str(self.price)