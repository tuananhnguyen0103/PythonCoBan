# Bài 6.1: Tách số chẵn và số lẻ từ 10 số nguyên, ghi vào 2 file

# Bước 1: Tạo danh sách rỗng L
L = []

# Bước 2: Nhập 10 số từ bàn phím
print("Nhập 10 số nguyên:")
for i in range(10):
    x = int(input(f"Nhập số thứ {i+1}: "))
    L.append(x)

# Bước 3: Tách số lẻ → sole.txt
Le = [str(x) for x in L if x % 2 != 0]  # chuyển sang string để ghi file

with open("sole.txt", "w") as f:
    f.write("\n".join(Le))

# Bước 4: Tách số chẵn → sochan.txt
Chan = [str(x) for x in L if x % 2 == 0]

with open("sochan.txt", "w") as f:
    f.write("\n".join(Chan))

# Bước 5: Đọc dữ liệu từ file để kiểm tra
print("\n===== KẾT QUẢ TRONG FILE =====")

with open("sochan.txt", "r") as f:
    print("Số chẵn:")
    print(f.read())

with open("sole.txt", "r") as f:
    print("Số lẻ:")
    print(f.read())
