{
    'name': 'Default Profit Percentage',
    'version': '1.0',
    'summary': 'Set default profit percentage',
    'description': """
        Configure a system-wide default profit percentage.
    """,
    'category': 'Sales',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/profit_percentage_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}