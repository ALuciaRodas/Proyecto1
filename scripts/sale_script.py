from xmlrpc import client

url = 'https://aluciarodas-proyecto1-odoo-academy-3011774.dev.odoo.com'
db = 'aluciarodas-proyecto1-odoo-academy-3011774'
username = 'admin'
password = ''

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)