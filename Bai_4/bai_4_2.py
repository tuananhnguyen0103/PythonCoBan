# Bài 4.2: Xác định giá trị và kiểu dữ liệu của years_of_birth và ages

years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
ages = []

for year in years_of_birth:
    ages.append(2018 - year)

print("Kiểu dữ liệu years_of_birth:", type(years_of_birth))
print("Giá trị years_of_birth:", years_of_birth)

print("Kiểu dữ liệu ages:", type(ages))
print("Giá trị ages:", ages)
