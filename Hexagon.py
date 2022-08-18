# draw a hexagon
import turtle

wn = turtle.Screen()
dijkstra = turtle.Turtle()

for i in range(6):
    dijkstra.forward(100)
    dijkstra.left(360/6)

wn.exitonclick()