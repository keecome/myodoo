# -*- coding: utf-8 -*-
{
    'name': 'AdminLTE Backend Theme',
    "summary": "Odoo 11.0 community adminlte backend theme",
    'category': 'Themes/Backend',
    'author': '碎石头(360026606@qq),广州救火(7017511@qq),风逍逍(675938238@qq.com)',
    'version': '11.0.1.0.0',
    'description': """        
        odoo10.0主题作者,风逍逍(675938238@qq.com)
        odoo12.0升级:广州救火(7017511@qq),技术总监:碎石头(360026606@qq)
        测试伙伴:晓德(805306265@qq),珠海杜哥(281388879@qq),吊脚楼(124412206@qq),广州救火(7017511@qq),bokit(147796961@qq)
    """,
    'depends': ['web'],
    'data': [
        'views/assets.xml',
        'views/webclient_templates.xml',
    ],
    'qweb': [
        "static/src/xml/base.xml",
    ],
    'auto_install': False

}
