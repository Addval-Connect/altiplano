# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GoldPrice(models.Model):
    _name = "gold.price"

    name = fields.Char(string='Nombre', compute='_compute_name')
    price = fields.Integer(string='Precio')
    company_id = fields.Many2one('res.company', string='Compañía', default=lambda self: self.env.company)

    def _compute_name(self):
        for s in self:
            s.name = str(s.price)