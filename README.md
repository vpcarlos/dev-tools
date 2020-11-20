DEV TOOLS
=========

Quick start
-----------
- Replace domain, database, user, password varibales with your own credentials on [main.py](https://github.com/vpcarlos/dev-tools/blob/master/main.py) file.
- Call Odoo class methods and consume Odoo via API.

Finaly just run script ond python3:

    $ python3 main.py

Examples
---------

Search all sale orders:
```python
odoo.search('sale.order',[[]])
```

Uninstall a module via API:
```python
odoo.execute('ir.module.module', 'button_immediate_uninstall', [367])
````

Cancel an specific invoice:
```python
odoo.execute('account.invoice','action_invoice_cancel',[666])
````

Search a record with domain and geting especifics fields:
```python
records = odoo.search_read('sale.order', [['state', '=', 'sale']], ['create_date'])
```

Trigger an onchange function on all records of a specific model:

```python
ids = odoo.search('stock.location',[[]])
for id in ids:
    odoo.execute('stock.location','onchange_picking_location',[id])
```