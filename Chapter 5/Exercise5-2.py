def check_fermat( a, b, c,n):
    """It checks if the Fermat's theorem 
    holds for a certain case"""
    if(a**n + b**n != c**n and n>2 ):
        print("No, it doesn't work")
    else:
        print("Holy smokes, Fermat was wrong!")

def ask_for_test_cases():
    a=int(input("Value of a:"))
    b=int(input("Value of b:"))
    c=int(input("Value of c:"))
    n=int(input("Value of n:")) 
    check_fermat(a,b,c,n)

if(__name__=="__main__"):
    ask_for_test_cases()
