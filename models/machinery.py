from odoo import models, fields

class Machinery(models.Model):
    _name='schedule.machinery'
    _description='Machinery'

    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
