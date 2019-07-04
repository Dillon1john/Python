import turtle
wn= turtle.Screen()
pen=turtle.Turtle()
pen.pensize(3)
pen.pencolor("black")
for i in range(7):
    for j in range(12):
        pen.forward(6)
        pen.right(8)
pen.forward(100)
pen.right(132)
pen.forward(156)
pen.right(110)
pen.forward(124)
pen.right(110)
pen.forward(60)
turtle.done()
wn.exitonclick()
