print('-----Hệ Thống Phân Loại Bệnh Nhân-----')
loai =""
ten = input('Nhập họ và tên bệnh nhân : ')
loai1 = ('ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa.')
loai2 = ('KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh.')
loai3 =('ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi.')
if not ten :
    print("LỖI: Tên không hợp lệ !")
else :
    try :        
        nam_sinh = int(input('Nhập năm sinh bệnh nhân : '))   
        tuoi = 2026 - nam_sinh
        if  150 >tuoi>=80 :
            loai = loai1
        elif 80>tuoi >=6  :
            loai = loai2       
        elif 6> tuoi >=0 :
            loai = loai3
        else :
            print("Tuổi nằm ngoài phạm vi con người (0-150)!")
        if loai:                           
            print('-----PHIẾU KHÁM BỆNH-----')
            print('Họ và tên bệnh nhân : ',ten) 
            print('Năm sinh : ',nam_sinh) 
            print('Tuổi : ',tuoi)
            print('Phân loại : ',loai) 
    except :
        print('Vui lòng chỉ sử dụng số')



