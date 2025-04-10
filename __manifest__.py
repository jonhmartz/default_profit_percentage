{
    'name': 'Default Profit Percentage',
    'version': '1.0',
    'summary': 'Set default profit percentage',
    'description': """
        Configure a system-wide default profit percentage
        that can be used across the application.
    """,
    'category': 'Sales',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base'],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}