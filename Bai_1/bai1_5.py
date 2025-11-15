hoten = input("Nhập họ tên chủ hộ: ")
chiso1 = int(input("Nhập chỉ số điện tháng trước: "))
chiso2 = int(input("Nhập chỉ số điện tháng này: "))

if chiso2 < chiso1:
    print("Lỗi: Chỉ số tháng này phải lớn hơn hoặc bằng tháng trước!")
else:
    sodien = chiso2 - chiso1
    print("Chủ hộ:", hoten)
    print("Số điện tiêu thụ tháng này là:", sodien, "kWh")
