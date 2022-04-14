import turtle as t


def yuz(yaricap, goz):
    t.title("BEN PYTHONUMM")
    t.shapesize(1)
    t.pensize(2)
    t.bgcolor("black")
    t.pencolor("yellow")
    t.penup()
    t.goto(0, -150)
    t.pendown()
    t.circle(yaricap)
    t.penup()
    t.goto(0, -((20 * (3 ** (1 / 2))) / 2))
    t.color("red")
    t.pendown()
    t.forward(20)
    t.left(120)
    t.forward(40)
    t.left(120)
    t.forward(40)
    t.left(120)
    t.forward(20)
    t.penup()
    t.goto(37.5 * (2 ** (1 / 2)), 37.5 * (2 ** (1 / 2)))
    t.pendown()
    t.circle(goz)
    t.penup()
    t.goto(-(37.5 * (2 ** (1 / 2))), 37.5 * (2 ** (1 / 2)))
    t.pendown()
    t.circle(goz)

    t.penup()
    t.goto(+30, -75)
    t.pendown()
    t.backward(60)
    t.right(90)
    t.circle(30, 180)
    t.hideturtle()


yuz(200,25)


t.mainloop()
