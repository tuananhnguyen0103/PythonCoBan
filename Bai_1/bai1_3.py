import math

# Nhập dữ liệu
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

# Kiểm tra điều kiện tam giác
if a + b > c and a + c > b and b + c > a:
    print("Ba cạnh tạo thành một tam giác.")

    # Tính diện tích theo công thức Heron
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))

    print("Diện tích tam giác là:", S)
else:
    print("Ba cạnh KHÔNG tạo thành tam giác.")
