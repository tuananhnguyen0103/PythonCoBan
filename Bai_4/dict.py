# Ví dụ:
#     sv = {"ma": "SV001", "ten": "Nguyen Van A", "diem": 8.5}

# Đặc điểm của Dictionary:
# - Dạng ánh xạ key → value.
# - Không có thứ tự như list (nhưng giữ thứ tự khai báo từ Python 3.7 trở đi).
# - Key là duy nhất.
# - Mutable: có thể thêm, sửa, xóa.
# - Value có thể là bất kỳ kiểu dữ liệu nào.

# Khai báo Dictionary:
#     d = {"ten": "An", "tuoi": 20, "diem": 9.0}

# Truy cập giá trị:
#     d["ten"]         # "An"
#     d.get("diem")    # 9.0
#     d.get("lop", "Không tồn tại")   # tránh lỗi khi key không tồn tại

# Duyệt dictionary:
# Duyệt key:
#     for k in d.keys():
#         print(k)

# Duyệt value:
#     for v in d.values():
#         print(v)

# Duyệt cả key và value:
#     for k, v in d.items():
#         print(k, v)

# Các phương thức quan trọng:
#     keys()      - lấy toàn bộ key
#     values()    - lấy toàn bộ value
#     items()     - lấy toàn bộ (key, value)
#     get(key)    - lấy giá trị an toàn
#     update({...}) - gộp dictionary
#     pop(key)    - xóa phần tử bằng key
#     clear()     - xóa toàn bộ

# Thêm / sửa phần tử:
#     d["email"] = "abc@gmail.com"  # thêm
#     d["ten"] = "Nguyen A"         # sửa

# Xóa phần tử:
#     d.pop("email")
#     del d["ten"]
#     d.clear()

# Dictionary lồng nhau:
#     students = {
#         "SV001": {"ten": "An", "toan": 8, "ly": 7},
#         "SV002": {"ten": "Binh", "toan": 9, "ly": 6}
#     }

sv = {"ma": "SV001", "ten": "Nguyen Van A", "diem": 8.5}
# print(sv["ten"])
# print(sv.get("ten"))
# # print(sv["namsinh"])
# print(sv.keys())
# print(sv.values())
# # print(sv.get())
# print(sv.items())
# print(type(sv.items))

for k,v in sv.items():
    print(k, ":", v)
    # print(v)
