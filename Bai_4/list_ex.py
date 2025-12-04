import os

ds_khoa = ["Điện-Điện tử", "Công nghệ thông tin", "Cơ khí", "Cơ khí động lực", "May - Thời trang", "Ngoại ngữ"]
print(ds_khoa)

# 2. Hiển thị danh sách khoa
#    - In ra toàn bộ danh sách khoa, mỗi khoa một dòng.
#    - Có đánh số thứ tự từ 1, 2, 3, …

for i in range(len(ds_khoa)):
    print("{0}. {1}".format(i+1,ds_khoa[i]))
    
# 3. Thêm khoa mới
#    - Người dùng nhập tên khoa mới.
#    - Nếu khoa đó CHƯA tồn tại trong list → thêm vào cuối danh sách.
#    - Nếu khoa đã tồn tại → thông báo “Khoa đã tồn tại, không thêm nữa”.


# print((new_khoa in ds_khoa))
while True:
    new_khoa = input("Nhập tên khoa mới: ")
    if new_khoa in ds_khoa:
        print("Khoa đã tồn tại, yêu cầu nhập 1 khoa mới")
        continue
    else:
        ds_khoa.append(new_khoa)
        print("Khoa mới là: khoa {} đã được thêm vào trong danh sách.".format(new_khoa))
        print("Danh sách khoa sau khi đã thêm là: ")
        for i in range(len(ds_khoa)):
            print("{0}. {1}".format(i+1,ds_khoa[i]))
        break
# 4. Xóa một khoa
#    - Người dùng nhập tên khoa muốn xóa.
#    - Nếu khoa tồn tại → xóa khỏi danh sách.
#    - Nếu không tồn tại → thông báo “Không tìm thấy khoa cần xóa”.
while True:
    del_khoa = input("Nhập tên khoa cần xóa: ")
    if del_khoa not in ds_khoa:
        print("Khoa không tồn tại, yêu cầu nhập 1 khoa cần xóa")
        continue
    else:
        ds_khoa.remove(del_khoa)
        print("Khoa cần xóa là: khoa {} đã được xóa vào trong danh sách.".format(del_khoa))
        print("Danh sách khoa sau khi đã xóa là: ")
        for i in range(len(ds_khoa)):
            print("{0}. {1}".format(i+1,ds_khoa[i]))
        break

# 5. Sửa tên khoa
#    - Người dùng nhập tên khoa cũ và tên khoa mới.
#    - Nếu tên khoa cũ tồn tại → thay thế bằng tên khoa mới.
#    - Nếu không tồn tại → thông báo “Không tìm thấy khoa cần sửa”.

while True:
    change_khoa = input("Nhập tên khoa cần sửa: ")
    if change_khoa not in ds_khoa:
        print("Khoa không tồn tại, yêu cầu nhập 1 khoa cần sửa")
        continue
    else:
        update_khoa = input("Nhập tên cần sửa của khoa {0}: ".format(change_khoa))
        idx_update_khoa = ds_khoa.index(change_khoa)
        ds_khoa[idx_update_khoa] = update_khoa
        print("Danh sách khoa sau khi đã sửa là: ")
        for i in range(len(ds_khoa)):
            print("{0}. {1}".format(i+1,ds_khoa[i]))
        break

# 6. Tìm kiếm khoa
#    - Người dùng nhập vào một từ khóa (chuỗi con), ví dụ: "Cơ khí".
#    - In ra tất cả các khoa có chứa chuỗi đó trong tên.
#    - Nếu không tìm thấy khoa phù hợp → thông báo “Không có khoa phù hợp”.

while True:
    search_khoa = input("Khoa cần tìm là: ")
    save_idxs = []
    for i in range(len(ds_khoa)):
        if search_khoa.lower() in ds_khoa[i].lower():
            save_idxs.append(i)
    for i in save_idxs:
        print("{0}. {1}".format(i+1,ds_khoa[i]))
    print("Bạn có muốn thoát khỏi chương trình không?") 
    break_condition = input("Nếu có thì nhấn phím 1: ")
    if break_condition == "1":
        break
    
print("Thành công rồi!!! 😎😎😎")