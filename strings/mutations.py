
def mutate_string(string, position, character):
		letters = list(string)
		letters[position] = character
		return ''.join(letters)

if __name__ == '__main__':
		string = raw_input()
		index, character = raw_input().split()
		new_string = mutate_string(string, int(index), character)
		print(new_string)