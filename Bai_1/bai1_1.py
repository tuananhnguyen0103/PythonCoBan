import math

print("Chương trình tính diện tính và chu vi của hình tròn")

print("Hình tròn là hình có bán kính ")

r = int(input("Nhập bán kính của hình tròn: "))

C = round(2 * math.pi * r, 2)
S = round(math.pi * pow(r, 2), 2)

print("Với bán kính là: {0}, thì Chu vi của hình tròn là là: {1}".format(r, C))
print("Với bán kính là: {0}, thì Diện tích của hình tròn là là: {1}".format(r, S))
