import turtle as t

t.pensize(4)
t.goto(-100,0)
t.fillcolor("red")
t.pencolor("blue")
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.penup()
t.forward(150)
t.pencolor("green")
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()


t.exitonclick()