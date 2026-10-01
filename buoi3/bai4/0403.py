danh_sach_hoa_don = [350_000, 1_200_000, -50_000, 999_999, 780_000, 0, 2_500_000, -1, 640_000]
tong_so_hoa_don = len(danh_sach_hoa_don)
tong_gia_tri = 0
hoa_don_hop_le = 0
for hoa_don , gia_tri_hoa_don in enumerate (danh_sach_hoa_don) :
    if gia_tri_hoa_don <=0 :
        print("Hóa đơn lỗi tại vị trí",hoa_don+1)
        continue
    elif hoa_don == 999_999 :
        pass
    elif hoa_don >=2_000_000:
        break
    else :
        hoa_don_hop_le +=1
        tong_gia_tri += gia_tri_hoa_don
print(f'Số hóa đơn hợp lệ đã xử lý là {hoa_don_hop_le}')
print(f'Số hóa đơn không hợp lệ đã xử lý là {tong_so_hoa_don - hoa_don_hop_le}')
print(f'Tổng giá trị là {tong_gia_tri}VND')
