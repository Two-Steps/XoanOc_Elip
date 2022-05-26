import turtle
import random

t = turtle.Turtle()
colors = ['gray', 'blue', 'red', 'purple', 'yellow', 'green', 'brown', 'pink']
angle = 0
while angle <=36:
    r = 0
    t.pencolor(random.choice(colors))
    while r < 2:
        t.circle(100, 90)
        t.circle(50, 90)
        r += 1
    t.lt(10)
    angle += 1
turtle.done()
