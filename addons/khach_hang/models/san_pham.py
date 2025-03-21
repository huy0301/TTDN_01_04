from odoo import models, fields, api
import random
import string

class SanPham(models.Model):
    _name = 'san_pham'
    _description = 'Sản Phẩm'

    ma_san_pham = fields.Char(string='Mã Sản Phẩm', required=True, readonly=True, copy=False, default='New')
    ten_san_pham = fields.Char(string='Tên Sản Phẩm', required=True)
    gia = fields.Float(string='Giá', required=True)
    mo_ta = fields.Text(string='Mô Tả')

    _sql_constraints = [
        ('ma_san_pham_uniq', 'unique(ma_san_pham)', 'Mã sản phẩm phải là duy nhất!'),
    ]

    @api.model
    def create(self, vals):
        if vals.get('ma_san_pham', 'New') == 'New':
            vals['ma_san_pham'] = self._generate_random_ma_san_pham()
        return super(SanPham, self).create(vals)

    def _generate_random_ma_san_pham(self):
        while True:
            random_code = 'SP' + ''.join(random.choices(string.digits, k=5))
            if not self.search([('ma_san_pham', '=', random_code)]):
                return random_code

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.ma_san_pham} - {record.ten_san_pham}"
            result.append((record.id, name))
        return result
