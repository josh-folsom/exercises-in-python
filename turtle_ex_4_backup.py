from random import *
from math import *
from turtle import *

#string = float[1, 2, 3, 4, 5, 6, 7]

#def nifty():
#    for x in range(11, 55, 3):
#        return randrange(5, 30)
def vary():
    randint(2, 7)

def repeat(times, f):
    for i in range(times): f()

def smaller():
    width(randint(2, 7))

def walk():
#    for i in [1, 2, 3]:
#        forward(10 + i)
#        left(10 + i)
    goto(randint(-300, 300), randint(-300, 300))
#    goto(random.sample(range(100), 10))
#    left(random.sample(range(100), 10))

#    for i in range(0, 10):
    #forward(random.randint(30,100))
    #left(random.randint(30,100))

def star():
    for i in range(5):
        def nifty():
            for x in range(11, 55, 3):
                return randrange(5, 30)
        forward(nifty())
#        forward(random.randint(30,100))
#        forward(random.sample(range(100), 10))
        right(144)
    pendown()
        #bgcolor("black")
        #color("white")
    begin_fill()

    width(2)
    end_fill()
    penup()
    walk()
    pendown()
#    for q in range(15):
#        star()

speed(0)
#goto(x, y=None)
bgcolor("black")
color("white")
#begin_fill()
#smaller()
#end_fill()
#penup()
#walk()
#pendown()

#penup()




repeat(10, star)


mainloop()
