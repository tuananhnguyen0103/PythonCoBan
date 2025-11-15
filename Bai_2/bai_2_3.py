# Bài tập 2.3: Phân tích chương trình

name = input('Give me your name: ')
age = int(input('Enter your age: '))

# Dòng sau đây gây lỗi vì cộng chuỗi với số nguyên:
# print('Your name is ' + name + 'Your age is ' + age)

# Sửa đúng:
print('Your name is ' + name + ' Your age is ' + str(age))
