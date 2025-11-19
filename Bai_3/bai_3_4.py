import math

while True:
    print("Nhập ba cạnh tam giác (nhập 0 để thoát):")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    if a <= 0 or b <= 0 or c <= 0:
        print("Kết thúc chương trình.")
        break

    # Điều kiện tạo thành tam giác
    if a + b > c and a + c > b and b + c > a:
        print("Ba cạnh tạo thành tam giác.")

        # Công thức Heron
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("Diện tích tam giác =", area)
    else:
        print("Ba cạnh không tạo thành tam giác!")

    print("---------------------------")
