# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
class Book(models.Model):
    
    _name = 'biblioteca.book'
    _description = 'Book Info'
    
    name = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author', required=True)
    isbn = fields.Char(string='ISBN', required=True)
    description = fields.Char(string='Description')
    
    state = fields.Selection(string='State', 
                        selection=[('available','Available'),
                                   ('borrowed','Borrowed'),
                                   ('unavailable','Unavailable')],
                       copy=False)
    
    active = fields.Boolean(string='Active', default=True)
    
    renta_ids = fields.One2many(comodel_name='biblioteca.renta', 
                                inverse_name='book_id',
                                string='Rentas')
    
#    @api.onchange()
#    def _onchange_len_isbn(self):
#        if len(self.isbn)>13:
#            raise UserError("El ISBN no puede tener más de 13 caracteres")

            
    @api.constrains('isbn')
    def _check_value_isbn(self):
        if len(self.isbn)>13:
            raise ValidationError("El ISBN no puede tener más de 13 caracteres")