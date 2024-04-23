# -*- coding: utf-8 -*-

from odoo import models, fields, api

class FeConcGrade(models.Model):
    _name = "fe.conc.grade"

    name = fields.Char(string='Nombre', compute='_compute_name')
    fe_conc_percentage = fields.Float(string='Porcentaje')
    company_id = fields.Many2one('res.company', string='Compañía', default=lambda self: self.env.company)

    def _compute_name(self):
        self.name = str(self.fe_conc_percentage) + '%'
