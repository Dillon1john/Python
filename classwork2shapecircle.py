import turtle
wn= turtle.Screen()
pen= turtle.Turtle()
pen.pensize(10)
for i in range(25):
    for j in range(10):
        pen.forward(30)
        pen.right(10)
pen.right(60)
pen.forward(100)
turtle.done()
wn.exitonclick() #Finish the program by clicking on the graphics screen
