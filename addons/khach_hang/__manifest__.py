# -*- coding: utf-8 -*-
{
    'name': "quan_ly_khach_hang",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','nhan_su'],
    
    # always loaded
   'data': [
    'security/ir.model.access.csv',
    'views/nhiem_vu.xml',
    'views/don_hang.xml',
    'views/ho_tro.xml',
    'views/khach_hang.xml',
    'views/khach_hang_tiem_nang.xml',
    'views/hop_dong.xml',
    'views/san_pham.xml',
    'views/menu.xml',
],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
