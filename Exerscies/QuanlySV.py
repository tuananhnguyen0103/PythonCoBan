import os
import re


# ========== CLASS ĐỊNH NGHĨA ==========
class SinhVien:
    def __init__(self, ma_sv, ho_ten, gioi_tinh, nam_sinh, dia_chi, so_dt, email):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.gioi_tinh = gioi_tinh
        self.nam_sinh = nam_sinh
        self.dia_chi = dia_chi
        self.so_dt = so_dt
        self.email = email


class HocPhan:
    def __init__(self, ma_hp, ten_hp, loai_hp, so_tin_chi):
        self.ma_hp = ma_hp
        self.ten_hp = ten_hp
        self.loai_hp = loai_hp
        self.so_tin_chi = so_tin_chi


class BangDiem:
    def __init__(self, ma_sv, ma_hp, lan_thi, diem_hp):
        self.ma_sv = ma_sv
        self.ma_hp = ma_hp
        self.lan_thi = lan_thi
        self.diem_hp = diem_hp


# ========== BIẾN TOÀN CỤC ==========
danh_sach_sv = []
danh_sach_hp = []
danh_sach_diem = []


# ========== HÀM KIỂM TRA DỮ LIỆU ==========
def kiem_tra_ma_sv(ma_sv):
    for sv in danh_sach_sv:
        if sv.ma_sv == ma_sv:
            return False
    return True


def kiem_tra_ho_ten(ho_ten):
    return bool(ho_ten) and ho_ten.replace(" ", "").isalpha()


def kiem_tra_gioi_tinh(gt):
    return gt in ["Nam", "Nu"]


def kiem_tra_nam_sinh(nam):
    return int(nam) < 2003


def kiem_tra_sdt(sdt):
    return len(sdt) == 10 and sdt.isdigit()


def kiem_tra_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def kiem_tra_ma_hp(ma_hp):
    for hp in danh_sach_hp:
        if hp.ma_hp == ma_hp:
            return False
    return True


def kiem_tra_ten_hp(ten_hp):
    return bool(ten_hp) and ten_hp.replace(" ", "").isalnum()


def kiem_tra_loai_hp(loai):
    return loai in ["ĐC", "CSN", "CN", "ĐA", "TT"]


def kiem_tra_tin_chi(tc):
    try:
        return 0 < float(tc) <= 10
    except:
        return False


def kiem_tra_lan_thi(lt):
    return lt in ["1", "2", "3"]


def kiem_tra_diem(diem):
    try:
        return 0 <= float(diem) <= 10
    except:
        return False


def kiem_tra_ma_sv_ton_tai(ma_sv):
    for sv in danh_sach_sv:
        if sv.ma_sv == ma_sv:
            return True
    return False


def kiem_tra_ma_hp_ton_tai(ma_hp):
    for hp in danh_sach_hp:
        if hp.ma_hp == ma_hp:
            return True
    return False


def kiem_tra_trung_diem(ma_sv, ma_hp, lan_thi):
    for d in danh_sach_diem:
        if d.ma_sv == ma_sv and d.ma_hp == ma_hp and d.lan_thi == lan_thi:
            return False
    return True


# ========== HÀM NHẬP DỮ LIỆU ==========
def nhap_sinh_vien():
    print("\n=== NHẬP SINH VIÊN ===")
    while True:
        ma_sv = input("Mã SV (hoặc 'stop' để dừng): ")
        if ma_sv.lower() == 'stop':
            break
        while True:
            if not kiem_tra_ma_sv(ma_sv):
                print("Mã SV đã tồn tại!")
                ma_sv = input("Nhập lại Mã SV: ")
            else:
                break

        ho_ten = input("Họ tên: ")
        while True:
            if not kiem_tra_ho_ten(ho_ten):
                print("Họ tên không hợp lệ!")
                ho_ten = input("Nhập lại Họ tên: ")
            else:
                break

        gioi_tinh = input("Giới tính (Nam/Nu): ")
        while True:
            if not kiem_tra_gioi_tinh(gioi_tinh):
                print("Giới tính không hợp lệ!")
                gioi_tinh = input("Nhập lại Giới tính (Nam/Nu): ")
            else:
                break

        nam_sinh = input("Năm sinh (trước 2003): ")
        while True:
            if not kiem_tra_nam_sinh(nam_sinh):
                print("Năm sinh không hợp lệ!")
                nam_sinh = input("Nhập lại Năm sinh (trước 2003): ")
            else:
                break

        dia_chi = input("Địa chỉ: ")
        so_dt = input("Số điện thoại (10 số): ")
        while True:
            if not kiem_tra_sdt(so_dt):
                print("Số điện thoại không hợp lệ!")
                so_dt = input("Số điện thoại (10 số): ")
            else:
                break

        email = input("Email: ")
        while True:
            if not kiem_tra_email(email):
                print("Email không hợp lệ!")
                email = input("Email: ")
            else:
                break

        sv = SinhVien(ma_sv, ho_ten, gioi_tinh, nam_sinh, dia_chi, so_dt, email)
        danh_sach_sv.append(sv)
        print("Đã thêm sinh viên!")


def nhap_hoc_phan():
    print("\n=== NHẬP HỌC PHẦN ===")
    while True:
        ma_hp = input("Mã HP (hoặc 'stop' để dừng): ")
        if ma_hp.lower() == 'stop':
            break
        while True:
            if not kiem_tra_ma_hp(ma_hp):
                print("Mã HP đã tồn tại!")
                ma_hp = input("Mã HP: ")
            else:
                break

        ten_hp = input("Tên học phần: ")
        while True:
            if not kiem_tra_ten_hp(ten_hp):
                print("Tên học phần không hợp lệ!")
                ten_hp = input("Tên học phần: ")
            else:
                break

        loai_hp = input("Loại HP (ĐC/CSN/CN/ĐA/TT): ")
        while True:
            if not kiem_tra_loai_hp(loai_hp):
                print("Loại học phần không hợp lệ!")
                loai_hp = input("Loại HP (ĐC/CSN/CN/ĐA/TT): ")
            else:
                break

        so_tin_chi = input("Số tín chỉ (0 < x <= 10): ")
        while True:
            if not kiem_tra_tin_chi(so_tin_chi):
                print("Số tín chỉ không hợp lệ!")
                so_tin_chi = input("Số tín chỉ (0 < x <= 10): ")
            else:
                break

        hp = HocPhan(ma_hp, ten_hp, loai_hp, float(so_tin_chi))
        danh_sach_hp.append(hp)
        print("Đã thêm học phần!")


def nhap_bang_diem():
    print("\n=== NHẬP BẢNG ĐIỂM ===")
    while True:
        ma_sv = input("Mã SV (hoặc 'stop' để dừng): ")
        if ma_sv.lower() == 'stop':
            break
        while True:
            if not kiem_tra_ma_sv_ton_tai(ma_sv):
                print("Mã SV không tồn tại!")
                ma_sv = input("Mã SV: ")
            else:
                break

        ma_hp = input("Mã HP: ")
        while True:
            if not kiem_tra_ma_hp_ton_tai(ma_hp):
                print("Mã HP không tồn tại!")
                ma_hp = input("Mã HP: ")
            else:
                break

        lan_thi = input("Lần thi (1/2/3): ")
        while True:
            if not kiem_tra_lan_thi(lan_thi):
                print("Lần thi không hợp lệ!")
                lan_thi = input("Lần thi (1/2/3): ")
            else:
                break

        if not kiem_tra_trung_diem(ma_sv, ma_hp, lan_thi):
            print("Đã tồn tại bản ghi với mã SV, mã HP và lần thi này!")
            continue

        diem_hp = input("Điểm học phần (0-10): ")
        while True:
            if not kiem_tra_diem(diem_hp):
                print("Điểm không hợp lệ!")
                diem_hp = input("Điểm học phần (0-10): ")
            else:
                break

        bd = BangDiem(ma_sv, ma_hp, lan_thi, float(diem_hp))
        danh_sach_diem.append(bd)
        print("Đã thêm điểm!")


# ========== HÀM LƯU FILE ==========
def luu_file_sv():
    with open("sinhvien.txt", "w", encoding="utf-8") as f:
        f.write("Mã SV,Họ tên,Giới tính,Năm sinh,Địa chỉ,SĐT,Email\n")
        for sv in danh_sach_sv:
            f.write(f"{sv.ma_sv},{sv.ho_ten},{sv.gioi_tinh},{sv.nam_sinh},{sv.dia_chi},{sv.so_dt},{sv.email}\n")
    print("Đã lưu sinhvien.txt")


def luu_file_hp():
    with open("hocphan.txt", "w", encoding="utf-8") as f:
        f.write("Mã HP,Tên HP,Loại HP,Số TC\n")
        for hp in danh_sach_hp:
            f.write(f"{hp.ma_hp},{hp.ten_hp},{hp.loai_hp},{hp.so_tin_chi}\n")
    print("Đã lưu hocphan.txt")


def luu_file_diem():
    with open("bangdiem.txt", "w", encoding="utf-8") as f:
        f.write("Mã SV,Mã HP,Lần thi,Điểm\n")
        for d in danh_sach_diem:
            f.write(f"{d.ma_sv},{d.ma_hp},{d.lan_thi},{d.diem_hp}\n")
    print("Đã lưu bangdiem.txt")


# ========== HÀM ĐỌC FILE ==========
def doc_file_sv():
    if not os.path.exists("sinhvien.txt"):
        return
    with open("sinhvien.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()[1:]  # Bỏ dòng tiêu đề
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) == 7:
                sv = SinhVien(*parts)
                danh_sach_sv.append(sv)


def doc_file_hp():
    if not os.path.exists("hocphan.txt"):
        return
    with open("hocphan.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()[1:]
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) == 4:
                hp = HocPhan(parts[0], parts[1], parts[2], float(parts[3]))
                danh_sach_hp.append(hp)


def doc_file_diem():
    if not os.path.exists("bangdiem.txt"):
        return
    with open("bangdiem.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()[1:]
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) == 4:
                bd = BangDiem(parts[0], parts[1], parts[2], float(parts[3]))
                danh_sach_diem.append(bd)


# ========== HÀM HIỂN THỊ ==========
def hien_thi_sv():
    print("\n=== DANH SÁCH SINH VIÊN ===")
    print(f"{'Mã SV':<10} {'Họ tên':<20} {'Giới tính':<10} {'Năm sinh':<10} {'Địa chỉ':<20} {'SĐT':<12} {'Email':<20}")
    for sv in danh_sach_sv:
        print(
            f"{sv.ma_sv:<10} {sv.ho_ten:<20} {sv.gioi_tinh:<10} {sv.nam_sinh:<10} {sv.dia_chi:<20} {sv.so_dt:<12} {sv.email:<20}")


def hien_thi_hp():
    print("\n=== DANH SÁCH HỌC PHẦN ===")
    print(f"{'Mã HP':<10} {'Tên HP':<30} {'Loại HP':<10} {'Số TC':<6}")
    for hp in danh_sach_hp:
        print(f"{hp.ma_hp:<10} {hp.ten_hp:<30} {hp.loai_hp:<10} {hp.so_tin_chi:<6.1f}")


def hien_thi_diem():
    print("\n=== BẢNG ĐIỂM CHI TIẾT ===")
    print(
        f"{'Mã SV':<10} {'Họ tên':<20} {'Giới tính':<10} {'Năm sinh':<10} {'Mã HP':<10} {'Tên HP':<30} {'Số TC':<6} {'Lần thi':<8} {'Điểm':<5}")
    for d in danh_sach_diem:
        sv_info = next((sv for sv in danh_sach_sv if sv.ma_sv == d.ma_sv), None)
        hp_info = next((hp for hp in danh_sach_hp if hp.ma_hp == d.ma_hp), None)
        if sv_info and hp_info:
            print(
                f"{sv_info.ma_sv:<10} {sv_info.ho_ten:<20} {sv_info.gioi_tinh:<10} {sv_info.nam_sinh:<10} {hp_info.ma_hp:<10} {hp_info.ten_hp:<30} {hp_info.so_tin_chi:<6.1f} {d.lan_thi:<8} {d.diem_hp:<5.1f}")


def hien_thi_hoc_lai():
    print("\n=== SINH VIÊN PHẢI HỌC LẠI (điểm lần 1 < 5) ===")
    print(f"{'Mã SV':<10} {'Họ tên':<20} {'Mã HP':<10} {'Tên HP':<30} {'Điểm lần 1':<10}")
    for d in danh_sach_diem:
        if d.lan_thi == "1" and d.diem_hp < 5:
            sv_info = next((sv for sv in danh_sach_sv if sv.ma_sv == d.ma_sv), None)
            hp_info = next((hp for hp in danh_sach_hp if hp.ma_hp == d.ma_hp), None)
            if sv_info and hp_info:
                print(
                    f"{sv_info.ma_sv:<10} {sv_info.ho_ten:<20} {hp_info.ma_hp:<10} {hp_info.ten_hp:<30} {d.diem_hp:<10.1f}")


def hien_thi_diem_trung_binh():
    print("\n=== ĐIỂM TRUNG BÌNH CHUNG LẦN 1 ===")
    print(f"{'Mã SV':<10} {'Họ tên':<20} {'Giới tính':<10} {'Năm sinh':<10} {'Điểm TB':<8}")
    for sv in danh_sach_sv:
        tong_diem_tin = 0
        tong_tin = 0
        for d in danh_sach_diem:
            if d.ma_sv == sv.ma_sv and d.lan_thi == "1":
                hp_info = next((hp for hp in danh_sach_hp if hp.ma_hp == d.ma_hp), None)
                if hp_info:
                    tong_diem_tin += d.diem_hp * hp_info.so_tin_chi
                    tong_tin += hp_info.so_tin_chi
        if tong_tin > 0:
            dtb = tong_diem_tin / tong_tin
            print(f"{sv.ma_sv:<10} {sv.ho_ten:<20} {sv.gioi_tinh:<10} {sv.nam_sinh:<10} {dtb:<8.2f}")


def hien_thi_hoc_bong():
    print("\n=== SINH VIÊN ĐỦ ĐIỀU KIỆN HỌC BỔNG (ĐTB >=7 và không học lại) ===")
    print(f"{'Mã SV':<10} {'Họ tên':<20} {'Giới tính':<10} {'Năm sinh':<10} {'Điểm TB':<8}")
    for sv in danh_sach_sv:
        # Tính điểm TB lần 1
        tong_diem_tin = 0
        tong_tin = 0
        for d in danh_sach_diem:
            if d.ma_sv == sv.ma_sv and d.lan_thi == "1":
                hp_info = next((hp for hp in danh_sach_hp if hp.ma_hp == d.ma_hp), None)
                if hp_info:
                    tong_diem_tin += d.diem_hp * hp_info.so_tin_chi
                    tong_tin += hp_info.so_tin_chi
        if tong_tin > 0:
            dtb = tong_diem_tin / tong_tin
            # Kiểm tra không có môn học lại (điểm lần 1 < 5)
            co_hoc_lai = False
            for d in danh_sach_diem:
                if d.ma_sv == sv.ma_sv and d.lan_thi == "1" and d.diem_hp < 5:
                    co_hoc_lai = True
                    break
            if dtb >= 7 and not co_hoc_lai:
                print(f"{sv.ma_sv:<10} {sv.ho_ten:<20} {sv.gioi_tinh:<10} {sv.nam_sinh:<10} {dtb:<8.2f}")


# ========== MENU CHÍNH ==========
def main():
    # Đọc dữ liệu cũ từ file
    doc_file_sv()
    doc_file_hp()
    doc_file_diem()

    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ SINH VIÊN =====")
        print("a. Nhập và lưu sinh viên")
        print("b. Nhập và lưu học phần")
        print("c. Nhập và lưu bảng điểm")
        print("d. Hiển thị sinh viên")
        print("e. Hiển thị học phần")
        print("f. Hiển thị bảng điểm chi tiết")
        print("g. Hiển thị sinh viên học lại")
        print("h. Hiển thị điểm trung bình lần 1")
        print("i. Hiển thị sinh viên đủ điều kiện học bổng")
        print("0. Thoát")

        chon = input("Chọn chức năng: ").strip().lower()

        if chon == 'a':
            nhap_sinh_vien()
            luu_file_sv()
        elif chon == 'b':
            nhap_hoc_phan()
            luu_file_hp()
        elif chon == 'c':
            nhap_bang_diem()
            luu_file_diem()
        elif chon == 'd':
            hien_thi_sv()
        elif chon == 'e':
            hien_thi_hp()
        elif chon == 'f':
            hien_thi_diem()
        elif chon == 'g':
            hien_thi_hoc_lai()
        elif chon == 'h':
            hien_thi_diem_trung_binh()
        elif chon == 'i':
            hien_thi_hoc_bong()
        elif chon == '0':
            print("Thoát chương trình!")
            break
        else:
            print("Chức năng không hợp lệ!")


if __name__ == "__main__":
    main()