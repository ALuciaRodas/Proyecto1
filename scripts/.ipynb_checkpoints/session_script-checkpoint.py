from xmlrpc import client

url = 'https://aluciarodas-proyecto1-odoo-academy-3011774.dev.odoo.com'
db = 'aluciarodas-proyecto1-odoo-academy-3011774'
username = 'admin'
password = 'admin'#no poseo las credenciales correctas

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access = models.execute_kw(db, uid, password,
                                'academy.session', 'check_access_rights',
                                ['write'],{'raise_exception':False})

print(model_access)

courses = models.execute_kw(db, uid, password,
                                'academy.course', 'search',
                                [[['name','=','ERP101']]])

print(course)

session_fields = models.execute_kw(db, uid, password,
                                'academy.session', 'field_get',
                                [],{'attributes':['string','type','required']})

print(session_fields)     

new_session = models.execute(db, uid, password,
                                'academy.session', 'create',
                             [
                                 {
                                     'course_id':course[0],
                                     'state':'open',
                                     'duration':5,
                                 }
                             ]
                            )

print(new_session)     