print('HỆ THỐNG PHÂN LOẠI TÌNH TRẠNG KHẨN CẤP')
try:
    nhip_tim = int(input('Nhập nhịp tim bệnh nhân (bpm):'))
    if nhip_tim > 120:
            print('Nguy kịch, cấp cứu ngay')
    elif nhip_tim > 100:
        print('Bất thường, cần theo dõi sát')
    elif nhip_tim > 60 :
        print(' Ổn định, chờ theo thứ tự')
    else :
            print(' Nhịp tim chậm, cần kiểm tra thêm')    
            
except:
    print('Cần nhập vào một số!')
