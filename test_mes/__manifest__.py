# -*- coding: utf-8 -*-
{
    "name": "Test MES",
    "summary": "Test MES",
    "version": "1.0",
    "category": "Hidden",
    # "website": "http://www.gudaotu.com/",
    "author": "kuai he",
    "license": "LGPL-3",
    "depends": [
        'base',
        'web',
        'auth_signup'
    ],
    'auto_install': False,
    "data": [
        'security/ir.model.access.csv',
        'views/mes_menuitem.xml',
        'views/mes_config_views.xml',
        'views/mes_role_views.xml',
        'views/mes_user_views.xml',
        'views/mes_menu_views.xml',
        'views/mes_iframe_action.xml',


    ],



}
