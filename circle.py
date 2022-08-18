import turtle

wn = turtle.Screen()

alex = turtle.Turtle()
alex.pensize(4)
alex.shape("arrow")

for _ in range(10):

    alex.circle(120, 180)
    alex.stamp();

wn.exitonclick()