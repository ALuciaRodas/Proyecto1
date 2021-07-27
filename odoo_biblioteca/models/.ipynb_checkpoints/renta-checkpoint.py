# -*- coding: utf-8 -*-


from odoo import models, fields, api

class Renta(models.Model):
    
    _name = 'biblioteca.renta'
    _description = 'Rental Info'
    
    name = fields.Char(string='Title', required=True)
    description = fields.Char(string='Description')