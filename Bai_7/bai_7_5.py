"""
BÀI 7.5 – BIỂU ĐỒ TRÒN (PIE CHART)

Đề bài:
Thị phần điện thoại:
A: 40% | B: 30% | C: 20% | D: 10%

Yêu cầu:
- Vẽ biểu đồ tròn với phần trăm trên từng lát cắt.
"""

import matplotlib.pyplot as plt

labels = ["Hãng A", "Hãng B", "Hãng C", "Hãng D"]
sizes  = [40, 30, 20, 10]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

plt.title("Thị phần các hãng điện thoại")
plt.axis('equal')

plt.show()
