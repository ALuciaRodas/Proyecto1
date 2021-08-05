from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
class Curso(models.Model):
    
    _name = 'academy.curso'
    _description = 'Curso Info'
