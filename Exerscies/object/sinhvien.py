class SinhVien:
    def __init__(self, ma_sv, ho_ten, gioi_tinh, nam_sinh, dia_chi, so_dt, email):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.gioi_tinh = gioi_tinh
        self.nam_sinh = nam_sinh
        self.dia_chi = dia_chi
        self.so_dt = so_dt
        self.email = email
    
sinhVien = SinhVien("SV001","Nguyen Van An","Nam","2001","Ha Noi","0987654321","an.nguyen@utehy.edu.vn")
# print(type(sinhVien))
# print(sinhVien)
# print(sinhVien.dia_chi)

# # for i in sinhVien:
# #     print(i)

sv1 = ["SV001","Nguyen Van Nam","Nam","2001","Ha Noi","0987654321","an.nguyen@utehy.edu.vn"]
sv2 = ["SV002","Nguyen Van Binh","Nam","2001","Ha Noi","0987654321","an.nguyen@utehy.edu.vn"]
# sinhViens = [sv1,sv2]

# print(sv1)

def getNameStudent(SinhVien):
    return SinhVien.ho_ten

def getName(sinhVien):
    return sinhVien[1]

print(getNameStudent(sinhVien))
print(getName(sv1))
