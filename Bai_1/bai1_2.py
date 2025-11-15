import os
import math

print("Chương trình tính diện tính và chu vi của hình chữ nhật")

print("Hình chữ nhật là hình có chiều dài ")
print("Hình chữ nhật là hình có chiều rộng ")

h = int(input("Nhập chiều dài của hình chữ nhật: "))
w = int(input("Nhập chiều rộng của hình chữ nhật: "))

C = round(h+w)*2
S = round(h*w)

os.system('cls' if os.name == 'nt' else 'clear')

print("Với chiều dài là: {0}, chiều rộng là: {1}; thì Chu vi của hình chữ nhật là là: {2}".format(h, w, C))
print("Với chiều dài là: {0}, chiều rộng là: {1}; thì Diện tích của hình chữ nhật là là: {2}".format(h, w, S))
