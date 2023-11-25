import turtle
import math

screen = turtle.Screen()
screen.setup(500, 500)

t = turtle.Turtle()
t.speed(0)

a = 50
b = 100
t.goto(a/2, 0)
t.left(90)
for my_time in range(0,200):
#     #my_angle = my_time * math.pi / 180.0
#     #x = int(30 * math.cos(4.378*my_angle)) + int(200*math.cos(-my_angle))
#     #y = int(30 * math.sin(4.378*my_angle)) + int(200*math.sin(-my_angle))
    if t.ycor() > b/2:         
        t.left(90)
        t.sety(b/2)
    t.forward(1)

turtle.mainloop()