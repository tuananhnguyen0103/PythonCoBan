"""
BÀI 7.2 – VẼ BIỂU ĐỒ CỘT (BAR CHART)

Đề bài:
Cho doanh thu cửa hàng (triệu đồng) trong 4 quý:
Q1: 120 | Q2: 150 | Q3: 100 | Q4: 180

Yêu cầu:
- Vẽ biểu đồ cột doanh thu theo quý.
- Hiển thị nhãn giá trị trên đầu mỗi cột.
"""

import matplotlib.pyplot as plt

quy = ["Q1", "Q2", "Q3", "Q4"]
doanh_thu = [120, 150, 100, 180]

plt.bar(quy, doanh_thu, color=['red', 'green', 'blue', 'orange'])

plt.title("Doanh thu theo từng quý (triệu đồng)")
plt.xlabel("Quý")
plt.ylabel("Doanh thu")

# Hiển thị giá trị trên đầu cột
for i in range(len(doanh_thu)):
    plt.text(i, doanh_thu[i] + 3, str(doanh_thu[i]), ha='center')

plt.show()
