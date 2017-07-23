import turtle
import math

# Exercise 4 -- square()
# 1. takes a parameter named t, which is a turtle
#   it should use the turtle to draw a square
#   write a function call that passes bob as an argument to square, run the program
# 2. add another parameter, named length, to square
#     modify the body so length of the sides is length
#     modify the function call to provide a second argument, run the program again


def square(t, length):
    """t = turtle will be used to draw a square"""
    for i in range(4):
        t.fd(length)
        t.lt(90)


# Exercise 3 -- polygon()
# make a copy of square() and change the name to polygon()
# add another parameter named n
# modify the body so it draws an n-sided regular polygon


def polygon(t, length, n):
    """
    t = turtle will be used to draw square
    length = length of the sides
    n = n-sided regular polygon
    """
    for i in range(n):
        t.fd(length)
        t.lt(360/n)


# Exercise 4 -- circle()
# takes a turtle, t, and radius, r, as parameters
# that draws an approximate circle by calling polygon
# with an appropriate length and number of sides
# hint: figure out he circumference of the circle
#     and make sure that length * n = circumference


def circle(t, r):
    """
    t = turtle will be used to draw the square
    r = define the radius of the circle
    """
    circumference = math.pi * 2 * r
    n = 60
    length = circumference / n
    polygon(t, length, n)


# Exercise 5 -- arc()
# take an additional parameter called angle,
# which determines which fraction of a circle to draw
# angle is in unit of degrees
# when angle=360, arc should draw a complete circle


def arc(t, r, angle):
    """
    t = turtle will be used to draw the circle
    r = define the radius of the circle
    angle = unit of degrees, determines which fraction of a circle to draw
    """
    circumference = math.pi * 2 * r
    n = 60
    length = circumference / n
    arc_in = int(((angle / 360) * circumference) / 2)
    for i in range(arc_in):
        t.fd(length)
        t.lt(360/n)

bob = turtle.Turtle()

# square(bob, 100)
# polygon(bob, length=100, n=8)
# circle(bob, 60)
arc(bob, r=20, angle=360)


turtle.mainloop()



