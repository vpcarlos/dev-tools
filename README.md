EXPAMPLES

    # ----- Trigger an onchange function on all records of a specific model
    # ids = odoo.search('stock.location',[[]])
    # for id in ids:
    #     odoo.execute('stock.location','onchange_picking_location',[id])

    # ----- Uninstall a module via API
    # odoo.execute('ir.module.module', 'button_immediate_uninstall', [367])

    # ----- Cancel a invoice
    # odoo.execute('account.invoice','action_invoice_cancel',[666])

    # ----- Search a record with domain and geting especifics fields
    #  records = odoo.search_read(
    #    'sale.order', [['state', '=', 'sale']], ['create_date'])