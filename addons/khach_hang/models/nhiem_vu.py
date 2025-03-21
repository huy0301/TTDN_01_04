from odoo import models, fields

class NhiemVu(models.Model):
    _name = 'nhiem_vu'
    _description = 'Nhiệm Vụ'

    ten_nhiem_vu = fields.Char(string='Tên Nhiệm Vụ', required=True)
    mo_ta = fields.Text(string='Mô Tả')
    ngay_bat_dau = fields.Date(string='Ngày Bắt Đầu')
    han_hoan_thanh = fields.Date(string='Hạn Hoàn Thành')
    muc_do_uu_tien = fields.Selection([
        ('thap', 'Thấp'),
        ('trung_binh', 'Trung Bình'),
        ('cao', 'Cao')
    ], string='Mức Độ Ưu Tiên', default='trung_binh')
    trang_thai = fields.Selection([
        ('chua_bat_dau', 'Chưa Bắt Đầu'),
        ('dang_thuc_hien', 'Đang Thực Hiện'),
        ('da_hoan_thanh', 'Đã Hoàn Thành')
    ], string='Trạng Thái', default='chua_bat_dau')
    
    nguoi_giao_viec_id = fields.Many2one('res.users', string='Người Giao Việc')
    khach_hang_id = fields.Many2one('khach_hang', string='Khách Hàng')
