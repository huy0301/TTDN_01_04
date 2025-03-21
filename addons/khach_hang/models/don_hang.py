from odoo import models, fields, api
import random
import string

class DonHang(models.Model):
    _name = 'don_hang'
    _description = 'Đơn Hàng'

    ma_don_hang = fields.Char(string='Mã Đơn Hàng', required=True, readonly=True, copy=False, default='New')
    khach_hang_id = fields.Many2one('khach_hang', string='Khách Hàng', required=True)
    san_pham_id = fields.Many2one('san_pham', string='Sản Phẩm', required=True)
    so_luong = fields.Integer(string='Số Lượng', required=True, default=1)
    tong_tien = fields.Float(string='Tổng Tiền', compute='_compute_tong_tien', store=True)
    ghi_chu = fields.Text(string='Ghi Chú')

    ngay_ban = fields.Date(string='Ngày Bán', default=fields.Date.today)
    nguoi_ban_id = fields.Many2one('res.users', string='Người Bán', default=lambda self: self.env.user)

    @api.depends('so_luong', 'san_pham_id')
    def _compute_tong_tien(self):
        for record in self:
            record.tong_tien = record.so_luong * record.san_pham_id.gia

    @api.model
    def create(self, vals):
        if vals.get('ma_don_hang', 'New') == 'New':
            random_code = ''.join(random.choices(string.digits, k=6))  # Sinh chuỗi số ngẫu nhiên 6 chữ số
            vals['ma_don_hang'] = 'DH' + random_code
        return super(DonHang, self).create(vals)
