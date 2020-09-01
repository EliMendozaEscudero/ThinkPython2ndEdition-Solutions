def print_filled_row(large):
    """It prints '+ - - - - ' n times and '+' at the end
    large: The n number of times to be printed.
    """
    print(large*('+ '+'- '*4), end='')
    print('+')

def print_empty_row(large):
    """It prints '|         ' n times and '|' at the end
    large: The n number of times to be printed.
    """
    print(large*('|'+' '*9), end = '')
    print('|')

def do_twice(f,arg):
    """It calls a function twice and pass an argument to the function.
    f:The function to be called.
    arg:The argument for the function.
    """
    f(arg)
    f(arg)

def do_four(f,arg):
    """It calls a function four times and pass an argument to the function.
    f:The function to be called.
    arg:The argument for the function.
    """
    do_twice(f,arg)
    do_twice(f,arg)

def print_grid(n):
    """It prints a squared grid of n*n  size."""
    for i in range(n):
        print_filled_row(n)
        do_four(print_empty_row,n)

    print_filled_row(n)

def print_small_grid():
    """It prints a grid of 2*2 size"""
    print_grid(2)

def print_big_grid():
    """It prints a grid of 4*4 size"""
    print_grid(4)

if __name__=='__main__':
    print('2x2 Grid:')
    print_small_grid()
    print('4x4 Grid:')
    print_big_grid()
