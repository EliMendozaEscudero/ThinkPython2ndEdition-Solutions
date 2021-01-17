def cumsum(t):
	"""It returns a list with the cumulative sum 
	of every element in a list"""
	t1 = t[:]
	leng = len(t1)
	for i in range(1,leng):
			t1[i] = t1[i-1] + t1[i]
	return t1
	
if __name__ == '__main__':
		t = [1,2,3,4,5,6]
		print('Original: '+str(t))
		print('Modified : '+ str(cumsum(t)))
