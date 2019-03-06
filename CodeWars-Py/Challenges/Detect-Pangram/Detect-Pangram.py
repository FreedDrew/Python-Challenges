import string

def is_pangram(s):
		s = s.lower()
		s = set(s)

		alphabet = [ch for ch in s if ord(ch) in range(ord('a'), ord('z') + 1)]

		if len(alphabet) == 26:
			return True
		else:
			return False
