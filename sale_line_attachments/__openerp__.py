# -*- coding: utf-8 -*-
{
    'name': "Sale Order Line Attachments",
    'author': "xujl",
    'description':"""
    This module add a new filed on sale order line that allows to upload attachments.""",
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views.xml',
    ],
    'license': 'LGPL-3'
}