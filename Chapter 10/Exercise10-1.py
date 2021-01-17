def nested_sum(t):
	"""It adds up all the elements from all of 
   nested list."""
	su = 0	
	for e in t:
		if isinstance(e,list):
			su += nested_sum(e)
		else:
			su += e
	return su

if __name__=='__main__':
	t = [[1, 2], [3,[1,2,4,[42,1]]], [4, 5, 6]]
	print('List: '+str(t))
	print('Sum : '+str(nested_sum(t)))
		
