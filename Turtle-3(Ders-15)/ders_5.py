import  turtle as t
import random as r

renkler = ["red", "blue", "green", "yellow", "indigo", "lime", "green"]
t.speed(20)
for i in range(50):
    t.begin_fill()
    t.color(renkler[i%6])
    for i in range(5):
        t.forward(50)
        t.left(144)
    t.end_fill()



    t.penup()
    t.goto(r.randint(-300, 300), r.randint(-300, 300))
    t.pendown()

    for i in range(5):
        t.forward(50)
        t.left(144)

    t.penup()
    t.goto(r.randint(-300, 300), r.randint(-300, 300))
    t.pendown()


    t.circle(i*5)




t.mainloop()