# -*- coding: utf-8 -*-


from odoo import models, fields, api

class Renta(models.Model):
    
    _name = 'biblioteca.renta'
    _description = 'Rental Info'
    
    book_id = fields.Many2one(string='Book', comodel_name='biblioteca.book', ondelete='cascade')

    name = fields.Char(string='Book TItle', related='book_id.name')

    customer_id = fields.Many2one(comodel_name='res.partner', string='Customer')
    
    description = fields.Char(string='Description')