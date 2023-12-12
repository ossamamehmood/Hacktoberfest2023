import turtle

t = turtle.Turtle()
t.pencolor("green")
screen = turtle.Screen()
screen.bgcolor("black")
a = 0
b = 0
t.speed(0)
t.goto(0, 210)
t.penup()
t.pendown()
while True:
    t.forward(a)
    t.right(b)
    a += 3
    b += 1
    if b == 210:
        break
    t.hideturtle()
turtle.done()
