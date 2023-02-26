#draw rainbow benzene
import turtle
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
t = turtle.Pen()
t.speed(-1)
turtle.bgcolor("black")
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100 +1)
    t.forward(x)
    t.left(59)