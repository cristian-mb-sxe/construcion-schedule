from odoo import models, fields

class Construction(models.Model):
    _name = 'schedule.construction'
    _description = 'Construction'

    name = fields.Char('Name', required=True)
    deadline = fields.Date('Deadline')
    activities = fields.Many2many('schedule.activity', 'construction_activity_rel', 'construction_id', 'activity_id', string='Activities')
    materials = fields.Many2many('schedule.material', 'construction_material_rel', 'construction_id', 'material_id', string='Material')