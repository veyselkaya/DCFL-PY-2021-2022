import turtle as t


t.speed(20)
renkler = ["red", "blue", "green", "yellow", "indigo", "lime", "green"]
t.bgcolor("black")


for i in range(360):
    t.pencolor(renkler[i%7])
    t.width(i//100+1)
    t.forward(i)
    t.left(59)


t.mainloop()