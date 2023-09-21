chieu_cao = int(input("nhập chiều cao (cm):")) / 100
can_nang = float(input("nhập cân nặng (kg):"))
BMI = can_nang / (chieu_cao ** 2)
print(f"nặng :{can_nang} kg , cao :{chieu_cao} cm, BMI = {BMI}")


if (chieu_cao <= 0 and can_nang <= 0):

    print("số nhập vào ko hợp lệ")

if BMI > 40 :

    print("béo phì cấp độ III")

elif 35 <= BMI < 40:

    print("béo phì cấp độ II") 

elif 30 <= BMI < 35:

    print("béo phì cấp I")

elif 25 <= BMI < 30:

    print("thừa cân")

elif 18.5 <= BMI <25 :

    print("bình thường")

elif 17 <= BMI < 18.5 :

    print("gầy cấp độ I")

elif 16 <= BMI < 17:

    print("gầy cấp độ II")
else:

    print("gầy cấp độ III")

