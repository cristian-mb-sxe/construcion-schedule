# -*- coding: utf-8 -*-
{
    'name': "Contruction Schedule",

    'summary': """
        Steps, material, staff and anything related to constructions""",

    'description': """
        This a module conceived for writting down the steps, material, staff and anything related to constructions for any construction chief
    """,

    'author': "a20cristianmb",
    'website': "https://gitlab.com/a20cristianmb/",
    'application': "true",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/contructions.xml',
        'views/machinery.xml',
        'views/materials.xml',
        'views/activities.xml',
        'views/employees.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
