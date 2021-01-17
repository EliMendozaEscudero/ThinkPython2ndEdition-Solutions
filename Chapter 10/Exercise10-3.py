def middle(t):
	"""It takes a list and return a new list with all but 
	the first and last elements."""
	t1 = t[:]
	del t1[0]
	del t1[len(t1)-1]
	return t1

if __name__=='__main__':
		t = [True,'Hello world',431,None,12] 
		print('Original: ' + str(t))
		print('Modified : ' + str(middle(t)))
