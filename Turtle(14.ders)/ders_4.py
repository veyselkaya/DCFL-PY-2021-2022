import turtle as t

t.speed(20)


for i in range(20):
    t.color("blue")
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.circle(30)

    t.color("red")

    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.circle(30)

    t.color("lime")
    t.penup()
    t.goto(100, 0)
    t.pendown()
    t.circle(30)

    t.color("green")

    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.circle(30)

    t.left(18)



t.mainloop()