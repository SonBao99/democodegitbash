# draw a square
import turtle as a

a.pensize(5)
a.fillcolor("red")
a.begin_fill()
for i in range(3):
    a.forward(150)
    a.left(120)


a.end_fill()

a.exitonclick()