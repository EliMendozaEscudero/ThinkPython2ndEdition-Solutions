def is_power(a,b): 
    if b==1 and a!=b: 
        return False
    elif a%b==0 and is_power(a/b,b) or a==b:
        return True
    else:
        return False

if __name__=='__main__':
    while(True):
        a = int(input("a:"))
        b = int(input("b:"))
        print(str(a) +" is "+("" if is_power(a,b) else "not ")+"power of "+str(b))
        op = int(input("What would you like to do?\n\t1.-Check other case.\n\t2.-Exit.\n"))
        if  op == 1:
            continue 
        else: 
            break
