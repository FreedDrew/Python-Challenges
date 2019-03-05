def disemvowel(string):
	vowels = ('A', 'E', 'I', 'O', 'U')
	for i in string.upper():
		if i in vowels:
			string = string.replace(i, "")
	vowels = ('a', 'e', 'i', 'o', 'u')
	for i in string.lower():
		if i in vowels:
			string = string.replace(i, "")
	return string
