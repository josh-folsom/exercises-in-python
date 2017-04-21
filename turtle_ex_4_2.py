from random import *
from math import *
from turtle import *

#def vary():
    #randint(2, 7)

def repeat(times, f):
    for i in range(times): f()

def smaller():
    width(randint(2, 7))

def walk():
    goto(randint(-300, 300), randint(-300, 300))

def star(size):
    for i in range(5):
        def nifty():
            for x in range(11, 55, 3):
                return randrange(5, 30)

        forward(size)
        right(144)

    pendown()
    begin_fill()
    width()
    end_fill()
    penup()
    walk()

speed(0)
bgcolor("black")
color("white")
repeat(10, star)
mainloop()
