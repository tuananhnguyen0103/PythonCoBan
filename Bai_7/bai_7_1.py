"""
BÀI 7.1 – VẼ ĐỒ THỊ ĐƯỜNG (LINE CHART)

Đề bài:
Cho dữ liệu điểm trung bình môn Toán của một học sinh trong 5 học kỳ:
Học kỳ: 1, 2, 3, 4, 5
Điểm:  6.5, 7.0, 7.8, 8.2, 8.5

Yêu cầu:
- Vẽ biểu đồ đường thể hiện sự thay đổi điểm theo học kỳ.
- Thêm tiêu đề, nhãn trục x và y.
- Đánh dấu từng điểm bằng marker.
"""

import matplotlib.pyplot as plt

hk = [1, 2, 3, 4, 5]
diem = [6.5, 7.0, 7.8, 8.2, 8.5]

plt.plot(hk, diem, marker='o', linestyle='-', color='blue')

plt.title("Điểm Toán qua các học kỳ")
plt.xlabel("Học kỳ")
plt.ylabel("Điểm trung bình")

plt.grid(True)
plt.show()
