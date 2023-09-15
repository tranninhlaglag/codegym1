# Bước 1: Cho người dùng nhập biến
input_str = input("Nhập số bắt đầu và số kết thúc (cách nhau bằng khoảng trắng): ")
start_str, end_str = input_str.split()

# Chuyển chuỗi thành số nguyên
start = int(start_str)
end = int(end_str)

# Bước 2: Kiểm tra biến nhập
if end < start:
    print("Số kết thúc cần lớn hơn số bắt đầu.")
else:
    # Bước 3: Bắt đầu xử lý việc in kết quả
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
