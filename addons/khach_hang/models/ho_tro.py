from odoo import models, fields, api
import random
import string

class HoTro(models.Model):
    _name = 'ho_tro'
    _description = 'Hỗ trợ khách hàng'

    ma_ho_tro = fields.Char(string="Mã hỗ trợ", required=True, readonly=True, default="New")
    khach_hang_id = fields.Many2one('khach_hang', string="Khách hàng", required=True)
    noi_dung = fields.Text(string="Nội dung hỗ trợ")

    nhan_vien_id = fields.Many2one('nhan_vien', string="Nhân viên chăm sóc")

    # Thêm một trường để lưu tên nhân viên chăm sóc
    nhan_vien_name = fields.Char(related="nhan_vien_id.ho_va_ten", string="Tên nhân viên chăm sóc", store=True)

    hinh_thuc_lien_he = fields.Selection([
        ('facebook', 'Facebook'),
        ('zalo', 'Zalo'),
        ('dien_thoai', 'Điện thoại'),
        ('email', 'Email')
    ], string="Hình thức liên hệ")

    cham_soc = fields.Selection([
        ('chua_cham_soc', 'Chưa chăm sóc'),
        ('da_cham_soc', 'Đã chăm sóc')
    ], string="Tình trạng chăm sóc", default='chua_cham_soc')

    _sql_constraints = [
        ('ma_ho_tro_unique', 'unique(ma_ho_tro)', 'Mã hỗ trợ phải là duy nhất!')
    ]

    @api.model
    def create(self, vals):
        if vals.get('ma_ho_tro', 'New') == 'New':
            random_code = ''.join(random.choices(string.digits, k=6))
            vals['ma_ho_tro'] = f"HT{random_code}"
        return super(HoTro, self).create(vals)

    def name_get(self):
        result = []
        for record in self:
            # Sử dụng tên nhân viên chăm sóc đã lấy qua 'nhan_vien_name'
            name = f"{record.ma_ho_tro} - {record.khach_hang_id.ten_khach_hang} - {record.nhan_vien_name}"
            result.append((record.id, name))
        return result
