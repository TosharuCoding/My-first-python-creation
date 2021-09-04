import turtle
turtle.pensize(5)

def drawUp():
    turtle.seth(90)
    turtle.fd(20)
def drawDown():
    turtle.seth(270)
    turtle.fd(20)
def drawLeft():
    turtle.seth(180)
    turtle.fd(20)
def drawRight():
    turtle.seth(0)
    turtle.fd(20)

def setPurple():
    turtle.color('Purple')
def setGray():
    turtle.color('Gray')
def Eraser():
    turtle.color('White')

turtle.onkey(drawUp,'Up')
turtle.onkey(drawDown,'Down')
turtle.onkey(drawLeft,'Left')
turtle.onkey(drawRight,'Right')

turtle.onkey(setPurple,'p')
turtle.onkey(setGray,'w')
turtle.onkey(Eraser,'e')

turtle.listen()
