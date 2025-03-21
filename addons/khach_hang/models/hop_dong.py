from odoo import models, fields, api
import random
import string

class HopDong(models.Model):
    _name = 'hop_dong'
    _description = 'Hợp Đồng'

    ma_hop_dong = fields.Char(string="Mã Hợp Đồng", required=True, readonly=True, copy=False, default='Mới')
    khach_hang_id = fields.Many2one('khach_hang', string="Khách Hàng", required=True)
    ngay_ky = fields.Date(string="Ngày Ký")
    ngay_het_han = fields.Date(string="Ngày Hết Hạn")
    gia_tri = fields.Float(string="Giá Trị Hợp Đồng")
    trang_thai = fields.Selection([
        ('draft', 'Nháp'),
        ('active', 'Đang Hiệu Lực'),
        ('expired', 'Hết Hạn')
    ], string="Trạng Thái", default='draft')

    doanh_thu_id = fields.Many2one('doanh_thu', string="Doanh Thu", ondelete="cascade")

    _sql_constraints = [
        ('ma_hop_dong_unique', 'unique(ma_hop_dong)', 'Mã hợp đồng phải là duy nhất!')
    ]

    @api.model
    def create(self, vals):
        if vals.get('ma_hop_dong', 'Mới') == 'Mới':
            random_code = ''.join(random.choices(string.digits, k=6))
            vals['ma_hop_dong'] = f"HD{random_code}"
        return super(HopDong, self).create(vals)

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.ma_hop_dong} - {record.khach_hang_id.ten_khach_hang}"
            result.append((record.id, name))
        return result
