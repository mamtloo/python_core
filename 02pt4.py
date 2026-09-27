print('-----Hệ Thống Sàng Lọc Điều Kiện Phẫu Thuật-----')
try :
    tuoi = int(input('Nhập vào tuổi bệnh nhân : '))
    huyet_ap = int(input('Nhập vào huyết áp bệnh nhân (mmHG) : '))
    duong_huyet = int(input('Nhập vào đường huyết bệnh nhân (mm/Dl) : '))
    if 0<=tuoi<75 and 90<=huyet_ap<=140 and 0<=duong_huyet<=150 :
        print('ĐỦ ĐIỀU KIỆN PHẪU THUẬT')
    else :
        print('TỪ CHỐI PHẪU THUẬT')
except :
    print('Dữ liệu nhập vào không hợp lệ')
