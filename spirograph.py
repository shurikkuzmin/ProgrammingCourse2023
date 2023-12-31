import turtle
import math

screen = turtle.Screen()
screen.setup(500, 500)

t = turtle.Turtle()
t.penup()
t.goto(-230,20)
t.pendown()
for my_time in range(0,1000):
    my_angle = my_time * math.pi / 180.0
    x = int(50 * math.cos(-my_angle)) + 0.5*my_time - 250
    y = int(50 * math.sin(-my_angle)) + 20
    t.goto(x,y)

turtle.mainloop()