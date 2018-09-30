"""
作者 sky
版本 1.0
"""
import turtle


def draw_fractal_branch(branch_length):
    """绘制分形树"""
    if branch_length > 5:
        if branch_length <= 30:
            turtle.pencolor('green')
            turtle.pensize(1)

        turtle.forward(branch_length)
        turtle.right(20)
        draw_fractal_branch(branch_length - 15)

        turtle.left(40)
        draw_fractal_branch(branch_length - 15)

        turtle.right(20)
        turtle.backward(branch_length)

        if branch_length >= 30:
            turtle.pencolor('brown')
            turtle.pensize(2)


def main():
    """
    主函数
    """
    turtle.left(90)
    turtle.penup()
    turtle.backward(300)
    turtle.pendown()
    turtle.pencolor('brown')
    turtle.pensize(2)
    draw_fractal_branch(120)

    turtle.penup()
    turtle.forward(550)
    turtle.pendown()
    turtle.pensize(6)
    turtle.pencolor('blue')
    turtle.write('sky painting', font=('标题', 40))

    turtle.exitonclick()




if __name__ == '__main__':
    main()