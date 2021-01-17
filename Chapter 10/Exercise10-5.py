def is_sorted(t):
	"""It take a list and returns True if it's sorted in 
	ascending order and False otherwise."""
	t1 = t[:]         	
	t1.sort()
	if t == t1:		
		return True
	else:
		return False

if __name__=='__main__':
	t = [42,1,32,0,-2341,2]
	t1 = [1,3,5,10,100]
	print(str(t)+'\nSorted: '+str(is_sorted(t)))
	print(str(t1)+'\nSorted: '+str(is_sorted(t1)))
