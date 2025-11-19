"""
BÀI 7.4 – BIỂU ĐỒ CỘT NHÓM (GROUPED BAR)

Đề bài:
Điểm trung bình môn Tin (3 bài kiểm tra) của 2 lớp:
Lớp A: 7.5, 8.0, 8.2
Lớp B: 6.8, 7.2, 7.5

Yêu cầu:
- Vẽ biểu đồ cột nhóm để so sánh 2 lớp.
- Thêm legend.
"""

import matplotlib.pyplot as plt
import numpy as np

labels = ["Bài 1", "Bài 2", "Bài 3"]
lopA = [7.5, 8.0, 8.2]
lopB = [6.8, 7.2, 7.5]

x = np.arange(len(labels))
width = 0.35

plt.bar(x - width/2, lopA, width, label="Lớp A")
plt.bar(x + width/2, lopB, width, label="Lớp B")

plt.title("So sánh điểm 2 lớp qua 3 bài kiểm tra")
plt.xlabel("Bài kiểm tra")
plt.ylabel("Điểm trung bình")
plt.xticks(x, labels)
plt.legend()

plt.show()
