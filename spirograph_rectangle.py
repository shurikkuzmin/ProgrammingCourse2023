import turtle
import math

screen = turtle.Screen()
screen.setup(500, 500)

t = turtle.Turtle()
t.speed(0)

#a = 150
#b = 300
a=20
b=80

def draw_rectangle(my_time):
    remainder_time = my_time % (2*(a+b))
    x, y = 0, 0
    if remainder_time < b:
        x = int(a/2)
        y = int(remainder_time)- int(b/2)
    elif remainder_time < b + a:
        x = b + int(a/2) -int(remainder_time)
        y = int(b/2)
    elif remainder_time < 2*b + a:
        x = -int(a/2)
        y= int(1.5*b) + a - int(remainder_time)
    else:
        x = int(remainder_time) - 2*b - 1.5*a
        y =-int(b/2)
    return x,y

t.goto(a/2,-b/2)
for my_time in range(0,2000):
    my_angle = my_time * math.pi / 180.0

    x, y = draw_rectangle(3*my_time)
    #xnew = x + int(20*math.cos(7.5*my_angle))
    #ynew = y + int(20*math.sin(7.5*my_angle))

    xnew = x + int(200*math.cos(-4.1*my_angle))
    ynew = y + int(200*math.sin(-4.1*my_angle))
    
    t.goto(xnew,ynew)

turtle.mainloop()