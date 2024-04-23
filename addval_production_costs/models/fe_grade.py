# -*- coding: utf-8 -*-

from odoo import models, fields, api

class FeGrade(models.Model):
    _name = "fe.grade"

    name = fields.Char(string='Nombre', compute='_compute_name')
    fe_percentage = fields.Float(string='Porcentaje')
    company_id = fields.Many2one('res.company', string='Compañía', default=lambda self: self.env.company)

    def _compute_name(self):
        self.name = str(self.fe_percentage) + '%'

