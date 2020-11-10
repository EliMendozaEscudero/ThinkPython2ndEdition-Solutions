import polygon
import math
import turtle

def draw_a_side(t,size,angle):
    """It prints a line using turtle and turns turtle n degres
    t:The turle instance
    size:The length of the line
    angle:The degrees to turn turle.
    """
    t.fd(size)
    t.lt(angle)


def print_shape(t,n):
    """It prints a shape as shown in the exersice. 
    t:Te turtle instance
    n: The numbers of sides of the shape.
     """
    teta=360/(n*2)
    alpha=(n-2)*90/n
    side1=50
    side2=25.0/(math.sin(teta*(math.pi/180)))
    for i in range(n):
        draw_a_side(t,side2,180-alpha)
        draw_a_side(t,side1,180-alpha)
        draw_a_side(t,side2,180)

def move(t, length):
    """It moves Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()

if __name__ == '__main__':
    bob = turtle.Turtle()
    move(bob,300)
    print_shape(bob,5)
    bob.lt(180)
    move(bob,300)
    print_shape(bob,6)
    move(bob,300)
    print_shape(bob,7)
    turtle.mainloop()
