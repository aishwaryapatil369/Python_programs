# draw an equilateral triangle
import turtle

wn = turtle.Screen()
norvig = turtle.Turtle()

for i in range(3):
    norvig.forward(100)

    # the angle of each vertice of a regular polygon
    # is 360 divided by the number of sides
    norvig.left(360/3)

wn.exitonclick()