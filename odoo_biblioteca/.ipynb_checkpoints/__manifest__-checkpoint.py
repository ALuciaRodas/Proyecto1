# -*- coding: utf-8 -*-

{
    'name': 'Odoo Biblioteca',
    'summary': """App para gestion de biblioteca""",
    'description': """
        Biblioteca module to manage Training:
        -Books
        -Clients
    """,
    
    'author': 'Odoo',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Biblioteca',
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'views/biblioteca_menuitems.xml',
        'views/book_views.xml',
        'security/ir.model.access.csv'
        
    ],
    
    'demo': [
        'demo/biblioteca_demo.xml',        
        
    ],
}
