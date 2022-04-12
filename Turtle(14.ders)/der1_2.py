import  turtle as t


t.speed(20)

for i in range(10):
    t.penup()
    t.goto(0, 200)
    t.pendown()

    t.color("blue")
    for i in range(4):
        t.forward(100)
        t.left(90)

    t.penup()
    t.goto(0, -200)
    t.pendown()

    t.color("red")
    for i in range(4):
        t.forward(100)
        t.left(90)

    t.penup()
    t.goto(-200, 0)
    t.pendown()

    t.color("yellow")
    for i in range(4):
        t.forward(100)
        t.left(90)

    t.penup()
    t.goto(200, 0)
    t.pendown()

    for i in range(4):
        t.forward(100)
        t.left(90)

    t.left(36)


t.mainloop()