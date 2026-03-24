import turtle

turtle.bgcolor("teal")
t = turtle.Turtle()
t.pensize(10)
t.color("black")
ns = int(input("Enter the number of sides on a polygon: "))
angle = 360/ns
for i in range(ns):
    t.forward(100)
    t.left(angle)
turtle.done()
   