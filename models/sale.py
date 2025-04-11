from odoo import api, fields, models

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    default_profit_percentage = fields.Float(
        string='Default Profit %', 
        default=20.0,  # Valor predeterminado fijo inicial
        digits=(16, 2),
        help='Default profit percentage from global settings'
    )
    
    @api.model
    def _get_default_profit(self):
        # Acceder directamente al parámetro en lugar de usar la clase
        return float(self.env['ir.config_parameter'].sudo().get_param('profit_percentage.default_value', '20.0'))
    
    # Añadir este método para actualizar el valor cuando cambie
    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for record in records:
            # Actualizamos el valor después de crear el registro
            default_profit = float(self.env['ir.config_parameter'].sudo().get_param('profit_percentage.default_value', '20.0'))
            record.default_profit_percentage = default_profit
        return records