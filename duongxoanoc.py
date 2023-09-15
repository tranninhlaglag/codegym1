import turtle

# Tạo một đối tượng Turtle
t = turtle.Turtle()

# Đặt màu nền và màu bút
turtle.bgcolor("black")
t.color("white")

# Đặt tốc độ vẽ của Turtle
t.speed(0)

# Khai báo các biến cho việc vẽ đường xoắn ốc
angle = 30  # Góc quay
length = 5  # Độ dài mỗi bước

# Vẽ đường xoắn ốc bằng vòng lặp while
while True:
    t.forward(length)
    t.right(angle)
    length += 1  # Tăng độ dài sau mỗi bước

    # Thoát vòng lặp khi độ dài quá lớn
    if length > 100:
        break

# Đóng cửa sổ khi nhấn chuột vào nó
turtle.exitonclick()
