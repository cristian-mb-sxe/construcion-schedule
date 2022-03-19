from unicodedata import name
from odoo import models, fields

class Employee(models.Model):
    _name = 'schedule.employee'
    _inherits = {'res.partner' : 'partner_id'}

    partner_id = fields.Many2one('res.partner', ondelete='cascade')
