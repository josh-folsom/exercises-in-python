from random import *
from math import *
from turtle import *

rando = randint(5, 10)

def repeat(times, f):
    for i in range(times): f()

def walk():
    goto(randint(-500, 500), randint(-500, 500))

def star(min=10, max=25):
    end_fill()
    r = randint(min, max)
    begin_fill()
    pensize(5)

    for i in range(5):
        forward(r)
        right(144)
    pendown()
#    filling()
#    pensize(5)
    width(2)
#    end_fill()
    penup()
    walk()
    pendown()
    

speed(0)
bgcolor("black")
color("white")

repeat(20, star)

mainloop()
