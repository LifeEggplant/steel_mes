# -*- coding: utf-8 -*-

from odoo import api, fields, models

class MesRole(models.Model):
    _name = 'mes.role'
    _description = u'MES Role'

    name = fields.Char(string="角色名称")
    key = fields.Char(string="角色标识")
    status = fields.Boolean(string="是否启用")
    admin = fields.Boolean(string="是否管理员")
    remark = fields.Char(string="备注")
    homepage_path = fields.Char(string="主页地址")

    menu_ids = fields.Many2many(
        comodel_name='mes.menu',
        relation='mes_menu_role_rel', column1='mes_menu_id', column2='mes_role_id',
        string="菜单名称")

    menu_lines = fields.One2many(comodel_name="mes.role.menu.rel", inverse_name="role_id", string="Menu Permissions")



class MesRoleMenuRel(models.Model):
    _name = "mes.role.menu.rel"

    role_id = fields.Many2one(comodel_name="mes.role", string="角色")
    menu_id = fields.Many2one(comodel_name="mes.menu", string="菜单", required=True)
    button_ids = fields.Many2many(comodel_name="mes.menu.button", string="按钮")

    @api.onchange('menu_id')
    def _onchange_menu_id(self):
        if self.menu_id:
            print("menu_id",self.menu_id)
            return {
                'domain': {
                    'button_ids': [('mes_menu_id', '=', self.menu_id.id)]
                }
            }