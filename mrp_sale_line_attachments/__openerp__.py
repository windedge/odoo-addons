# -*- coding: utf-8 -*-
{
    'name': "Manufacuring Show Sale Line's Attachments",
    'description': """
Show sale order line's attachments on production.
Inspired by module 'mrp_show_related_attachment'. """,
    'author': "xujl",
    'category': 'Manufacturing',
    'version': '0.1',

    'depends': ['base', 'sale_line_attachments'],

    'data': [
        # 'security/ir.model.access.csv',
        'views.xml',
    ],
    'license': 'LGPL-3'
}
