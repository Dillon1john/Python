import turtle
wn= turtle.Screen()
pen= turtle.Turtle()
pen.pensize(10)
pen.pencolor("blue")
for i in range(3):
    for j in range(4):
        pen.forward(100)
        pen.right(90)
    pen.right(120)
turtle.done()
wn.exitonclick() #Finish the program by clicking on the graphics screen
