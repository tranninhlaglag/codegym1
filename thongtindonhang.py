chi_tieu = int(input("nhập số tiền bạn đã chi tiêu $:"))
if chi_tieu > 0:
    if chi_tieu < 75:
        print(f"số tiền bạn cần thanh toán là :{chi_tieu}")
    elif chi_tieu < 100 :
        print(f"số tiền bạn phải thanh toán là :{chi_tieu - 15}")
    elif chi_tieu < 150:
        print(f"số tiền bạn phải thanh toán là : {chi_tieu - 25}")
    else:
        print(f"số tièn bạn phải thanh toán là :{chi_tieu - 50}")
else:
    print("bạn nhập sai thông tin")