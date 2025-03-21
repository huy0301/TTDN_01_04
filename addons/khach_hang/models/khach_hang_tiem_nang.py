from odoo import models, fields, api

class KhachHangTiemNang(models.Model):
    _name = 'khach_hang_tiem_nang'
    _description = 'Khách Hàng Tiềm Năng'
    _auto = True

    khach_hang_id = fields.Many2one('khach_hang', string="Khách Hàng", required=True)
    ten_khach_hang = fields.Char(string="Tên Khách Hàng", related="khach_hang_id.ten_khach_hang", store=True)
    so_dien_thoai = fields.Char(string="Số Điện Thoại", related="khach_hang_id.so_dien_thoai", store=True)
    email = fields.Char(string="Email", related="khach_hang_id.email", store=True)
    dia_chi = fields.Char(string="Địa Chỉ", related="khach_hang_id.dia_chi", store=True)
    loai_khach_hang = fields.Selection(
        [('ca_nhan', 'Cá Nhân'), ('doanh_nghiep', 'Doanh Nghiệp')],
        string="Loại Khách Hàng", related="khach_hang_id.loai_khach_hang", store=True
    )

    tinh_trang = fields.Selection([
        ('moi', 'Mới'),
        ('dang_cham_soc', 'Đang Chăm Sóc'),
        ('khong_tiem_nang', 'Không Tiềm Năng')
    ], string="Tình Trạng", default='moi')

    ngay_tao = fields.Datetime(string="Ngày Tạo", default=fields.Datetime.now, readonly=True)
    nhan_vien_phu_trach = fields.Many2one('res.users', string="Nhân Viên Phụ Trách")
    hinh_thuc_lien_he = fields.Selection([
        ('zalo', 'Zalo'),
        ('facebook', 'Facebook'),
        ('dien_thoai', 'Điện Thoại'),
        ('email', 'Email')
    ], string="Hình Thức Liên Hệ")
    ghi_chu = fields.Text(string="Ghi Chú")

    tong_so_don_hang = fields.Integer(string="Tổng Số Đơn Hàng", compute="_compute_tong_so_don_hang", store=True)

    @api.depends('khach_hang_id')
    def _compute_tong_so_don_hang(self):
        for record in self:
            if record.khach_hang_id:
                record.tong_so_don_hang = self.env['don_hang'].search_count([('khach_hang_id', '=', record.khach_hang_id.id)])
            else:
                record.tong_so_don_hang = 0
