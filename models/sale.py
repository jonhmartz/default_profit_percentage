from odoo import api, fields, models

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    default_profit_percentage = fields.Float(
        string='Default Profit %', 
        compute='_compute_default_profit',
        digits=(16, 2),
        help='Default profit percentage from global settings'
    )
    
    @api.depends('product_id')  # O cualquier otra dependencia relevante
    def _compute_default_profit(self):
        for line in self:
            line.default_profit_percentage = float(self.env['ir.config_parameter'].sudo().get_param('profit_percentage.default_value', '20.0'))
    
    @api.model
    def _get_default_profit(self):
        return float(self.env['ir.config_parameter'].sudo().get_param('profit_percentage.default_value', '20.0'))