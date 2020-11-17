def has_no_e(word):
    """It returns True if the word doesn't have any 
    'e' character and False otherwise."""
    for c in word:
        if c == 'e':
            return False
    return True

if __name__=='__main__':
    fin = open('words.txt')
    count = 0
    total = 0
    for word in fin:
        if has_no_e(word):
            print(word)
            count += 1 
        total += 1
    percentage = count * 100 / total
    print('The {:.2f}% of all the words in the list have no "e"'.format(percentage))
