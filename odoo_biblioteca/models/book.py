# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
class Book(models.Model):
    
    _inherit = 'product.product'
    
    _name = 'biblioteca.book'
    _description = 'Book Info'
    
    description = fields.Char(string='Description')
    
    author_id = fields.Many2one('res.partner', string='Authors', domain=[('is_author', '=', True)])
    edition_date = fields.Date()
    publisher_id = fields.Many2one('res.partner', string='Publisher', domain=[('is_publisher', '=', True)])
    
    name = fields.Char(string='Title', required=True)
    isbn = fields.Char(string='ISBN', required=True)
    
    copy_ids = fields.One2many('biblioteca.copy', 'book_id', string="Book Copies")
    is_book = fields.Boolean(string='Is a Book', default=False)
    
    state = fields.Selection(string='State', 
                        selection=[('available','Available'),
                                   ('rented','Rented'),
                                   ('lost','Lost')],
                       copy=False)
    
    
#    @api.onchange()
#    def _onchange_len_isbn(self):
#        if len(self.isbn)>13:
#            raise UserError("El ISBN no puede tener más de 13 caracteres")

            
    @api.constrains('isbn')
    def _check_value_isbn(self):
        if len(self.isbn)>13:
            raise ValidationError("El ISBN no puede tener más de 13 caracteres")
            
class BookCopy(models.Model):
    _name = 'biblioteca.copy'
    _description = 'Book Copy'
    _rec_name = 'reference'

    book_id = fields.Many2one('product.product', string="Book", domain=[('is_book', "=", True)], required=True, ondelete="cascade", delegate=True)
    reference = fields.Char(required=True, string="Ref")

    rental_ids = fields.One2many('biblioteca.rental', 'copy_id', string='Alquileres')
    book_state = fields.Selection([('available', 'Available'), ('rented', 'Rented'), ('lost', 'Lost')], default="available")
    readers_count = fields.Integer(compute="_compute_readers_count")

    def open_readers(self):
        self.ensure_one()
        reader_ids = self.rental_ids.mapped('customer_id')
        return {
            'name':      'Readers of %s' % (self.name),
            'type':      'ir.actions.act_window',
            'res_model': 'res.partner',
            'view_mode': 'tree,form',
            'view_type': 'form',
            'domain':    [('id', 'in', reader_ids.ids)],
            'target':    'new',
        }

    @api.depends('rental_ids.customer_id')
    def _compute_readers_count(self):
        for book in self:
            book.readers_count = len(book.mapped('rental_ids'))