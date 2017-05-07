
def parse_command(command, array):
		parsed_command = command.split(" ")

		# Commands of length 3 are typically insert commands
		if len(parsed_command) == 3:
				array.insert(int(parsed_command[1]), int(parsed_command[2]))
		# Commands of length 2 are typically remove or append commands
		elif len(parsed_command) == 2:
				if parsed_command[0] == 'remove':
						try:
								array.remove(int(parsed_command[1]))
						except ValueError:
								pass
				else:
						array.append(int(parsed_command[1]))
		# Commands of length 1 are typically used for printing, popping, sorting, or reversing the array
		else:
				if parsed_command[0] == 'print':
						print(array)
				elif parsed_command[0] == 'pop':
						array.pop()
				elif parsed_command[0] == 'sort':
						array = sorted(array)
				else:
						array = array[::-1]
		return array


if __name__ == '__main__':
		n = int(raw_input())
		current_list = []

		for x in range(n):
				current_command = raw_input()
				current_list = parse_command(current_command, current_list)
