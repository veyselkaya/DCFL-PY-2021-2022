import turtle as t


def kare(kenar, x, y):
    t.speed(20)
    for i in range(4):
        t.forward(kenar)
        t.left(90)
    t.penup()
    t.goto(x,y)
    t.pendown()

def cember(yaricap, x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(yaricap)

#kare(50,100,80)
#kare(50, -100, 80)
#kare(50, 0, 100)
#kare(50, 0, -100)

for i in range(10):
    kare(50, 20, 20)
    t.left(36)

t.color("red")
for i in range(10):
    kare(100, 20, 20)
    t.left(36)

t.color("lime")
for i in range(10):
    cember(60, 100,100)
    t.left(36)

t.color("blue")
for i in range(10):
    cember(60, -100,-100)
    t.left(36)

t.mainloop()