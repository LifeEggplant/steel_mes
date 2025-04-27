from odoo import models, fields, api
import requests
from ..utils.jwt_utils import get_valid_token
from odoo.exceptions import (
    UserError
)

# MES_API_URL = "http://localhost:8000/ed/api/v1/order/"

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def send_to_mes(self,orders):
        print('销售')
        mes_url = self.env["mes.config"].sudo().search([],limit=1)
        if not mes_url:
            raise UserError("MES URL配置失败")
        for order in orders:
            payload = {
                "order_code": order.name,
                "sap_order_code": order.name,
                "type_of_order": "1"
            }

            token = get_valid_token(self.env.user)
            headers = {"Authorization": f"Bearer {token}"}
            try:
                response = requests.post(mes_url.mes_api_url + '/order/', json=payload, headers=headers)
                response.raise_for_status()
            except Exception as e:
                raise UserError(f"MES同步失败：{e}")


    @api.model_create_multi
    def create(self, vals_list):
        orders = super().create(vals_list)
        self.send_to_mes(orders=orders)
        return orders

    # def write(self, vals):
    #     res = super().write(vals)
    #     self.send_to_mes()
    #     return res