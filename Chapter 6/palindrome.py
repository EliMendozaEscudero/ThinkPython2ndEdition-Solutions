#Exercise 6-3 from "Think python 2e"
def first(word):
    """It returns the first character of a string"""
    return word[0]

def last(word):
    return word[-1]

def midle(word):
    return word[1:-1]

def is_palindrome(word):
    """It checks whether or not a word is palindrome"""
    return is_palindrome_not_inclusive(word.upper())

def is_palindrome_not_inclusive(word):
    """It checks whether or not a word that only contains
    upper case letters or only contains lower case letters is palindrome."""  
    if len(word)<2:
        return True
    elif first(word)==last(word) and is_palindrome(midle(word)):
        return True
    else:
        return False

if __name__== "__main__":
    print(midle("ab"))
    print(midle("a"))
    while(True):
        word = input("Type a word to check whether or not it is palindrome or just press enter to exit:\n")
        if len(word) > 0:
            print(word + (" is palindrome." if is_palindrome(word) else " is not palindrome.")) 
        else:
            break
