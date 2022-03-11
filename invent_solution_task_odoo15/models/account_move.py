from odoo import api, models, fields


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    margin = fields.Float(string='Margin',defualt=0)
    discount_amount = fields.Float(string='Discount amount',defualt=0)

    @api.onchange('margin','discount_amount')
    def _compute_amount_residual(self):
        res = super(AccountMoveLine, self)._compute_amount_residual()
        for line in self:
            line.price_subtotal = line.price_subtotal + ((line.margin * line.price_subtotal) / 100) - line.discount_amount
        return res

    # def _onchange_price_subtotal(self):
    #     res = super(AccountMoveLine,self)._onchange_price_subtotal()
    #     for line in self:
    #         line.price_subtotal = line.price_subtotal + ((line.margin * line.price_subtotal) / 100) - line.discount_amount
    #     return res




















    # def write(self,vals):
    #     res = super(AccountMoveLine,self).write(vals)
    #     for line in self:
    #         line.price_subtotal = line.price_subtotal + ((lfrom odoo import api, models, fields


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    margin = fields.Float(string='Margin',defualt=0)
    discount_amount = fields.Float(string='Discount amount',defualt=0)

    @api.onchange('margin','discount_amount')
    def _compute_amount_residual(self):
        res = super(AccountMoveLine, self)._compute_amount_residual()
        for line in self:
            line.price_subtotal = line.price_subtotal + ((line.margin * line.price_subtotal) / 100) - line.discount_amount
        return res

    # def _onchange_price_subtotal(self):
    #     res = super(AccountMoveLine,self)._onchange_price_subtotal()
    #     for line in self:
    #         line.price_subtotal = line.price_subtotal + ((line.margin * line.price_subtotal) / 100) - line.discount_amount
    #     return res




















    # def write(self,vals):
    #     res = super(AccountMoveLine,self).write(vals)
    #     for line in self:
    #         line.price_subtotal = line.price_subtotal + ((line.margin * line.price_subtotal) / 100) - line.discount_amount
    #     return res
    # def _onchange_price_subtotal(self):
    #     res = super(AccountMoveLine,self)._onchange_price_subtotal()
    #     for line in self:
    #         line.price_subtotal = line.price_subtotal + ((line.margin * line.price_subtotal) / 100) - line.discount_amount
    #     return res




