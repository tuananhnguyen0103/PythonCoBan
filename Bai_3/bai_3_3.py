import math

while True:
    r = float(input("Nhập bán kính r (nhập số âm để thoát): "))

    if r < 0:
        print("Kết thúc chương trình.")
        break

    C = 2 * math.pi * r
    S = math.pi * r * r

    print("Chu vi hình tròn =", C)
    print("Diện tích hình tròn =", S)
    print("---------------------------")
