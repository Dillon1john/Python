import turtle
wn= turtle.Screen()
pen= turtle.Turtle()
pen.pensize(5)
pen.pencolor("red")
for i in range(3):
    for j in range(12):
        pen.forward(30)
        pen.right(10)
pen.pencolor("blue")
pen.right(55)
pen.forward(300)
pen.right(125)
pen.forward(312)
pen.right(119)
pen.forward(283)
turtle.done()
wn.exitonclick() #Finish the program by clicking on the graphics screen

