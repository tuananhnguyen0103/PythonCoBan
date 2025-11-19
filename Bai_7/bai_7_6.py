"""
BÀI 7.6 – HISTOGRAM

Đề bài:
Cho danh sách điểm thi 30 sinh viên (0–10).
Yêu cầu:
- Vẽ histogram phân bố điểm.
"""

import matplotlib.pyplot as plt

diem = [5, 6.5, 7, 8, 9, 4, 6, 7.5, 8, 9.5, 3, 5.5, 6, 7, 8.5,
        2, 4.5, 5, 6.5, 7, 8, 9, 10, 3.5, 5, 6, 7.5, 8, 9, 4]

plt.hist(diem, bins=10, color='skyblue', edgecolor='black')

plt.title("Phân bố điểm thi")
plt.xlabel("Điểm")
plt.ylabel("Số lượng sinh viên")

plt.show()
