import turtle as t

t.bgcolor("black")
t.pen(pencolor="red", pensize=1, speed=0)


for i in range(6):
    for colours in ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]:
        t.color(colours)
        for i in range(4):
            t.forward(100)
            t.right(91)
        for i in range(3):
            t.forward(120)
            t.right(120)
        t.circle(100)
        t.left(10)

t.mainloop()
