from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
class Course(models.Model):
    
    _name = 'academy.course'
    _description = 'Curso Info'
    
    name = fields.Char(string='Title', required=True)
    
    description = fields.Char(string='Description')
    
    level = fields.Selection(string='Level', 
                        selection=[('beginner','Beginner'),
                                   ('intermediate','Intermediate'),
                                   ('advanced','Advanced')],
                       copy=False)
    active = fields.Boolean(string='Active', default=True)