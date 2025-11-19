# Bài 4.3: Nhập dãy số và thực hiện các thao tác

n = int(input("Nhập số lượng phần tử n: "))
numbers = []

# Nhập dãy số
for i in range(n):
    x = float(input(f"Nhập phần tử x[{i}]: "))
    numbers.append(x)

print("\nDãy bạn vừa nhập:")
print(numbers)

# 1. Giá trị lớn nhất
max_val = max(numbers)
print("Giá trị lớn nhất:", max_val)

# 2. Giá trị nhỏ nhất
min_val = min(numbers)
print("Giá trị nhỏ nhất:", min_val)

# 3. Tổng các phần tử
total = sum(numbers)
print("Tổng các phần tử:", total)

# 4. Đảo ngược dãy
reversed_list = numbers[::-1]
print("Dãy đảo ngược:", reversed_list)

# 5. Sắp xếp tăng dần
asc_list = sorted(numbers)
print("Dãy tăng dần:", asc_list)

# 6. Sắp xếp giảm dần
desc_list = sorted(numbers, reverse=True)
print("Dãy giảm dần:", desc_list)

# 7. Đếm số dương, âm, 0
pos = neg = zero = 0

for x in numbers:
    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1
    else:
        zero += 1

print(f"\nSố dương: {pos}")
print(f"Số âm: {neg}")
print(f"Số 0 : {zero}")

# 8. Loại nào nhiều nhất?
max_count = max(pos, neg, zero)
most = []

if pos == max_count:
    most.append("số dương")
if neg == max_count:
    most.append("số âm")
if zero == max_count:
    most.append("số 0")

print("Loại xuất hiện nhiều nhất:", ", ".join(most))
