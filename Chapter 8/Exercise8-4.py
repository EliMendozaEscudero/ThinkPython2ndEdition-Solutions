def any_lowercase1(s):
    """It returns True if the first character of s is lower case and False otherwise.""" 
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    """It always returns the string 'True'"""
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    """It returns True if the last character of s is lower case and False otherwise"""
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    """It returns True if s contains any lower case character and False otherwise."""
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    """It returns False if s contains any upper case character and True otherwise."""
    for c in s:
        if not c.islower():
            return False
    return True    

