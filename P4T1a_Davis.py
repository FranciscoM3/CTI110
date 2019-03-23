# Create shapes using the turtle function.
# 01MAR2019
# CTI-110 P4T1A - Turtle Graphics
# Francisco Davis
#
# Import Turtle
# Modify two turtles
# Using the for loop create two shapes/
# square and triangle
#


import turtle
wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.title('Turtle Programing')


Shelly = turtle.Turtle()
Shelly.shape("turtle")
Shelly.color('red')
Shelly.pensize(6)
Shelly.speed(2)

Sheldon = turtle.Turtle()
Sheldon.shape("turtle")
Sheldon.color('green')
Sheldon.pensize(6)
Sheldon.speed(2)
Sheldon.penup()
Sheldon.backward(150)
Sheldon.pendown()

for square in range(4):
    Shelly.forward(100)
    Shelly.left(90)
    
for square in range(3):
    Sheldon.forward(100)
    Sheldon.left(120)
    

turtle.exitonclick()
