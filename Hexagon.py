
import turtle as t
t.penup()

t.goto(-50,100)
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.pencolor("orange")
t.pensize(5)
t.speed(5)

for i in range(6):
    t.forward(100)
    t.left(300)

t.end_fill()
t.exitonclick()