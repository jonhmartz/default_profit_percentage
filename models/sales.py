from odoo import api, fields, models

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    default_profit_percentage = fields.Float(
        string='Default Profit %', 
        default=lambda self: self._get_default_profit(),
        digits=(16, 2),
        help='Default profit percentage from global settings'
    )
    
    @api.model
    def _get_default_profit(self):
        return self.env['profit.percentage.config'].get_default_percentage()