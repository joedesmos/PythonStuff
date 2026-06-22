#imports
from turtle import *
import random
import time

#settings
screensize(1000, 1000)

#colors
pen_colors = ["blue", "red", "green", "turquoise", "black", "pink", "gray", "brown", "teal"]

#First shape(progressively gets bigger)
goto(0,0)
pensize(10)
speed(10)
for i in range(500):
    forward(i + 10)
    right(i + 5)
    color(random.choice(pen_colors))
penup()
clear()

#Second shape(spiral)
goto(0,0)
pendown()
pensize(5)
speed(10)
color("teal")
for i in range(250):
    forward(i)
    right(15)
penup()
clear()

#Third shape(Dots)
goto(0,0)
penup()
pensize(50)
speed(10)
for i in range(1000000):
    goto(random.randint(-1000, 1000), random.randint(-1000, 1000))
    color(random.choice(pen_colors))
    pendown()
    forward(0.00001)
    penup()
clear()

#Finish
done()