# -*- coding: utf-8 -*-

from odoo import api, fields, models

class MesConfig(models.Model):
    _name = 'mes.config'
    _description = u'MES Config'

    name = fields.Char(string="配置名称", default="MES API 连接")
    mes_api_url = fields.Char(string="MES API 地址")
    mes_api_key = fields.Char(string="MES API Key")

