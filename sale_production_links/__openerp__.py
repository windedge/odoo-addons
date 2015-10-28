# -*- coding: utf-8 -*-
{
    'name': "Sale Order to Manufacturing Order",
    'description': """
Add relation between Manufacturing Order and Sale Order
    """,
    'author': "xujl",
    'category': 'Manufacturing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'mrp'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views.xml',
    ],
    'images': [
        'static/description/sale_production_links.png'
    ],
}
