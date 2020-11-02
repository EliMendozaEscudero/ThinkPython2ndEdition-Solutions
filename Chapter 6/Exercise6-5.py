def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__=='__main__':
    while(True):
        a=int(input("a:"))
        b=int(input("b:"))
        gcd_a_b=gcd(a,b)
        print(f"The greatest common divisor of {a} and {b} is {gcd_a_b}")
        op = int(input("0.-To exit\n1.-Enter to check for other case."))
        if op == 0:
            break
        

