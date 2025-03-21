from odoo import models, fields, api
import random
import string

class KhachHang(models.Model):
    _name = 'khach_hang'
    _description = 'Khách Hàng'

    ma_khach_hang = fields.Char(string='Mã Khách Hàng', required=True, copy=False, readonly=True, default='New')
    ten_khach_hang = fields.Char(string='Tên Khách Hàng', required=True)
    so_dien_thoai = fields.Char(string='Số Điện Thoại')
    dia_chi = fields.Char(string='Địa Chỉ')
    email = fields.Char(string='Email', store=True)
    
    loai_khach_hang = fields.Selection(
        [('ca_nhan', 'Cá Nhân'), ('doanh_nghiep', 'Doanh Nghiệp')],
        string='Loại Khách Hàng',
        required=True,
        default='ca_nhan',
        store=True
    )
    ten_doanh_nghiep = fields.Char(string='Tên Doanh Nghiệp', store=True)
    
    don_hang_ids = fields.One2many('don_hang', 'khach_hang_id', string='Đơn Hàng Đã Mua')
    hop_dong_ids = fields.One2many('hop_dong', 'khach_hang_id', string='Hợp Đồng Đã Ký')

    _sql_constraints = [
        ('ma_khach_hang_uniq', 'unique(ma_khach_hang)', 'Mã khách hàng phải là duy nhất!'),
    ]

    @api.model
    def create(self, vals):
        if vals.get('ma_khach_hang', 'New') == 'New':
            random_code = ''.join(random.choices(string.digits, k=6))  # Tạo mã số 6 chữ số ngẫu nhiên
            vals['ma_khach_hang'] = f'KH{random_code}'
        return super(KhachHang, self).create(vals)

    def name_get(self):
        result = []
        for record in self:
            name = record.ten_khach_hang
            if record.loai_khach_hang == 'doanh_nghiep' and record.ten_doanh_nghiep:
                name += f" ({record.ten_doanh_nghiep})"
            result.append((record.id, name))
        return result
