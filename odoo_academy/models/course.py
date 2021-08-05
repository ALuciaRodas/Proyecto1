from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
class Course(models.Model):
    
    _name = 'academy.course'
    _description = 'Curso Info'
