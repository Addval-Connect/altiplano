# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PlantRecovery(models.Model):
    _name = "plant.recovery"

    name = fields.Char(string='Nombre', compute='_compute_name')
    plant_recovery = fields.Float(string='Porcentaje')
    company_id = fields.Many2one('res.company', string='Compañía', default=lambda self: self.env.company)

    def _compute_name(self):
        for s in self:
            s.name = str(s.plant_recovery) + '%'
