# Khởi tạo một danh sách chứa các số
my_list = [12, 45, 78, 34, 56, 89, 23, 67]

# Sắp xếp danh sách theo thứ tự giảm dần
my_list.sort(reverse=True)

# Kiểm tra xem danh sách có ít hơn 2 phần tử hay không
if len(my_list) < 2:
    print("Danh sách không đủ phần tử để tìm hai số lớn nhất.")
else:
    # Lấy hai số lớn nhất từ danh sách
    max1 = my_list[0]
    max2 = my_list[1]

    print("Hai số lớn nhất trong danh sách là:", max1, "và", max2)
