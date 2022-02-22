import turtle as t

t.penup()
t.goto(-350, 350)
t.pendown()



for i in range(4):
    t.forward(400)
    t.right(90)

t.penup()
t.goto(-345, 300)
t.pendown()

for i in range(4):
    t.forward(300)
    t.right(90)

t.mainloop()