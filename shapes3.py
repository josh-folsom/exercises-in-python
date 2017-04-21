from turtle import *

def triangle(arg1, arg2, arg3):
    for i in range(3):
        forward(arg1)
        filling(arg2)
        color(arg3)
        right(120)

def square():
    for i in range(4):
        forward(100)
        right(90)

def pentagon():
    for i in range(5):
        forward(100)
        left(72)

def hexagon():
    for i in range(6):
        forward(100)
        left(60)

def octagon():
    for i in range(8):
        forward(100)
        left(45)

def star():
    for i in range(5):
        forward(100)
        right(144)

def mycircle():
    width(1)
    circle(90)
    mainloop()
