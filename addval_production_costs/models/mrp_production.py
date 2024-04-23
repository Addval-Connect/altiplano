# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MrpProduction(models.Model):
    _inherit = "mrp.production"

    #Campos relacionados a los concentrados
    mrp_cu_id = fields.Many2one('mrp.production', string='Concentrado de cobre', readonly=True)
    mrp_fe_id = fields.Many2one('mrp.production', string="Concentrado de fierro", readonly=True)
    mrp_relave_id = fields.Many2one('mrp.production', string="Relave", readonly=True)

    #Campos relacionados a mantenedores
    fe_grade_id = fields.Many2one('fe.grade', string='Ley Fierro')
    plant_recovery_id = fields.Many2one('plant.recovery', string='Recuperación Metalúrgica de la  Planta')
    fe_conc_grade_id = fields.Many2one('fe.conc.grade', string='Ley de concentrado de Fierro')
    au_conc_grade_id =fields.Many2one('au.conc.grade', string='Au Conc. Calificación')
    cu_price_id = fields.Many2one('cu.price', string='Precio Cu')
    gold_price_id = fields.Many2one('gold.price', string='Precio de oro')
    fe_conc_price_id = fields.Many2one('fe.conc.price', string='Precio del concentrado de Fe')

    #Campos con valores fijos
    tonnes_processed  = fields.Integer(string="Toneladas de Minerales Procesado", default=185)
    cu_grade = fields.Float(string="Ley Cobre", default=0.016, digits='Product Unit of Measure')
    cu_conc_grade = fields.Float(string="Ley de concentrado de cobre", default=0.265, digits='Product Unit of Measure')
    average_mining_humidity = fields.Float(string="Descuento humedad promedio mineral", default=0.965, digits='Product Unit of Measure')
    drum_efficiency_1 = fields.Float(string="Eficiencia tambor 1", digits='Product Unit of Measure')
    drum_efficiency_2 = fields.Float(string="Eficiencia tambor 2", digits='Product Unit of Measure')
    drum_efficiency_3 = fields.Float(string="Eficiencia tambor 3", digits='Product Unit of Measure')

    # @api.depends('bom_id', 'product_id')
    # def _compute_product_qty(self):
    #     for production in self:
    #         if production.state != 'draft':
    #             continue
    #         if production.product_id == 906:
    #             production.product_qty = production._calculate_cu_conc(production)

    #         elif production.product_id == 906:
    #             production.product_qty

    #         elif production.product_id == 906:
    #             production.product_qty

    #         else:
    #             if production.bom_id and production._origin.bom_id != production.bom_id:
    #                 production.product_qty = production.bom_id.product_qty

    #@api.onchange('cu_grade', 'tonnes_processed', 'plant_recovery_id', 'average_mining_humidity', 'cu_conc_grade')
    def calculate_cu_conc(self):
        plant_recovery = self.plant_recovery_id.plant_recovery/100
        tonnes_cu = (self.cu_grade * self.tonnes_processed * plant_recovery* self.average_mining_humidity)/self.cu_conc_grade				

        self.product_qty = tonnes_cu
    
    def calculate_fe_conc(self):
        if not self.mrp_cu_id:
            raise ValidationError("Se necesita tener primero el concentrado de Cobre")
        else:
            mineral_tonnes = self.tonnes_processed - round(self.mrp_cu_id.product_qty)
            fe_conc_grade = self.fe_conc_grade_id.fe_conc_percentage/100
            fe_grade = self.fe_grade_id.fe_percentage/100
            tonnes_fe = (mineral_tonnes * fe_grade * self.drum_efficiency_1 * self.drum_efficiency_2 * self.drum_efficiency_3)/fe_conc_grade				

            self.product_qty = tonnes_fe

    def calculate_relave(self):
        if not self.mrp_cu_id or not self.mrp_fe_id:
            raise ValidationError("Se necesita tener primero el concentrado de Cobre y Fierro")
        else:
            cu_tonnes = round(self.mrp_cu_id.product_qty)
            fe_tonnes = round(self.mrp_fe_id.product_qty)
            relave_tonnes = (self.tonnes_processed - cu_tonnes) - fe_tonnes				

            self.product_qty =  relave_tonnes

    def create_cu_conc(self):
        specific_product_id = 906 
        # Create a new mrp.production record
        new_manufacturing = self.env['mrp.production'].create({
            'product_id': specific_product_id,
            'product_uom': 1, 
            'product_qty': 1.0, 
        })

        self.mrp_cu_id = new_manufacturing.id

        # Return to the created record form view
        return {
            'type': 'ir.actions.act_window',
            'name': 'Manufacturing Order',
            'res_model': 'mrp.production',
            'view_mode': 'form',
            'res_id': new_manufacturing.id,
            'target': 'current',
        }
    
    def create_fe_conc(self):
        specific_product_id = 907 
        # Create a new mrp.production record
        new_manufacturing = self.env['mrp.production'].create({
            'product_id': specific_product_id,
            'product_uom': 1, 
            'product_qty': 1.0, 
        })

        self.mrp_fe_id = new_manufacturing.id

        # Return to the created record form view
        return {
            'type': 'ir.actions.act_window',
            'name': 'Manufacturing Order',
            'res_model': 'mrp.production',
            'view_mode': 'form',
            'res_id': new_manufacturing.id,
            'target': 'current',
        }
    
    def create_relave(self):
        specific_product_id = 908
        # Create a new mrp.production record
        new_manufacturing = self.env['mrp.production'].create({
            'product_id': specific_product_id,
            'product_uom': 1, 
            'product_qty': 1.0, 
        })

        self.mrp_relave_id = new_manufacturing.id

        # Return to the created record form view
        return {
            'type': 'ir.actions.act_window',
            'name': 'Manufacturing Order',
            'res_model': 'mrp.production',
            'view_mode': 'form',
            'res_id': new_manufacturing.id,
            'target': 'current',
        }