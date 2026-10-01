so_tien_da_rut = 0
so_du = 5_000_000 
so_lan = 0
so_giao_dich = 0
while True :
    try :
        nhap_tien = int(input("Nhập vào số tiền cần rút"))
        if nhap_tien == "0" :
            break 
        elif nhap_tien>so_du:
            print("Giao dịch thất bại! Số dư không đủ") 
        elif nhap_tien < 0 :
            print("Số tiền nhập vào không hợp lệ")
        else :
            so_du -= nhap_tien
            so_tien_da_rut+= nhap_tien
            print(f"Số dư của bạn là {so_du} VND") 
            so_lan +=1
            so_giao_dich +=1
            if so_lan >5 :
                print(' Đã đạt giới hạn giao dịch của phiên')
                break
            
    except :
        print('Số tiền phải là một số')
        break
print(f"Số giao dịch thành công là {so_giao_dich} giao dịch ")
print(f"Số dư là {so_du}VND ")
print(f"Số tiền đã rút {so_tien_da_rut}VND ")
