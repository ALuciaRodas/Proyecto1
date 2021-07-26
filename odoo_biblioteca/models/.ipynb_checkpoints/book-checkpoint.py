# -*- coding: utf-8 -*-

from odoo import models, fields, api

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
    
    @api.onchange('isbn')
    def _onchange_len_isbn(self):
        if len(self.isbn)>13:
            raise ValidationError('El ISBN no puede tener más de 13 caracteres')
