# Create snowflakes using the turtle function.
# 02MAR2019
# CTI-110 P4T1C - Snowflakes
# Francisco Davis
#
# Import Turtle and random
# Modify two turtles
# Using the for loop create two shapes/
# N-sided polygon and advance snowflake
# Create a for loop to display multiple snowflakes

import turtle
import random

wn = turtle.Screen()
wn.bgcolor('lightgray')
wn.title('Snowflake')

snow= turtle.Turtle()
color_mix= ['cyan','purple','white','blue','magenta']
snow.pensize(3)
snow.speed(8)

flakes= turtle.Turtle()
flakes.speed(0)
flakes.pensize(3)
flakes.penup()
flakes.backward(200)
flakes.left(90)
flakes.forward(250)
flakes.pendown()

for x in range(10):
    snow.color(random.choice(color_mix))
    for x in range(2):
        snow.forward(100)
        snow.right(60)
        snow.forward(80)
        snow.right(120)
    snow.right(36)

def flake_full():
    for y in range(8):
        flakes.left(45)
        for y in range(3):
            for y in range(3):
                flakes.forward(15)
                flakes.backward(15)
                flakes.right(45)
            flakes.left(90)
            flakes.backward(15)
            flakes.left(45)
        flakes.right(90)
        flakes.forward(45)

for z in range(4):
    flakes.color(random.choice(color_mix))
    flake_full()
    flakes.penup()
    flakes.backward(30)
    flakes.right(90)
    flakes.forward(450)
    flakes.pendown()
    
wn.exitonclick()
