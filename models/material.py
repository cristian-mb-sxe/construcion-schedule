from odoo import models, fields, api

class Material(models.Model):
    _name = 'schedule.material'
    _description = 'Material'

    name = fields.Char('Name', required=True)
    currency_id = fields.Many2one('res.currency', string='Currency');
    quantity = fields.Integer('Quantity')
    cost = fields.Float('Cost')
    provider = fields.Text('Provider Company')
    total_cost = fields.Float('Total', compute='_compute_total')
    material_id = fields.Many2one('schedule.construction', string='Construction')

    @api.depends('total_cost')
    def _compute_total(self): 
        for material in self.filtered('cost'):            
            material.total_cost = material.quantity * material.cost