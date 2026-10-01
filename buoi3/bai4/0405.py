don_gia = int(input('Nhập vào đơn giá một sản phẩm'))
moc_giam_gia =[0,5,10,15]
# giảm giá chạy theo các giá trị trong list
for giam_gia in moc_giam_gia:
    for so_luong in range (1,6):
        gia_goc = so_luong * don_gia
        tong = gia_goc * ((100-giam_gia)/100)
        nhan ="Combo lớn" if so_luong >=4 else "Combo nhỏ"
        print (f'Mức giảm {giam_gia}%,Số lượng {so_luong},Thành tiền {tong} VND,{nhan}')
