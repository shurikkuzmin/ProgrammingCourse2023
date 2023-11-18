import turtle
import math

screen = turtle.Screen()
screen.setup(500, 500)

t = turtle.Turtle()
t.penup()
t.pendown()
for my_time in range(0,2000):
    my_angle = my_time * math.pi / 180.0
    x = int(30 * math.cos(4.378*my_angle)) + int(200*math.cos(-my_angle))
    y = int(30 * math.sin(4.378*my_angle)) + int(200*math.sin(-my_angle))
    t.goto(x,y)

turtle.mainloop()