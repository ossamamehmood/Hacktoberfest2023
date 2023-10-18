import turtle

t = turtle.Turtle()
radius = 10
n = 8
for i in range(1, n + 1):
    t.circle(radius * i)
turtle.done()
