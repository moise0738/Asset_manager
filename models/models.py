from odoo import models, fields, api
from odoo.exceptions import ValidationError


class MaterialCategory(models.Model):
    _name = 'asset_manager.material_category'
    _description = 'Material Category'

    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string='Description')


class Material(models.Model):
    _name = 'asset_manager.material'
    _description = 'Material'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    category_id = fields.Many2one('asset_manager.material_category', string='Category')
    location_id = fields.Many2one('stock.location', string='Location')
    employee_id = fields.Many2one('hr.employee', string='Assigned Employee')
    maintenance_ids = fields.One2many('asset_manager.maintenance', 'material_id', string='Maintenances')


class Maintenance(models.Model):
    _name = 'asset_manager.maintenance'
    _description = 'Maintenance'

    name = fields.Char(string='Name', required=True)
    date = fields.Date(string='Date', required=True)
    cost = fields.Float(string='Cost')
    material_id = fields.Many2one('asset_manager.material', string='Material')
    state = fields.Selection([
        ('todo', 'A Faire'),
        ('in_progress', 'En Cours'),
        ('done', 'Fait')
    ], string='State', default='todo')


class StockLocation(models.Model):
    _name = 'stock.location'
    _description = 'Stock Location'

    name = fields.Char(string='Location Name', required=True)
    description = fields.Text(string='Description')


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    material_ids = fields.One2many('asset_manager.material', 'employee_id', string='Assigned Materials')
