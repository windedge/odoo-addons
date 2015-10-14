# -*- coding: utf-8 -*-
{
    'name': "Send message button on topbar",
    'description': """
Just revert the compose message code which is removed from official code base""",
    'author': "xujl",
    'category': 'Base',
    'version': '0.1',

    'depends': ['base', 'mail'],

    'data': [
        # 'security/ir.model.access.csv',
        'template.xml',
    ],
    'qweb':[
        'static/src/xml/mail.xml',
    ]
}
