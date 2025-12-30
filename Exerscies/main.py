# main.py
# Bài tập thực hành tổng hợp (a -> i)
# Lưu dữ liệu vào: sinhvien.txt, hocphan.txt, bangdiem.txt
# Định dạng mỗi dòng: các trường ngăn bởi dấu |

import os
import re

SV_FILE = "sinhvien.txt"
HP_FILE = "hocphan.txt"
BD_FILE = "bangdiem.txt"

DELIM = "|"
HP_TYPES = {"ĐC", "CSN", "CN", "ĐA", "TT"}


# ---------------------------
# Helpers: đọc / ghi file
# ---------------------------
def ensure_file(path: str):
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write("")


def write_rows(path: str, rows: list[list[str]]):
    ensure_file(path)
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(DELIM.join(map(str, r)) + "\n")


def append_row(path: str, row: list[str]):
    ensure_file(path)
    with open(path, "a", encoding="utf-8") as f:
        f.write(DELIM.join(map(str, row)) + "\n")


def read_rows(path: str) -> list[list[str]]:
    ensure_file(path)
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(line.split(DELIM))
    return rows


# ---------------------------
# Validation
# ---------------------------
def is_valid_name(name: str) -> bool:
    """Họ tên: khác rỗng, không chứa ký tự đặc biệt (chỉ chữ + khoảng trắng)."""
    name = name.strip()
    if not name:
        return False
    # Cho phép chữ tiếng Việt + khoảng trắng
    return re.fullmatch(r"[A-Za-zÀ-ỹ\s]+", name) is not None


def is_valid_gender(g: str) -> bool:
    return g in {"Nam", "Nu"}


def is_valid_birth_year(y: str) -> bool:
    if not y.isdigit():
        return False
    return int(y) < 2003


def is_valid_phone(p: str) -> bool:
    return p.isdigit() and len(p) == 10


def is_valid_email(email: str) -> bool:
    # username@Domain1.Domain2 (tối thiểu 2 phần domain)
    # Ví dụ: abc@utehy.edu.vn
    return re.fullmatch(r"[\w\.-]+@[\w-]+(\.[\w-]+)+", email) is not None


def is_float_number(s: str) -> bool:
    try:
        float(s)
        return True
    except:
        return False


# ---------------------------
# Load dữ liệu thành dict
# ---------------------------
def load_students() -> list[dict]:
    rows = read_rows(SV_FILE)
    data = []
    for r in rows:
        # ma|ten|gt|ns|dc|sdt|email
        if len(r) != 7:
            continue
        data.append(
            {
                "ma": r[0],
                "ten": r[1],
                "gt": r[2],
                "ns": r[3],
                "dc": r[4],
                "sdt": r[5],
                "email": r[6],
            }
        )
    return data


def load_courses() -> list[dict]:
    rows = read_rows(HP_FILE)
    data = []
    for r in rows:
        # mahp|tenhp|loai|tc
        if len(r) != 4:
            continue
        data.append({"mahp": r[0], "tenhp": r[1], "loai": r[2], "tc": r[3]})
    return data


def load_scores() -> list[dict]:
    rows = read_rows(BD_FILE)
    data = []
    for r in rows:
        # masv|mahp|lan|diem
        if len(r) != 4:
            continue
        data.append({"masv": r[0], "mahp": r[1], "lan": r[2], "diem": r[3]})
    return data


def index_by_key(items: list[dict], key: str) -> dict:
    return {it[key]: it for it in items}


# ---------------------------
# a) Nhập sinh viên
# ---------------------------
def input_students():
    students = load_students()
    existing_ids = {sv["ma"] for sv in students}

    print("\nNhập sinh viên (Enter ở Mã SV để dừng)")
    while True:
        ma = input("Mã SV: ").strip()
        if ma == "":
            break
        if ma in existing_ids:
            print("Mã SV đã tồn tại, nhập lại!")
            continue

        ten = input("Họ tên: ").strip()
        if not is_valid_name(ten):
            print("Họ tên không hợp lệ (khác rỗng, không ký tự đặc biệt).")
            continue

        gt = input("Giới tính (Nam/Nu): ").strip()
        if not is_valid_gender(gt):
            print("Giới tính chỉ nhận Nam hoặc Nu.")
            continue

        ns = input("Năm sinh: ").strip()
        if not is_valid_birth_year(ns):
            print("Năm sinh phải là số và trước năm 2003.")
            continue

        dc = input("Địa chỉ: ").strip()

        sdt = input("Số điện thoại (10 số): ").strip()
        if not is_valid_phone(sdt):
            print("SĐT phải gồm đúng 10 ký tự số.")
            continue

        email = input("Email (username@domain1.domain2): ").strip()
        if not is_valid_email(email):
            print("Email không đúng định dạng.")
            continue

        row = [ma, ten, gt, ns, dc, sdt, email]
        append_row(SV_FILE, row)
        existing_ids.add(ma)
        print("Đã thêm sinh viên!")

    print("Hoàn thành nhập sinh viên.\n")


# ---------------------------
# b) Nhập học phần
# ---------------------------
def input_courses():
    courses = load_courses()
    existing_ids = {hp["mahp"] for hp in courses}

    print("\nNhập học phần (Enter ở Mã HP để dừng)")
    while True:
        mahp = input("Mã học phần: ").strip()
        if mahp == "":
            break
        if mahp in existing_ids:
            print("Mã học phần đã tồn tại, nhập lại!")
            continue

        tenhp = input("Tên học phần: ").strip()
        if not is_valid_name(tenhp):
            print("Tên học phần không hợp lệ (khác rỗng, không ký tự đặc biệt).")
            continue

        loai = input("Loại học phần (ĐC/CSN/CN/ĐA/TT): ").strip()
        if loai not in HP_TYPES:
            print("Loại học phần không hợp lệ.")
            continue

        tc = input("Số tín chỉ (0 < tc <= 10): ").strip()
        if not is_float_number(tc):
            print("Số tín chỉ phải là số thực.")
            continue
        tc_val = float(tc)
        if not (0 < tc_val <= 10):
            print("Số tín chỉ phải > 0 và <= 10.")
            continue

        row = [mahp, tenhp, loai, str(tc_val)]
        append_row(HP_FILE, row)
        existing_ids.add(mahp)
        print("Đã thêm học phần!")

    print("Hoàn thành nhập học phần.\n")


# ---------------------------
# c) Nhập bảng điểm
# ---------------------------
def input_scores():
    students = load_students()
    courses = load_courses()
    scores = load_scores()

    sv_ids = {sv["ma"] for sv in students}
    hp_ids = {hp["mahp"] for hp in courses}
    existing_triplets = {(bd["masv"], bd["mahp"], bd["lan"]) for bd in scores}

    if not sv_ids:
        print("Chưa có sinh viên trong sinhvien.txt")
        return
    if not hp_ids:
        print("Chưa có học phần trong hocphan.txt")
        return

    print("\nNhập bảng điểm (Enter ở Mã SV để dừng)")
    while True:
        masv = input("Mã SV: ").strip()
        if masv == "":
            break
        if masv not in sv_ids:
            print("Mã SV không tồn tại trong sinhvien.txt")
            continue

        mahp = input("Mã học phần: ").strip()
        if mahp not in hp_ids:
            print("Mã học phần không tồn tại trong hocphan.txt")
            continue

        lan = input("Lần thi (1/2/3): ").strip()
        if lan not in {"1", "2", "3"}:
            print("Lần thi chỉ nhận 1, 2, hoặc 3.")
            continue

        if (masv, mahp, lan) in existing_triplets:
            print("Trùng (Mã SV, Mã HP, Lần thi) - không được phép.")
            continue

        diem = input("Điểm học phần (0..10): ").strip()
        if not is_float_number(diem):
            print("Điểm phải là số thực.")
            continue
        diem_val = float(diem)
        if not (0 <= diem_val <= 10):
            print("Điểm phải trong [0,10].")
            continue

        row = [masv, mahp, lan, str(diem_val)]
        append_row(BD_FILE, row)
        existing_triplets.add((masv, mahp, lan))
        print("Đã thêm điểm!")

    print("Hoàn thành nhập bảng điểm.\n")


# ---------------------------
# d) Hiển thị sinh viên
# ---------------------------
def show_students():
    students = load_students()
    print("\nDANH SÁCH SINH VIÊN")
    print("MaSV | HoTen | GioiTinh | NamSinh | DiaChi | SDT | Email")
    for sv in students:
        print(
            f"{sv['ma']} | {sv['ten']} | {sv['gt']} | {sv['ns']} | {sv['dc']} | {sv['sdt']} | {sv['email']}"
        )
    print()


# ---------------------------
# e) Hiển thị học phần
# ---------------------------
def show_courses():
    courses = load_courses()
    print("\nDANH SÁCH HỌC PHẦN")
    print("MaHP | TenHP | LoaiHP | SoTinChi")
    for hp in courses:
        print(f"{hp['mahp']} | {hp['tenhp']} | {hp['loai']} | {hp['tc']}")
    print()


# ---------------------------
# f) Hiển thị danh sách điểm join
# ---------------------------
def show_joined_scores():
    students = load_students()
    courses = load_courses()
    scores = load_scores()

    sv_map = index_by_key(students, "ma")
    hp_map = index_by_key(courses, "mahp")

    print("\nBẢNG ĐIỂM (JOIN)")
    print(
        "MaSV | HoTen | GioiTinh | NamSinh | MaHP | TenHP | SoTinChi | LanThi | Diem"
    )
    for bd in scores:
        sv = sv_map.get(bd["masv"])
        hp = hp_map.get(bd["mahp"])
        if not sv or not hp:
            # dữ liệu lỗi (không nên có nếu nhập đúng)
            continue
        print(
            f"{sv['ma']} | {sv['ten']} | {sv['gt']} | {sv['ns']} | "
            f"{hp['mahp']} | {hp['tenhp']} | {hp['tc']} | {bd['lan']} | {bd['diem']}"
        )
    print()


# ---------------------------
# g) DS sinh viên phải học lại (điểm lần 1 < 5)
# ---------------------------
def show_retake_students():
    students = load_students()
    courses = load_courses()
    scores = load_scores()

    sv_map = index_by_key(students, "ma")
    hp_map = index_by_key(courses, "mahp")

    # lấy các bản ghi lần 1 có điểm < 5
    retakes = []
    for bd in scores:
        if bd["lan"] == "1":
            try:
                if float(bd["diem"]) < 5:
                    sv = sv_map.get(bd["masv"])
                    hp = hp_map.get(bd["mahp"])
                    if sv and hp:
                        retakes.append((sv["ma"], sv["ten"], hp["mahp"], hp["tenhp"], bd["diem"]))
            except:
                pass

    print("\nDANH SÁCH SINH VIÊN PHẢI HỌC LẠI (LẦN 1 < 5)")
    print("MaSV | HoTen | MaHP | TenHP | DiemLan1")
    for r in retakes:
        print(" | ".join(map(str, r)))
    print()


# ---------------------------
# h) DS: MaSV, HoTen, GT, NS, DTB tích lũy lần 1
#     = Tổng(diem_lan1 * tc) / Tổng(tc)
# ---------------------------
def show_gpa_attempt1():
    students = load_students()
    courses = load_courses()
    scores = load_scores()

    hp_map = index_by_key(courses, "mahp")

    # gom điểm lần 1 theo sv
    by_sv = {}
    for bd in scores:
        if bd["lan"] != "1":
            continue
        hp = hp_map.get(bd["mahp"])
        if not hp:
            continue
        try:
            diem = float(bd["diem"])
            tc = float(hp["tc"])
        except:
            continue
        masv = bd["masv"]
        by_sv.setdefault(masv, []).append((diem, tc))

    print("\nĐIỂM TRUNG BÌNH CHUNG TÍCH LŨY LẦN 1")
    print("MaSV | HoTen | GioiTinh | NamSinh | DTB_Lan1")
    for sv in students:
        masv = sv["ma"]
        items = by_sv.get(masv, [])
        if not items:
            dtb = 0.0
        else:
            total_tc = sum(tc for _, tc in items)
            total = sum(diem * tc for diem, tc in items)
            dtb = (total / total_tc) if total_tc > 0 else 0.0
        print(f"{sv['ma']} | {sv['ten']} | {sv['gt']} | {sv['ns']} | {dtb:.2f}")
    print()


# ---------------------------
# i) DS học bổng:
#    DTB lần 1 >= 7 và không có học phần nào phải học lại (lần 1 < 5)
# ---------------------------
def show_scholarship_students():
    students = load_students()
    courses = load_courses()
    scores = load_scores()

    hp_map = index_by_key(courses, "mahp")

    # tính dtb lần 1 và flag học lại
    by_sv = {}
    retake_flag = set()  # masv có môn lần 1 < 5

    for bd in scores:
        if bd["lan"] != "1":
            continue
        hp = hp_map.get(bd["mahp"])
        if not hp:
            continue
        try:
            diem = float(bd["diem"])
            tc = float(hp["tc"])
        except:
            continue

        if diem < 5:
            retake_flag.add(bd["masv"])

        by_sv.setdefault(bd["masv"], []).append((diem, tc))

    scholarship = []
    for sv in students:
        masv = sv["ma"]
        items = by_sv.get(masv, [])
        if not items:
            dtb = 0.0
        else:
            total_tc = sum(tc for _, tc in items)
            total = sum(diem * tc for diem, tc in items)
            dtb = (total / total_tc) if total_tc > 0 else 0.0

        if dtb >= 7 and masv not in retake_flag:
            scholarship.append((sv["ma"], sv["ten"], sv["gt"], sv["ns"], f"{dtb:.2f}"))

    print("\nDANH SÁCH SINH VIÊN ĐỦ ĐIỀU KIỆN HỌC BỔNG")
    print("MaSV | HoTen | GioiTinh | NamSinh | DTB_Lan1")
    for r in scholarship:
        print(" | ".join(r))
    print()


# ---------------------------
# MENU
# ---------------------------
def menu():
    ensure_file(SV_FILE)
    ensure_file(HP_FILE)
    ensure_file(BD_FILE)

    while True:
        print(
            """
========= MENU =========
1) (a) Nhập danh sách sinh viên -> sinhvien.txt
2) (b) Nhập danh sách học phần  -> hocphan.txt
3) (c) Nhập bảng điểm           -> bangdiem.txt
4) (d) Hiển thị danh sách sinh viên
5) (e) Hiển thị danh sách học phần
6) (f) Hiển thị danh sách điểm (join)
7) (g) Hiển thị SV phải học lại (lần 1 < 5)
8) (h) Hiển thị DTB tích lũy lần 1
9) (i) Hiển thị SV đủ điều kiện học bổng
0) Thoát
========================
"""
        )
        choice = input("Chọn: ").strip()

        if choice == "1":
            input_students()
        elif choice == "2":
            input_courses()
        elif choice == "3":
            input_scores()
        elif choice == "4":
            show_students()
        elif choice == "5":
            show_courses()
        elif choice == "6":
            show_joined_scores()
        elif choice == "7":
            show_retake_students()
        elif choice == "8":
            show_gpa_attempt1()
        elif choice == "9":
            show_scholarship_students()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    menu()
