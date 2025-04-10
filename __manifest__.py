{
    'name': 'Default Profit Percentage',
    'version': '1.0',
    'summary': 'Set default profit percentage',
    'description': """
        Configure a system-wide default profit percentage and add it to sales order lines.
    """,
    'category': 'Sales',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'sale'],  # Añadimos la dependencia de 'sale'
    'data': [
        'security/ir.model.access.csv',
        'views/profit_percentage_view.xml',
        'views/sale_views.xml',  # Nuevo archivo para las vistas de ventas
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}