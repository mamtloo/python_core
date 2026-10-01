try :
    so_luong = int(input("Nhập vào số lượng thùng hàng : "))
    kiem_tra = 0
    if so_luong <=0 :
        print('Nhập vào số lớn hơn 0')
    else :    
        for index in range(1,so_luong+1):
            print(f"Thùng số {index} đã nhập kho")
            if index % 5 ==0:
                print("Kiểm tra chất lượng thùng này")
                kiem_tra +=1
        print("Số thùng đã nhập kho là ",so_luong)
        print("Số thùng đã kiểm tra chất lượng là ",kiem_tra)

        
except :    
    print("Số lượng thùng phải là một số!")