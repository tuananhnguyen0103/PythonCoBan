# Bài tập 2.1: Các biểu thức kiểm tra số

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

print("a là số âm:", a < 0)
print("a là số dương:", a > 0)
print("a là số chẵn:", a % 2 == 0)
print("a là số lẻ:", a % 2 != 0)
print("a là số âm chẵn:", a < 0 and a % 2 == 0)
print("a là số âm lẻ:", a < 0 and a % 2 != 0)
print("a là số dương chẵn:", a > 0 and a % 2 == 0)
print("a là số dương lẻ:", a > 0 and a % 2 != 0)
print("a là bội số của b:", b != 0 and a % b == 0)
print("a là ước số của b:", a != 0 and b % a == 0)
print("a là số tự nhiên 3 chữ số:", 100 <= a <= 999)
