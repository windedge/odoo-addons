# -*- coding: utf-8 -*-
{
    'name': "Stock Move Show Sale Line's Attachments",

    'description': """
In the stock form view, show the related sale order line's attachments
    """,

    'author': "xujl",
    'category': 'Inventory',
    'version': '0.1',

    'depends': ['base', 'stock', 'sale_line_attachments'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views.xml',
    ],
}
