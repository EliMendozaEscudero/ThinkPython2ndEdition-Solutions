import math

def mysqrt(a):
    """It calculates the square root of a positive integer.
    a:The positive integer."""
    x=1
    while True:
        y = (x + a/x) / 2
        if y == x:
            return x
        x = y

def test_square_root():
    """It measure the difference between mysqrt function
    and the math.sqrt function using the numbers from 1 
    to 9. And print it into a table"""
    print('a\tmysqrt(a)\tmath.sqrt(a)\tdiff')
    print('-\t---------\t------------\t----')
    for a in range(1,10):
        mysqrta=mysqrt(a)
        sqrta=math.sqrt(a)
        diff=abs(mysqrta-sqrta)
        print('%.1f\t%f \t%f\t%g'%(a,mysqrta,sqrta,diff))


if __name__=='__main__':
    test_square_root()
