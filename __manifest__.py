# -*- coding: utf-8 -*-
{
    'name': "asset_manager",

    'summary': "Gestion des ressources matérielles",

    'description': """
Module de gestion des ressources matérielles pour suivre et gérer les équipements, machines et autres actifs matériels de l'entreprise.
    """,

    'author': "Your Company",
    'website': "https://www.yourcompany.com",
    'application': True,
    'installable': True,
    'auto_install': False,

    'category': 'Operations/Inventory',

    'version': '0.1',

    'depends': ['base', 'hr'],


    'data': [
        'security/asset_manager_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        #'views/website_material_list_template'
    ],

    'demo': [
        'demo/demo.xml',
    ],
}
