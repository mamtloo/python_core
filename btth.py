import sys
print("Vui lòng nhập thông tin bệnh nhân ")
ten = input('Nhập tên bệnh nhân: ')
try:
    nam_sinh = int(input('Nhập năm sinh bệnh nhân: '))
except: 
    print("Phải là một số")
    sys.exit()   
try:
    so_ngay_bi_benh = int(input('Nhập số ngày bị bệnh: '))
except:
    print("Phải là một số")
    sys.exit()
try:
    nhiet_do = float(input('Nhập nhiệt độ cơ thể bệnh nhân: '))
except:
        print("Phải là một số ")
        sys.exit()
try:
    chi_phi_kham = float(input('Nhập chi phí khám: '))
except:
    print("Phải là một số")
    sys.exit()
if not ten:
    print("Tên không được để trống ")
    sys.exit()
if not (1900<= nam_sinh <=2026):
    print("năm sinh không hợp lệ")
    sys.exit() 
if so_ngay_bi_benh < 0:
    print("không hợp lệ")
    sys.exit()
if not (30<= nhiet_do <= 45):
    print("không hợp lệ")
    sys.exit()
if not (chi_phi_kham >0):
    print("không hợp lệ")
    sys.exit()
tuoi_benh_nhan = 2026 - nam_sinh
phu_phi = 0.1 * chi_phi_kham
tong_chi_phi = phu_phi + chi_phi_kham
print ("-----KẾT QUẢ KHÁM SỨC KHỎE -----")
print("Tên bệnh nhân :",ten)
print("Sinh năm :",nam_sinh)
print("Nhiệt độ :",f'{nhiet_do} độ C')
print("Số ngày bị bệnh:",so_ngay_bi_benh)

tinh_trang =""
if nhiet_do > 38 and so_ngay_bi_benh >3 :
    tinh_trang = "NGUY HIỂM"
    print("Tình trạng : NGUY HIỂM")
elif nhiet_do >38 :

    print("Tình trạng : SỐT CAO")
elif nhiet_do >37.5:
    print("Tình trạng : SỐT NHẸ")
else:
    print("Tình trạng :BÌNH THƯỜNG")


if tinh_trang=="NGUY HIỂM":
    if tuoi_benh_nhan > 60:
        print("Mức độ ưu tiên :CẤP CỨU")
    else:
        print("Mức độ ưu tiên :ƯU TIÊN CAO")
else:
    print("Mức độ ưu tiên :BÌNH THƯỜNG")
print("Tổng chi phí khám bệnh :",tong_chi_phi)
muc_chi_phi = "Cao" if tong_chi_phi>500_000 else "Thấp"
print('Mức chi phí :',muc_chi_phi)









