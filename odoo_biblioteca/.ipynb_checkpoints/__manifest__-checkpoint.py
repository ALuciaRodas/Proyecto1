# -*- coding: utf-8 -*-

{
    'name': 'Odoo Biblioteca',
    'summary': """App para gestion de biblioteca""",
    'description': """
        Biblioteca module to manage:
        -Books
        -Clients
    """,
    
    'author': 'Odoo',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Biblioteca',
    'version': '0.1',
    
    'depends':     ['base', 'product'],
    
    'data': [
        'views/biblioteca_menuitems.xml',
        'views/book_views.xml',
        'security/biblioteca_security.xml',
        'security/ir.model.access.csv',
        'views/partner_views.xml',
        'views/rental_views.xml',
        'views/author_views.xml',
        'wizard/select_books_views.xml',
        'data/cron.xml',
        'data/mail.xml',
        'data/biblioteca_data.xml',
    ],
    
    'demo': [
        'demo/biblioteca_demo.xml',        
        
    ],
}
