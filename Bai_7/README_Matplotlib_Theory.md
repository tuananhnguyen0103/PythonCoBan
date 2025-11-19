#  README – CHƯƠNG: SỬ DỤNG MATPLOTLIB (plt) ĐỂ VẼ BIỂU ĐỒ

##  1. Mục tiêu của chương
- Hiểu vai trò của hình ảnh hóa dữ liệu.
- Biết thư viện Matplotlib và module pyplot (`plt`).
- Nắm các thuộc tính quan trọng khi vẽ biểu đồ.
- Chọn đúng loại biểu đồ cho đúng dữ liệu.
- Áp dụng quy trình 4 bước chuẩn để vẽ biểu đồ.

##  2. Giới thiệu về Matplotlib và `plt`
`matplotlib.pyplot` là module dùng để vẽ đồ thị 2D: đường, cột, điểm, tròn, histogram,...
Quy trình hoạt động: Chuẩn bị dữ liệu → Gọi hàm vẽ → Tùy chỉnh thuộc tính → Hiển thị.

##  3. Các loại biểu đồ và thuộc tính cần biết

### 3.1. Line Chart – Đồ thị đường (`plt.plot`)
**Khi dùng:** dữ liệu theo thứ tự hoặc thời gian, quan sát xu hướng.  
**Thuộc tính:**  
- color – màu đường  
- linestyle – kiểu đường  
- linewidth – độ dày  
- marker – ký hiệu điểm  
- markersize – kích thước điểm  
- label – tên đường  

### 3.2. Bar Chart – Biểu đồ cột (`plt.bar`)
**Khi dùng:** so sánh dữ liệu giữa các nhóm.  
**Thuộc tính:**  
- color – màu  
- width – độ rộng cột  
- edgecolor – màu viền  
- label – chú thích  

### 3.3. Scatter Plot – Biểu đồ điểm (`plt.scatter`)
**Khi dùng:** phân tích tương quan giữa hai biến.  
**Thuộc tính:**  
- s – kích thước điểm  
- color – màu  
- alpha – độ trong suốt  
- marker – hình dạng điểm  
- label – tên dataset  

### 3.4. Pie Chart – Biểu đồ tròn (`plt.pie`)
**Khi dùng:** thể hiện tỷ lệ các phần trong tổng thể.  
**Thuộc tính:**  
- labels – tên từng lát  
- autopct – hiển thị phần trăm  
- startangle – góc bắt đầu  
- explode – tách lát đặc biệt  
- shadow – đổ bóng  

### 3.5. Histogram – Biểu đồ phân bố (`plt.hist`)
**Khi dùng:** mô tả phân bố dữ liệu.  
**Thuộc tính:**  
- bins – số cột  
- color – màu  
- edgecolor – viền  
- alpha – độ trong suốt  
- density – chuẩn hóa phân bố  

##  4. Thuộc tính chung cho mọi biểu đồ
- title() – tiêu đề  
- xlabel(), ylabel() – tên trục  
- legend() – chú thích  
- grid() – lưới  
- figure(figsize=(w,h)) – kích thước  
- xticks(), yticks() – mốc trục  
- xlim(), ylim() – giới hạn trục  
- tight_layout() – tự căn chỉnh bố cục  

##  5. Quy trình 4 bước chuẩn khi vẽ biểu đồ

### Bước 1 – Chọn loại biểu đồ phù hợp
- Line: dữ liệu theo thời gian  
- Bar: so sánh nhóm  
- Scatter: tương quan  
- Pie: tỷ lệ  
- Histogram: phân bố  

### Bước 2 – Chuẩn bị dữ liệu
- Dữ liệu dạng list/array  
- X và Y phải khớp  

### Bước 3 – Tùy chỉnh biểu đồ
- Màu  
- Marker  
- Line style  
- Tiêu đề  
- Nhãn trục  
- Legend  
- Grid  

### Bước 4 – Hiển thị và hoàn thiện
- Biểu đồ rõ ràng, dễ đọc  
- Bố cục chuẩn, nhãn đầy đủ  

##  6. Checklist nhanh
- Đúng loại biểu đồ?  
- Dữ liệu đúng định dạng?  
- Đủ tiêu đề và nhãn trục?  
- Màu sắc dễ nhìn?  
- Có cần grid/legend không?  

