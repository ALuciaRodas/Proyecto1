# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Partner(models.Model):
    _inherit = 'res.partner'
    _name = 'biblioteca.partner'
    
    _description = 'Partner Info'
    
    description = fields.Char(string='Description')
    
    is_author = fields.Boolean(string="Is an Author", default=False)
    is_publisher = fields.Boolean(string="Is a Publisher", default=False)
    
    current_rental_ids = fields.One2many('biblioteca.rental', 'customer_id', string='Current Rentals', domain=[('state', '=', 'rented')])
    old_rental_ids = fields.One2many('biblioteca.rental', 'customer_id', string='Old Rentals', domain=[('state', '=', 'returned')])
    lost_rental_ids = fields.One2many('biblioteca.rental', 'customer_id', string='Lost Rentals', domain=[('state', '=', 'lost')])

    book_ids = fields.Many2many("product.product", string="Books", domain=[('is_book', '=', True)])
    copy_ids = fields.Many2many("biblioteca.copy", string="Book Copies")
    nationality_id = fields.Many2one('res.country', 'Nationality')
    birthdate = fields.Date()

    qty_lost_book = fields.Integer(string='Number of book copies lost', compute="_get_lost_books_qty")

    def _get_lost_books_qty(self):
        for rec in self:
            rec.qty_lost_book = len(rec.lost_rental_ids)


