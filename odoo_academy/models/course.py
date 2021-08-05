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
    
    base_price = fields.Float(string='Base Price', default=0.00)
    
    additional_fee = fields.Float(string='Additional Fee', default=0.00)
    
    total_price = fields.Float(string='Total Price', readonly=True)
    
    session_ids = fields.One2many(comodel_name='academy.session',
                                   inverse_name='course_id',
                                   string='Course')

    @api.onchange('base_price', 'additional_fee')
    def _onchange_total_price(self):
        if self.base_price<0.00:
            raise UserError("El precio base no puede ser negativo")

            
    @api.constrains('additional_fee')
    def _check_aditional_fee(self):
        for record in self:
            if record.additional_fee<10.00:
                raise ValidationError('La tarifa adicional no puede ser menor a 10.00: %s' %record.additional_fee)