import polygon
import turtle
def draw_a_petal(turt,arc):
    """It draws one petal of the flower
    turt:The turtle instance
    arc:The angle of the arcs.
    """
    for i in range(2):
        polygon.arc(turt,100,arc)
        turt.lt(180-arc)

def paint_flower(turt,petals):
    """It draws a flower of n petals
    turt:The turtle instance.
    petals:The number of petals.
    """
    arc=((petals-2)*180)/(petals*2)
    print(arc)
    for i in range(petals):
       draw_a_petal(turt,arc)
       turt.rt(360.0/petals)

def move(t, length):
    """It moves Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()

if __name__=='__main__':
    pat = turtle.Turtle()
    pat.speed(0)
    pat.lt(180)
    move(pat,250)
    paint_flower(pat,7)
    pat.lt(180)
    move(pat,250)
    paint_flower(pat,11)
    move(pat,250)
    paint_flower(pat,22)
    turtle.mainloop()
