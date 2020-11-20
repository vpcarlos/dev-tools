from xmlrpc import client as xmlrpclib
import decimal


class Odoo():
    def __init__(self, srv, db, user, pwd):
        self.common = xmlrpclib.ServerProxy(
            '{}/xmlrpc/2/common'.format(srv))
        self.api = xmlrpclib.ServerProxy(
            '{}/xmlrpc/2/object'.format(srv))
        self.uid = self.common.authenticate(db, user, pwd, {})
        self.pwd = pwd
        self.db = db

    # odoo.execute('sale.order','compute_last_invoice',[id])
    def execute(self, model, method, params):
        return self.api.execute_kw(self.db, self.uid, self.pwd, model,
                                   method, params)

    def search_read(self, model, domain, fields=[]):
        return self.api.execute_kw(self.db, self.uid, self.pwd, model,
                                   'search_read', [domain, fields])

    # odoo.search('ir.module.module', [[['author', '=', 'admin']]])
    # odoo.search('sale.order',[[]])
    def search(self, model, domain):
        return self.api.execute_kw(self.db, self.uid, self.pwd, model,
                                   'search', domain)

    def write(self, model, values):
        return self.api.execute_kw(self.db, self.uid, self.pwd, model,
                                   'write', values)
    
    def unlink(self, model, id):
        return self.api.execute_kw(self.db, self.uid, self.pwd, model,
                                   'unlink', id)

    def create(self, model, data):
        return self.api.execute_kw(self.db, self.uid, self.pwd, model,
                                   'create', data)
 
    # odoo.read('res.users',[1],['lang'])
    def read(self, model, ids, fields=[]):
        return self.api.execute_kw(self.db, self.uid, self.pwd, model,
                                   'read', ids, fields)
