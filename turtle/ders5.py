import  turtle as t


t.pen(pencolor="red", pensize=1, speed=0)

for i in range(100):
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(-100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
#for için eklendi
    t.left(91)



t.mainloop()