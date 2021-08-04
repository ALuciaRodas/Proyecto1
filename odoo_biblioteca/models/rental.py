# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Rental(models.Model):
    
    _name = 'biblioteca.rental'
    _order = "rental_date desc,return_date desc"
    _description = 'Rental Info'
    
    description = fields.Char(string='Description')
    
    name = fields.Char(string='Book Title', related='book_id.name')

    customer_id = fields.Many2one('res.partner', string='Customer', domain=[('customer', '=', True)], required=True)
    copy_id = fields.Many2one('biblioteca.copy', string="Book Copy", domain=[('book_state', '=', 'available')], required=True)
    book_id = fields.Many2one('product.product', string='Book', domain=[('is_book', '=', True)], related='copy_id.book_id', readonly=True)

    rental_date = fields.Date(default=fields.Date.context_today, required=True)
    return_date = fields.Date(required=True)
    state = fields.Selection([('draft', 'Draft'), ('rented', 'Rented'), ('returned', 'Returned'), ('lost', 'Lost')], default="draft")

    customer_address = fields.Text(compute='_compute_customer_address')
    customer_email = fields.Char(related='customer_id.email')


#    book_authors = fields.Many2many(related='book_id.author_id')
#    book_edition_date = fields.Date(related='copy_id.edition_date')
 #   book_publisher = fields.Many2one(related='copy_id.publisher_id')

    @api.depends('customer_id')
    def _compute_customer_address(self):
        self.customer_address = self.customer_id.address_get()

    def action_confirm(self):
        for rec in self:
            rec.state = 'rented'
            rec.copy_id.book_state = 'rented'


    def action_return(self):
        for rec in self:
            rec.state = 'returned'
            rec.copy_id.book_state = 'available'

    def action_lost(self):
        for rec in self:
            rec.state = 'lost'
            rec.copy_id.book_state = 'lost'
            rec.copy_id.active = False

    @api.model
    def _cron_check_date(self):
        late_rentals = self.search([('state', '=', 'rented'), ('return_date', '<', fields.Date.today())])
        template_id = self.env.ref('biblioteca.mail_template_book_return')
        for rec in late_rentals:
            mail_id = template_id.send_mail(rec.id)