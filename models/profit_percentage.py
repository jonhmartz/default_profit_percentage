from odoo import api, fields, models

class ProfitPercentageConfig(models.TransientModel):
    _name = 'profit.percentage.config'
    _description = 'Profit Percentage Configuration'
    
    value = fields.Float(
        string='Default Profit Percentage', 
        default=lambda self: self._get_default_value(),
        help='Default percentage to calculate profit margins'
    )
    
    def _get_default_value(self):
        return float(self.env['ir.config_parameter'].sudo().get_param('profit_percentage.default_value', '20.0'))
    
    def set_default(self):
        self.ensure_one()
        self.env['ir.config_parameter'].sudo().set_param('profit_percentage.default_value', str(self.value))
        return {'type': 'ir.actions.client', 'tag': 'reload'}
    
    @api.model
    def get_default_percentage(self):
        return float(self.env['ir.config_parameter'].sudo().get_param('profit_percentage.default_value', '20.0'))