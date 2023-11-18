import turtle
import math

screen = turtle.Screen()
screen.setup(500, 500)

t = turtle.Turtle()
t.penup()
t.goto(200,0)
t.pendown()
for my_time in range(0,720):
    my_angle = my_time * math.pi / 180.0
    x = int(200 * math.cos(my_angle))
    y = int(200 * math.sin(my_angle))
    t.goto(x,y)

turtle.mainloop()