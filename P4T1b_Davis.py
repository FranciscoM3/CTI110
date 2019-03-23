# Draw initials using the turtle function.
# 01MAR2019
# CTI-110 P4T1B - Initials
# Francisco Davis
#
# Import Turtle
# Modify turtle functions
# Using the turtle function to include 'penup'/'pendown' /
# draw first and second initial of my name.


import turtle
wn = turtle.Screen()
wn.bgcolor('lightgray')
wn.title('My Turtle Initials')

Don = turtle.Turtle()
Don.shape('turtle')
Don.color('red')
Don.pensize(8)
Don.speed(3)
 # 'F'
Don.backward(80)
Don.right(90)
Don.forward(50)
Don.left(90)
Don.forward(50)
Don.backward(50)
Don.right(90)
Don.forward(60)
Don.left(90)

Don.penup()
Don.forward(150)
Don.pendown()

Don.color('black')
Don.left(90)
# 'D'
Don.forward(110)
Don.right(90)
for curve in range(12):
    Don.forward(16)
    Don.right(16)

turtle.exitonclick()
