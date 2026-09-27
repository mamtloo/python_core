print('-----Hệ Thống Phân Loại Bệnh Nhân-----')
loi = True
ten = input('Nhập họ và tên bệnh nhân : ')
loai1 = ('ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa.')
loai2 = ('KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh.')
loai3 =('ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi.')
if not ten :
    print("LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
else :
    try :        
        nam_sinh = int(input('Nhập năm sinh bệnh nhân : '))   
        if loi :
            tuoi = 2026 - nam_sinh
            if not 0< tuoi < 150 :
                print ('LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!')
                loi = False 
        if loi :
            if tuoi >=80 :
                    loai = loai1
            elif tuoi >=6  :
                    loai = loai2       
            else : 
                    loai = loai3
    except :
        print('Vui lòng chỉ sử dụng số')
        loi = False
    if loi:                           
        print('-----PHIẾU KHÁM BỆNH-----')
        print('Họ và tên bệnh nhân : ',ten) 
        print('Năm sinh : ',nam_sinh) 
        print('Tuổi : ',tuoi)
        print('Phân loại : ',loai) 



