# Nhập tiền lương mỗi tháng và số người phụ thuộc
tien_luong = float(input("Nhập tiền lương mỗi tháng (triệu đồng): "))
so_nguoi_phu_thuoc = int(input("Nhập số người phụ thuộc: "))

# Tính giảm trừ gia cảnh
giam_tru_ban_than = 11.0
giam_tru_nguoi_phu_thuoc = so_nguoi_phu_thuoc * 4.4
giam_tru_gia_canh = giam_tru_ban_than + giam_tru_nguoi_phu_thuoc

# Tính thu nhập chịu thuế
thu_nhap_chiu_thue = tien_luong - giam_tru_gia_canh

# Tính thuế theo mức thuế suất
if 0 < thu_nhap_chiu_thue <= 5:
    thue_tncn = thu_nhap_chiu_thue * 0.05
elif 5 < thu_nhap_chiu_thue <= 10:
    thue_tncn = thu_nhap_chiu_thue * 0.1
elif 10 < thu_nhap_chiu_thue <= 18:
    thue_tncn = thu_nhap_chiu_thue * 0.15
elif 18 < thu_nhap_chiu_thue <= 32:
    thue_tncn = thu_nhap_chiu_thue * 0.2
elif 32 < thu_nhap_chiu_thue <= 52:
    thue_tncn = thu_nhap_chiu_thue * 0.25
elif 52 < thu_nhap_chiu_thue < 80:
    thue_tncn = thu_nhap_chiu_thue * 0.3
else:
    thue_tncn = thu_nhap_chiu_thue * 0.35

# Tính số tiền thực lãnh
tien_thuc_lanh = tien_luong - thue_tncn

# In kết quả
print(f"Số thuế thu nhập cá nhân cần nộp: {thue_tncn} triệu đồng")
print(f"Số tiền thực lãnh: {tien_thuc_lanh} triệu đồng")
