import turtle

turtle.bgcolor("teal")
t = turtle.Turtle()
t.pensize(4)
t.color("black")
t.shape("turtle")

size = 0
while True:
    for i in  range(4):
        t.fd(size)
        t.left(90)
        size = size - 5
    size = size + 1
       

