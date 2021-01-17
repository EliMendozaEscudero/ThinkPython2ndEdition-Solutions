def is_anagram(s,s1):
	"""It takes two words and returns True if they are
	anagrams and False otherwise."""
	s = list(s)
	s1 = list(s1)
	s.sort()
	s1.sort()
	if s == s1:
		return True
	else:
		return False

if __name__=='__main__':
	s = input('First string:')
	s1 = input('Second string:')
	is_ana = is_anagram(s,s1)
	print(str(s),' and ',str(s1),'are'+(' ' if is_ana else "n't ") ,'anagrams.')

