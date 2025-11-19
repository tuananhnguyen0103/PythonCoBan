# Hàm đổi giá trị hai biến
def swap(a, b):
    return b, a   # đổi chỗ

def main():
    print("Chương trình đổi giá trị 2 biến")
    x = input("Nhập giá trị x: ")
    y = input("Nhập giá trị y: ")

    print("Trước khi đổi: x =", x, ", y =", y)

    x, y = swap(x, y)

    print("Sau khi đổi : x =", x, ", y =", y)

main()
