from odoo import models, fields

class Activity(models.Model):
    _name='schedule.activity'
    _description='Activity'

    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
    employees = fields.Many2many('schedule.employee', string='Employees')
    machinery = fields.Many2many('schedule.machinery', 'activity_machinery_rel', 'machinery_id', 'activity_id', 'Machinery')
    activity_id = fields.Many2one('schedule.construction', string='Construction')