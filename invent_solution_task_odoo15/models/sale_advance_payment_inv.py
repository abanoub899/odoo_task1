from odoo import fields, models, api, _


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def create_invoices(self):
        res = super(SaleAdvancePaymentInv, self).create_invoices()
        active_order = self.env['sale.order'].browse(self._context.get('active_ids', []))
        active_invoice = self.env['account.move'].browse(self._context.get('active_ids', []))
        orders = self.env['sale.order'].search([])
        invoices = self.env['account.move'].from odoo import fields, models, api, _


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def create_invoices(self):
        res = super(SaleAdvancePaymentInv, self).create_invoices()
        active_order = self.env['sale.order'].browse(self._context.get('active_ids', []))
        active_invoice = self.env['account.move'].browse(self._context.get('active_ids', []))
        orders = self.env['sale.order'].search([])
        invoices = self.env['account.move'].search([])
        for order in orders:
            if order == active_order:
                print('inside active order')
                for invoice in invoices:
                    if invoice == active_invoice:
                        print('inside active invoice')
                        invoice.invoice_line_ids.margin = order.order_line.margin
                        invoice.invoice_line_ids.discount_amount = order.order_line.discount_amount
                        print(invoice.invoice_line_ids.margin)
                        print(invoice.invoice_line_ids.discount_amount)
        return res

