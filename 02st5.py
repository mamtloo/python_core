print('-----NHẬP THÔNG TIN BỆNH NHÂN----')
ten = input('Nhập họ và tên bệnh nhân :')
tinh_trang1 = "Cấp cứu khẩn"
tinh_trang2 = 'Theo dõi sát'
tinh_trang3 = 'Khám thường'
loi1 = True
loi2 =True
if not ten :
    print('Dữ liệu nhập vào không hợp lệ!') 
else :
    try :
        tuoi = int(input('Nhập tuổi bệnh nhân :'))
        if not 150>=tuoi>=0:
            print("Tuổi vượt quá giới hạn con người (0-150) ")
            loi1=False

        nong_do = int(input('Nhập nồng độ oxy trong máu bệnh nhân (Sp02) :'))
        if not 100>=nong_do>=0 :
            print('Dữ liệu nhập vào không hợp lệ!') 
            loi1=False    
            
        nhip_tim = int(input('Nhập nhịp tim bệnh nhân (Nhịp/phút)'))
        if not 150 >=nhip_tim>=0 :
            print('Nhịp tim vượt quá giới hạn con người')
            loi1=False    

            
        print('Bệnh nhân có thẻ bảo hiểm y tế không (Trả lời có hoặc không)')
        nhap_du_lieu = input('')
        if not nhap_du_lieu =="có" or not nhap_du_lieu =="không":
            print('Trả lời có hoặc không')
        else :    
            if loi1:
                if nong_do <90 or nhip_tim >120:
                    tinh_trang = tinh_trang1 
                elif 90<= nong_do<=95  or 120>=nhip_tim>=100:
                    tinh_trang = tinh_trang2 
                elif 95 < nong_do<=100 or 100>nhip_tim>=0:
                    tinh_trang = tinh_trang3
                else :
                    print('Dữ liệu nhập vào không hợp lệ!') 
                    loi2 =False   
            if loi2 :
                if 6<=tuoi or 80>=tuoi :
                    vien_phi=('0VND')
                elif nhap_du_lieu =="có":
                    vien_phi=('250_000VND')
                else:
                    vien_phi=("500_000VND")
            print('-----THÔNG TIN KHÁM BỆNH-----')
            print("Họ và tên bệnh nhân : ", ten)
            print("Tuoi : ", tuoi)
            print("Thẻ bảo hiểm y tế : ", nhap_du_lieu)
            print("Tình trạng bệnh nhân : ", tinh_trang)
            print("Viện phí: ", vien_phi)

    except :
        print('Dữ liệu nhập vào không hợp lệ!') 
