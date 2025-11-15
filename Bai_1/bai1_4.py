import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

# Trường hợp a = 0 → phương trình bậc nhất
if a == 0:
    if b != 0:
        x = -c / b
        print("Phương trình bậc nhất, nghiệm:", x)
    else:
        if c == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
else:
    # Phương trình bậc hai
    delta = b**2 - 4*a*c
    print("Delta =", delta)

    if delta < 0:
        print("Phương trình vô nghiệm (trong tập số thực).")
    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép x =", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phương trình có 2 nghiệm phân biệt:")
        print("x1 =", x1)
        print("x2 =", x2)
