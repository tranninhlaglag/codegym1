def ktcl(number):
    number = number % 2
    if number == 1:
        return "số lẻ"
    elif number == 0:
        return "sô chẵn"
    
def main():
    numer = int(input("nhập số cần kiểm tra :"))
    print(ktcl(numer))
main()        