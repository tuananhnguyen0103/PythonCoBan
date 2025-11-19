# Bài 4.1: Chọn kiểu dữ liệu tuple hay list và giải thích

du_lieu = {
    "20_so_nguyen_to_dau_tien": "tuple  # dữ liệu tĩnh, không thay đổi",
    "ten_ngon_ngu_lap_trinh": "list    # có thể thêm ngôn ngữ mới",
    "tuoi_can_nang_chieu_cao": "list    # thay đổi theo thời gian, cần cập nhật",
    "sinh_nhat_va_noi_sinh": "tuple    # thông tin cố định",
    "ket_qua_1_van_bi_a": "tuple      # kết quả cố định của 1 ván",
    "ket_qua_nhieu_van_bi_a": "list     # danh sách có thể thêm ván mới"
}

print("Kết quả bài 4.1:")
for k, v in du_lieu.items():
    print(f"{k}: {v}")
