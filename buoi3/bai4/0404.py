danh_sach_san_pham = ["SP101", "SP205", "SP310", "SP422", "SP507"]
ma_san_pham_can_tim = input("Nhập mã sản phẩm cần tìm kiếm :").upper()
for thu_tu_san_pham,ma_san_pham in enumerate (danh_sach_san_pham) :
    if ma_san_pham == ma_san_pham_can_tim :
        print("Sản phẩm nằm ở vị trí :",thu_tu_san_pham+1)
        break
else :
    print(f'Không tìm thấy mã {ma_san_pham_can_tim} trên băng chuyền')
