from odoo import fields, models, api, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    margin = fields.Float(string='Margin',defualt=0)
    discount_amount = fields.Float(string='Discount amount',defualt=0)

    @api.depends('margin','discount_amount')
    def _compute_amount(self):
        res = super(SaleOrderLine, self)._compute_amount()
        self.price_subtotal = self.price_subtotal + ((self.margin * self.price_subtotal) / 100) - self.discount_amount
        return res


                                        from odoo import fields, models, api, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    margin = fields.Float(string='Margin',defualt=0)
    discount_amount = fields.Float(string='Discount amount',defualt=0)

    @api.depends('margin','discount_amount')
    def _compute_amount(self):
        res = super(SaleOrderLine, self)._compute_amount()
        self.price_subtotal = self.price_subtotal + ((self.margin * self.price_subtotal) / 100) - self.discount_amount
        return res


