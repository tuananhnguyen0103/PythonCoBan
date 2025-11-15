thang = int(input("Nhập tháng (1–12): "))

if thang < 1 or thang > 12:
    print("Tháng không hợp lệ!")
else:
    if thang in (2, 3, 4):
        print("Mùa Xuân")
    elif thang in (5, 6, 7):
        print("Mùa Hè")
    elif thang in (8, 9, 10):
        print("Mùa Thu")
    else:  # 11, 12, 1
        print("Mùa Đông")
