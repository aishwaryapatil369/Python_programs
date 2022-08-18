import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("Blue")
alex.pensize(3)
alex.shape("turtle")
alex.penup()

for _ in range(10):
    alex.forward(70)
    alex.stamp()
    alex.forward(-70)
    alex.right(36)

wn.exitonclick()