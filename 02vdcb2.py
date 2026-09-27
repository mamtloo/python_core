print('HỆ THỐNG SÀNG LỌC NGƯỜI THAM GIA HIẾN MÁU')
loi = False
try: 
    can_nang = float(input('Nhập cân nặng :'))
    tuoi = int(input('Nhập tuổi : '))
    if can_nang <50 or  tuoi < 18:
        print("Người tham gia không đủ điều kiện hiến máu")
    else :
        print('Người tham gia đủ điều kiện hiến máu')
except :
    print('Phải nhập vào một số !')