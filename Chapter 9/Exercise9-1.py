def print_larger(fo,minlen):
    """Function that print all the words with more than
    a x number of characters.
    fo: File object to read from.
    minlen: Minimum number of characters."""
    for line in fin:
        word = line.strip()
        if len(word) > minlen:
            print(word)
 
if __name__=='__main__':
    fin = open('words.txt')
    print_larger(fin,20) 
