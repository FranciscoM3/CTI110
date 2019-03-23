# Create my own N-sided polygon
# 19MAR2019
# CTI-110 P4HW4 - N-sided polygon
# Francisco Davis
#
# Import turtle and random
# Modify turtle function
# Use a nested for loop to create polygon


import turtle
import random

wn = turtle.Screen()
wn.bgcolor('darkgreen')
wn.title('Shapes')

shape= turtle.Turtle()
shape.pensize(5)
shape.speed(6)
colors= ['black', 'silver']



for n in range(6):
    for n in range(6):
        shape.color(random.choice(colors))
        shape.forward(120)
        shape.left(60)
    shape.left(60)
    



wn.exitonclick()
