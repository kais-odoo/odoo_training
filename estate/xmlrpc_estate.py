import xmlrpc.client

db = "training"
username = "admin"
password = "admin"

common = xmlrpc.client.ServerProxy('http://localhost:8069/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})

if uid:
    print ("Connection Successful")

models = xmlrpc.client.ServerProxy('http://localhost:8069/xmlrpc/2/object')

result = models.execute_kw(db, uid, password, 'estate.property', 'search_read', [[], ['name', 'description']])

print ("\n\nresult is ::: ", result)