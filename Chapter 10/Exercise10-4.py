def chop(t):
	"""It takes a list and modify it by removing 
	the first and last elements, and returns None."""
	del t[0]
	del t[len(t)-1]
	return None

if __name__=='__main__':
		t = [True, 'Hello world', 431, None, 12]
		print('Original: '+ str(t))
		chop(t)
		print('Modified: '+str(t))
