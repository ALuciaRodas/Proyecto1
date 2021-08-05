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
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'security/academy_security.xml',
        'security/ir.model.access.csv',
    ],
    
    'demo': [
      'demo/academy_demo.xml',  
    ],
}
