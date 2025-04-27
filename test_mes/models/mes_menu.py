# -*- coding: utf-8 -*-

from odoo import api, fields, models

class MesMenu(models.Model):
    _name = 'mes.menu'
    _description = u'MES Menu'

    name = fields.Char(string="菜单名称")
    title = fields.Char(string="菜单标识")
    sort = fields.Integer(string="排序")
    icon = fields.Char(string="icon")

    is_link = fields.Boolean(string="是否外链")
    is_catalog = fields.Boolean(string="是否目录")
    web_path = fields.Char(string="路由地址")
    component = fields.Char(string="组件")
    component_name = fields.Char(string="组件名称")
    status = fields.Boolean(string="菜单状态")
    visible = fields.Boolean(string="侧边栏中是否显示")
    desc = fields.Char(string="备注")

    parent_id = fields.Many2one(
        comodel_name='mes.menu',
        string='父级菜单'
    )

    button_ids = fields.One2many(
        comodel_name='mes.menu.button',
        inverse_name='mes_menu_id',
        string='菜单按钮'
    )



class MesMenuButton(models.Model):
    _name = 'mes.menu.button'
    _description = u'MES Menu Button'

    name = fields.Char(string="按钮名称")

    mes_menu_id = fields.Many2one(
        comodel_name='mes.menu',
        string='菜单'
    )

