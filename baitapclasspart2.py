class SoHoc:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def print_info(self):
        print(f"Number 1: {self.number1}")
        print(f"Number 2: {self.number2}")

    def addition(self):
        return self.number1 + self.number2

    def subtract(self):
        return self.number1 - self.number2

    def multi(self):
        return self.number1 * self.number2

    def division(self):
        if self.number2 == 0:
            return "Không thể chia cho 0"
        return self.number1 / self.number2

# nhập 2 tham số trong ( , ) k nhạp báo lỗi ráng chịu
so_hoc_objec = SoHoc(10, 5)


so_hoc_objec.print_info()


result_addition = so_hoc_objec.addition()
print("Kết quả cộng:", result_addition)


result_subtract = so_hoc_objec.subtract()
print("Kết quả trừ:", result_subtract)


result_multi = so_hoc_objec.multi()
print("Kết quả nhân:", result_multi)


result_division = so_hoc_objec.division()
print("Kết quả chia:", result_division)
