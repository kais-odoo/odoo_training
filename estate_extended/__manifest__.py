{
    'name': 'Real Estate Extended',
    'category': 'Sales',
    'version': '15.0.1.1.0',
    'author': "karan israni",
    'website': 'abc.com',
    'license': 'LGPL-3',
    'summary': 'real estate module',
    'description': """Real Estate module for sales of real estate properties""",
    'application': True,
    'depends' : [
        'estate'
    ],
    'data': [
        'security/ir.model.access.csv',
        #'views/estate_menus.xml',
        'views/estate_property_views.xml',
    ]
}