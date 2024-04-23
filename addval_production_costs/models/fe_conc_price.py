# -*- coding: utf-8 -*-

from odoo import models, fields, api

class FeConcPrice(models.Model):
    _name = "fe.conc.price"

    name = fields.Char(string='Nombre', compute='_compute_name')
    price = fields.Integer(string='Calificación')
    company_id = fields.Many2one('res.company', string='Compañía', default=lambda self: self.env.company)

    def _compute_name(self):
        self.name = str(self.price)