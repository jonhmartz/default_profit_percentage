from odoo import api, fields, models

class ProfitPercentageConfig(models.Model):
    _name = 'profit.percentage.config'
    _description = 'Profit Percentage Configuration'
    
    value = fields.Float(string='Default Profit Percentage', default=20.0)
    
    @api.model
    def get_default(self):
        config = self.search([], limit=1)
        if not config:
            config = self.create({'value': 20.0})
        return config.value