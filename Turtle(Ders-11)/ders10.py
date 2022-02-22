import turtle as t


for i in range(4):
    t.forward(100)
    t.right(90)


for i in range(3):
    t.fillcolor("red")
    t.begin_fill()
    t.forward(100)
    t.left(120)
    t.end_fill()

t.mainloop()