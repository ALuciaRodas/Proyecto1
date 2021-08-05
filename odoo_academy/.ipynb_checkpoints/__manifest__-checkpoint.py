# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    'summary': """App para gestion de cursos""",
    'description': """
        Modulo para administrar:
        -Cursos
        -Estudiantes
        -Pofesroes
    """,
    
    'author': 'Odoo',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
    ],
    
    'demo': [
      'demo/academy_demo.xml',  
    ],
}
