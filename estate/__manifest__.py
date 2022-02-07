{
    'name': 'Real Estate',
    'category': 'Sales',
    'version': '15.0.1.0.0',
    'author': "karan israni",
    'website': 'abc.com',
    'license': 'LGPL-3',
    'summary': 'real estate module',
    'description': """Real Estate module for sales of real estate properties""",
    'application': True,
    'data': [
        'security/estate_security.xml',
        'security/ir.model.access.csv',
        'views/estate_menus.xml',
        'views/estate_property_views.xml',
        'views/estate_templates.xml',
        'wizard/offer_wizard_view.xml',
        'data/estate_property_data.xml',
        
    ],
    'depends': [
        'mail',
        'website',
    ],
}