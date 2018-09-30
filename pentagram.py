"""
作者 sky
版本 1.0
"""
import turtle


def draw_pentagram(size):
    # 计数器
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1


def main():
    """
    主函数
    """

    turtle.penup()
    turtle.backward(100)
    turtle.pendown()

    size = 100
    while size <= 200:
        draw_pentagram(size)
        size += 50

    turtle.penup()
    turtle.left(90)
    turtle.forward(120)
    turtle.pendown()
    turtle.pensize(6)
    turtle.pencolor('blue')
    turtle.write('sky painting', font=('标题', 40))
    turtle.exitonclick()


if __name__ == '__main__':
    main()