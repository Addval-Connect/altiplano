# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AuConcGrade(models.Model):
    _name = "au.conc.grade"

    name = fields.Char(string='Nombre', compute='_compute_name')
    grade = fields.Float(string='Calificación')
    company_id = fields.Many2one('res.company', string='Compañía', default=lambda self: self.env.company)

    def _compute_name(self):
        self.name = str(self.grade)