from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    default_profit_percentage = fields.Float(
        string='Default Profit Percentage',
        default=20.0,
        config_parameter='default_profit_percentage.value',
        help='Default percentage to calculate profit margins across the system'
    )

class ProfitPercentageHelper(models.Model):
    _name = 'profit.percentage.helper'
    _description = 'Profit Percentage Helper'

    @api.model
    def get_default_percentage(self):
        """Get the default profit percentage value from system parameters"""
        return float(self.env['ir.config_parameter'].sudo().get_param('default_profit_percentage.value', 20.0))