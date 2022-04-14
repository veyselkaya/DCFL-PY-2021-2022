import  turtle as t
import  random as rand



def cember(yaricap):
    t.speed(20)
    t.circle(yaricap)

renk = ["red", "blue", "green", "yellow", "indigo", "lime"]


for i in range(30):
    for i in range(6):
        t.color(renk[rand.randint(0,5)])
        cember(i * 10)

    for i in range(6):
        t.color(renk[rand.randint(0,5)])
        cember(i * 10)

t.left(90)

for i in range(30):
    for i in range(6):
        t.color(renk[rand.randint(0,5)])
        cember(i * 10)

    for i in range(6):
        t.color(renk[rand.randint(0,5)])
        cember(i * 10)


t.mainloop()