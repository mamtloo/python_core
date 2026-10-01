import sys
hoa_don_lon = 0
doanh_thu = 0
so_hoa_don =0 
loi = True
if loi :
    while True :
        try :
            gia_tri_hoa_don =int(input('Nhập vào giá trị hóa đơn của khách hàng (VND)'))
            if gia_tri_hoa_don >= 0:
                if gia_tri_hoa_don >= 1_000_000 :
                    hoa_don_lon+=1
                    so_hoa_don+=1
                    doanh_thu += gia_tri_hoa_don
                else :
                    so_hoa_don+=1
                    doanh_thu += gia_tri_hoa_don
                        
        except:
            print('Vui lòng nhập một số ')
        while True :
            print('''Tiếp tục thực hiện xử lý
            1/Y
            2/N
            ''')
            tiep_tuc = (input()).upper()
            if tiep_tuc == "N" :
                loi = False
                break
            elif tiep_tuc == "Y" :
                break
            else :
                print("Chỉ được nhập y hoặc n")
                continue
ti_le = (hoa_don_lon / so_hoa_don)*100
print('----- Báo cáo -----')
print (f'Tổng doanh thu là {doanh_thu}VND')
print(f"Số hóa đơn lớn là : {hoa_don_lon} hóa đơn")
print(f"Tỉ lệ hóa đơn lớn là {ti_le}%")
        
