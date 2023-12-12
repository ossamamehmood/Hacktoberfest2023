import turtle
t = turtle.Turtle()
t.goto(0, -100)
t.pensize(10)
turtle.bgcolor("blue")
t.pencolor("red")
for i in range(0, 6):
    t.forward(100)
    t.left(60)


