def do_twice(f,arg):
    """It runs a function twice
    f:Name of the function
    arg: Argument passed to the function 
    """
    f(arg)
    f(arg)

def do_four(f,arg):
    """It runs a function four times.
    f:Name of the function.
    arg:Argument passed to the function.
    """
    for i in range(4):
        f(arg)

def print_twice(bruce):
    """Print the argument twice.
    bruce: A printable object.
    """"
    print(bruce)
    print(bruce)

def print_spam():
    """It prints the word 'Spam'"""
    print('Spam')

if __name__=='__main__':
    do_four(print_twice,'Spam')