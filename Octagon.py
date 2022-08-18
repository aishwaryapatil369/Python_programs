
import turtle

wn = turtle.Screen()
knuth = turtle.Turtle()

for i in range(8):
    knuth.forward(75)
    knuth.left(360/8)

wn.exitonclick()