tuan = int(input("nhập số ngày trong tuần muốn hiển thị:"))
if tuan < 1 or tuan > 7:
    print("“error, out of range”")
else:
    if tuan == 1 : print("Monday")
    elif tuan == 2 : print("Tuesday")
    elif tuan == 3 : print("Wednesday")
    elif tuan == 4 : print("Thurday")
    elif tuan == 5 : print("Friday")
    elif tuan == 6 : print("Saturday")
    elif tuan == 7 : print("Sunday")
