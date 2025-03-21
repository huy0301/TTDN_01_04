from odoo import models, fields, api
from datetime import datetime


class NhanVien(models.Model):
    _name = 'nhan_vien'
    _description = 'Bảng chứa thông tin nhân viên'

    ma_dinh_danh = fields.Char("Mã định danh", required=True)
    ho_va_ten = fields.Char("Họ và tên", required=True)
    ngay_sinh = fields.Date("Ngày sinh")
    que_quan = fields.Char("Quê quán")
    email = fields.Char("Email")
    so_dien_thoai = fields.Char("Số điện thoại")
    lich_su_cong_tac = fields.One2many("lich_su_cong_tac", 
                                        inverse_name="nhan_vien_id", 
                                        string="Danh sách lịch sử công tác")
    quan_ly_bang_cap = fields.One2many("quan_ly_bang_cap", 
                                        inverse_name="nhan_vien_id", 
                                        string="Danh sách bàng cấp")
    tuoi = fields.Integer("Tuổi", compute="_compute_tinh_tuoi", stoge=True)
    anh = fields.Binary("Ảnh")

    @api.depends("ngay_sinh")
    def _compute_tinh_tuoi(self):
        today = datetime.today()
        for record in self:
            if record.ngay_sinh:
                birth_date = fields.Date.from_string(record.ngay_sinh)
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                record.tuoi = age
            else:
                record.tuoi = 0  # or None if you prefer
                