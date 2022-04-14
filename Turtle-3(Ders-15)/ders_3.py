import  turtle as t

t.speed(20)
renkler = ["red", "blue", "green", "yellow", "indigo", "lime"]
for i in range(36):
    t.color(renkler[i%6])
    t.circle(5*i)
    t.circle(-5*i)
    t.left(i)

t.mainloop()