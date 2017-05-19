
def swap_case(s):
		result = ''
		for letter in s:

				# If it's a lowercase letter
				if letter.lower() == letter:
						result += letter.upper()
				else:
						result += letter.lower()
		return result