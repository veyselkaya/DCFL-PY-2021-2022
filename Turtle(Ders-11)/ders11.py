import turtle as t

t.pen(pensize=2, fillcolor="red", speed=0)



t.left(90)

for i in range(5):
    for i in range(10):
        t.forward(50)
        t.left(45)
        t.forward(30)
        t.back(30)
        t.right(90)
        t.forward(30)
    t.left(10)



t.mainloop()