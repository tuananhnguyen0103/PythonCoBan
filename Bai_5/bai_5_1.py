import math

# Hàm tính delta
def tinh_delta(a, b, c):
    return b*b - 4*a*c

# Hàm giải khi delta < 0
def giai_delta_am():
    print("Phương trình vô nghiệm (delta < 0).")

# Hàm giải khi delta = 0
def giai_delta_0(a, b):
    x = -b / (2*a)
    print("Phương trình có nghiệm kép x1 = x2 =", x)

# Hàm giải khi delta > 0
def giai_delta_duong(a, b, delta):
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Phương trình có 2 nghiệm phân biệt:")
    print("x1 =", x1)
    print("x2 =", x2)

# Hàm chính: gọi các hàm con
def giai_pt_bac_hai():
    print("Giải phương trình bậc hai ax^2 + bx + c = 0")
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    c = float(input("Nhập c: "))

    if a == 0:
        print("a = 0 → Đây không phải phương trình bậc hai.")
        return

    delta = tinh_delta(a, b, c)
    print("Delta =", delta)

    if delta < 0:
        giai_delta_am()
    elif delta == 0:
        giai_delta_0(a, b)
    else:
        giai_delta_duong(a, b, delta)

# Gọi chương trình
giai_pt_bac_hai()
