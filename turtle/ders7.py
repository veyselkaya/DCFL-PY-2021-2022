import turtle as t

t.bgcolor("black")
t.pen(pencolor="white", pensize=1, speed=0)

for i in range(50):
    for i in range(5):
        t.color("red")
        t.forward(100)
        t.right(72)

    for i in range(5):
        t.color("lime")
        t.forward(-100)
        t.right(72)
    t.right(15)



t.mainloop()
