import turtle
wn= turtle.Screen()
pen= turtle.Turtle()
pen.pensize(5)
for i in range(3):
    for j in range(15):
        pen.forward(30)
        pen.right(10)
turtle.done()
wn.exitonclick() #Finish the program by clicking on the graphics screen
