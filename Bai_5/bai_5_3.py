# Hàm tính giai thừa
def giaithua(n):
    gt = 1
    for i in range(1, n + 1):
        gt *= i
    return gt

def main():
    print("Chương trình tính giai thừa n!")

    while True:
        n = int(input("Nhập n (n >= 0): "))
        if n >= 0:
            break
        print("n phải >= 0. Vui lòng nhập lại!")

    print(f"{n}! =", giaithua(n))

main()
