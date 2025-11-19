"""
BÀI 7.3 – SCATTER PLOT

Đề bài:
Cho dữ liệu chiều cao và cân nặng:
Chiều cao: 150, 155, 160, 165, 170, 175, 180
Cân nặng:  45, 48, 52, 55, 60, 65, 72

Yêu cầu:
- Vẽ biểu đồ điểm để biểu diễn mối quan hệ chiều cao – cân nặng.
- Thêm tiêu đề và nhãn trục.
"""

import matplotlib.pyplot as plt

chieucao = [150, 155, 160, 165, 170, 175, 180]
cannang  = [45, 48, 52, 55, 60, 65, 72]

plt.scatter(chieucao, cannang, color='purple')

plt.title("Mối quan hệ giữa chiều cao và cân nặng")
plt.xlabel("Chiều cao (cm)")
plt.ylabel("Cân nặng (kg)")

plt.grid(True)
plt.show()
