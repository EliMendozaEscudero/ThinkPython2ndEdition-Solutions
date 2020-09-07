import math

def eval_loop():
    """It ask the user for a mathematical statement 
    and evaluates it using the eval function. It do it again
    and again, until the user enters 'done'"""
    statement = ''
    while(True):
        statement = input('Enter a mathematical statement (or "done" to finish):\n')
        if (statement != 'done'):
            result = eval(statement)
            print(result)
        else:
            return result

if __name__ == '__main__':
    eval_loop()
