import turtle
import math

# refactor circle_v2() and arc() to use polyline() instead of polygon()
# ignore polygon() and circle(), created just for testing
# cleaned up the function interfaces by basing the value of n depending on the circle's circumference
# .. where value of n is not manually entered
# after arc is refactored, update circle [circle_v3()] to use arc()


def polygon(t, n, length):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)


def polyline(t, n, length_fd, angle_lt):
    """
    t = turtle will be used to draw polyline
    n = number the loop will be repeated, as number of sides
    length_fd = unit in pixels, length of each turtle
    angle_lt = unit in degrees, angle for each left turn a turtle makes
    """
    for p in range(n):
        t.fd(length_fd)
        t.lt(angle_lt)


def circle(t, r):
    circumference = math.pi * 2 * r
    n = int(circumference / 3) + 1
    length = int(circumference / n)
    angle = 360/n
    # print(circumference)
    # print('n =', n)
    # print('length =', length)
    # print('angle =', angle)
    polygon(t, n, length)


def circle_v2(t, r):    # update circle() to use polyline()
    circumference = math.pi * 2 * r
    n = int((circumference / 3) + 1)
    length_fd = int(circumference / n)
    angle_lt = 360/n
    # print('circumference =', circumference)
    # print('n =', n)
    # print('length_fd =', length_fd)
    # print('angle_lt', angle_lt)
    polyline(t, n, length_fd, angle_lt)


def arc(t, r, angle_arc):  # update arc() to use polyline()
    """
    t = turtle to draw the circle
    r = unit in pixels, radius of the circle
    angle_arc = unit in degrees, used to draw part of the circle; angle_arc=360 equals to a full circle
    """
    circumference = math.pi * 2 * r
    n = int((circumference / 3) + 1)
    length_fd = int(circumference / n)
    angle_lt = 360 / n
    arc_length = int((angle_arc / 360 * n))
    # print('circumference =', circumference)
    # print('n =', n)
    # print('length_fd =', length_fd)
    # print('angle_lt', angle_lt)
    # print('arc_length =', arc_length)
    polyline(t, arc_length, length_fd, angle_lt)


def circle_v3(t, r):  # update circle_v3 to use arc()
    arc(t, r, angle_arc=360)

bob = turtle.Turtle()

# polygon(bob, n=5, length=100)
# circle(bob, 40)

# use polyline to create a square
# polyline(bob, n=4, length_fd=100, angle_lt=int(360/4))

# use polyline to create a circle
# polyline(bob, n=360, length_fd=2, angle_lt=1)

# use polyline to create an arc, half circle
# polyline(bob, n=180, length_fd=2, angle_lt=1)

# circle() using polyline()
# circle_v2(bob, 80)

# arc() using polyline
# arc(bob, r=40, angle_arc=180)

# circle_v3() using arc()
circle_v3(bob, r=40)

turtle.mainloop()
