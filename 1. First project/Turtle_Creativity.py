import turtle
import time
flechita = turtle.Turtle()
flechita.speed(0)
flechita.color('red', 'yellow')
flechita.hideturtle()
flechita.begin_fill()
while True:
    flechita.fd(200)
    flechita.lt(170)
    if abs(flechita.pos()) < 1:
        break
flechita.end_fill()
time.sleep(3)
flechita.clear()
position1=flechita.pos()
flechita.speed(6)
flechita.color('red', 'yellow')
flechita.begin_fill()
list_position=[]
for i in range (4):
    flechita.rt(90)
    flechita.fd(100)
    list_position.append(flechita.pos())
flechita.color('red', 'yellow')
flechita.up() # No visible
flechita.setpos(50,50) # Setpos funciona como un go to a menos que se haga antes un .up
flechita.down() #Visible
list_position2=[]
for i in range (4):
    flechita.rt(90)
    flechita.fd(100)
    list_position2.append(flechita.pos())
for i,j in zip(list_position,list_position2):
    flechita.up()
    flechita.setpos(i)
    flechita.down()
    flechita.goto(j)
flechita.end_fill()
turtle.done()