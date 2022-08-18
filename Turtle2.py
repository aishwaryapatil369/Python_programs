import turtle
wn = turtle.Screen()
#wn.bgpic("")

alex = turtle.Turtle()
alex.color("Red")
alex.pensize(4)
alex.shape("circle")

dist = 6

alex.up()

for _ in range(30):
    alex.stamp()
    alex.backward(dist)
    alex.right(-30)
    dist = dist + 2

wn.exitonclick()
