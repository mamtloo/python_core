canh_bao = True
laptop = 0
phone = 0
tablet = 0
try :
    nguong_canh_bao = int(input("Nhập vào ngưỡng hàng muốn cảnh báo :" ))
except :
    print("Cần nhập vào một số hợp lệ")
if nguong_canh_bao < 0 :
    print ("Dữ liệu nhập vào không hợp lệ")
while True :
    print ("""Chọn chức năng muốn sử dụng :
    1.Xem báo cáo tồn kho
    2.Nhập kho
    3.Xuất kho 
    4.Cảnh báo hàng tồn kho thấp 
    5.Thoát chương trình
    """)
    lua_chon_1 = int(input("Nhập vào lựa chọn của bạn :"))
    if not 1<= lua_chon_1 <= 5 :
        print("Lựa chọn không hợp lệ, vui lòng chọn lại!")
    elif lua_chon_1 == 1 :
        print(f"Số laptop còn trong kho là {laptop} ")
        print(f"Số điện thoại còn trong kho là {phone} ")
        print(f"Số máy tính bảng còn trong kho là {tablet} ")
    elif lua_chon_1 == 2 :
        print (''' Mặt hàng muốn nhập kho  
        1.Laptop
        2.Điện thoại
        3.Máy tính bảng
        ''')
        lua_chon_2 = int(input("Nhập vào lựa chọn của bạn : " ))
        if not 1<=lua_chon_2<=3 :
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")
            continue
        elif lua_chon_2 == 1 :
            try :
                nhap_laptop = int(input('Nhập số lượng laptop muốn nhập :'))
            except :
                print("Cần nhập vào một số !")
                continue    
            if nhap_laptop <= 0 :
                print("Cần nhập vào một số lớn hơn 0!")
                continue
            else :
                laptop += nhap_laptop
                print (f"Đã nhập {nhap_laptop} laptop.Tồn kho {laptop} laptop")    
            


        elif lua_chon_2 == 2 :
            try :
                nhap_phone = int(input('Nhập số lượng điện thoại muốn nhập : '))
            except :
                print("Cần nhập vào một số !")
                continue 
            if nhap_phone <= 0 :
                print("Cần nhập vào một số lớn hơn 0!")
                continue
            else :
                phone += nhap_phone
                print (f"Đã nhập {nhap_phone} laptop.Tồn kho {phone} chiếc điện thoại")
                    



        elif lua_chon_2 == 3 :
            try:
                nhap_tablet = int(input('Nhập số lượng máy tính bảng  muốn nhập : '))
                    
            except :
                print("Cần nhập vào một số !")
                continue    
            if nhap_tablet <= 0 :
                print("Cần nhập vào một số lớn hơn 0!")
                continue
            else :
                tablet += nhap_tablet
                print (f"Đã nhập {nhap_tablet} laptop.Tồn kho {tablet} chiếc máy tính bảng")



    elif lua_chon_1 == 3 :
        print (''' Mặt hàng muốn xuất kho  
                1.Laptop
                2.Điện thoại
                3.Máy tính bảng
                ''')
        lua_chon_2 = int(input("Nhập vào lựa chọn của bạn : "))
        if not 1<=lua_chon_2<=3 :
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")
            continue
        elif lua_chon_2 == 1 :
            try :
                xuat_laptop = int(input('Nhập số lượng laptop muốn xuất kho  :'))
            except :
                print("Cần nhập vào một số !")
                continue 

            if xuat_laptop <0 :
                print("Cần nhập vào một số lớn hơn 0!")
                continue

            if laptop >= xuat_laptop :
                laptop -= xuat_laptop
                print (f"Đã xuất {xuat_laptop} laptop.Tồn kho {laptop} laptop")
                continue
            
            print(f'Không đủ hàng . Còn lại {laptop} laptop ') 
            continue       
                


        elif lua_chon_2 == 2 :
            try :
                xuat_phone = int(input('Nhập số lượng điện thoại muốn xuất kho : '))

            except :
                print("Cần nhập vào một số !")
                continue 
            if xuat_phone <0 :
                print("Cần nhập vào một số lớn hơn 0!")
                continue
            else :
                if phone >= xuat_phone:
                    phone -= xuat_laptop
                    print (f"Đã xuất {xuat_phone} chiếc điện thoại .Còn lại {phone} chiếc điện thoại")
                    continue
                else :
                    print(f'Không đủ hàng . Còn lại {phone} chiếc điện thoại ') 
                    continue       
                


        elif lua_chon_2 == 3 :
            try:
                xuat_tablet = int(input('Nhập số lượng máy tính bảng  muốn xuất kho : '))
                    
            except :
                print("Cần nhập vào một số !")
                continue  
            if xuat_tablet <0 :
                print("Cần nhập vào một số lớn hơn 0!")
                continue
            else :
                if tablet >= xuat_tablet:
                    tablet -= xuat_tablet
                    print (f"Đã xuất {xuat_tablet} chiếc máy tính bảng .Còn lại {tablet} chiếc máy tính bảng")
                    continue
                else :
                    print(f'Không đủ hàng . Còn lại {tablet} chiếc máy tính bảng') 
                    continue   
    elif lua_chon_1 ==1:
        print(f"Số laptop còn lại là {laptop} chiếc")
        for so_laptop in range(laptop) :
            print('*',end ="")
        
        print(f"Số điện thoại còn lại là ({phone}): ",end ="")
        for so_phone in range (phone):
            print("*",end = "")
        print(f"Số máy tính bảng còn lại là ({tablet}):", end ="")
        for so_tablet in range (tablet) :
            print("*",end ="")
        print(f"Tổng số hàng còn lại là {tablet + phone + laptop} chiếc")

        for so_phone in range (phone) :
            print('*',end ="")
        for so_tablet in range (tablet) :
            print('*',end ="")


    elif lua_chon_1 == 4 :
        if laptop ==0 :
            print('[CẢNH BÁO] Mặt hàng laptop đã hết hàng!')    
            canh_bao = False
        elif laptop < nguong_canh_bao :
            print(f'[CẢNH BÁO] Mặt hàng laptop sắp hết (Chỉ còn {laptop} sản phẩm)')
            canh_bao = False

        if phone ==0 :
            print('[CẢNH BÁO] Mặt hàng điện thoại đã hết hàng!')    
            canh_bao = False
        elif phone < nguong_canh_bao :
            print(f'[CẢNH BÁO] Mặt hàng điện thoại sắp hết (Chỉ còn {phone} sản phẩm)')
            canh_bao = False

        if tablet ==0 :
            print('[CẢNH BÁO] Mặt hàng máy tính bảng đã hết hàng!')    
            canh_bao = False
        elif tablet < nguong_canh_bao :
            print(f'[CẢNH BÁO] Mặt hàng máy tính bảng sắp hết (Chỉ còn {tablet} sản phẩm)')
            canh_bao = False
    if canh_bao :
            print('Tất cả mặt hàng đều ở mức an toàn.')  
    elif lua_chon_1 ==5 :
        print ("Chương trình kết thúc")
        break         
            