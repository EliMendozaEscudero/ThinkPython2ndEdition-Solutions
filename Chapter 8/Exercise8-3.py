def is_palindrome(word): return  word.upper() == word[::-1].upper()

if __name__=='__main__':
    word = input('Word to check: ')
    print('"'+word + '" is' +('' if is_palindrome(word) else ' not')
        +' a palindrome.')
