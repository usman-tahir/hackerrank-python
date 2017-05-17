
if __name__ == '__main__':
		arr = []
		for x in range(int(raw_input())):
				name = raw_input()
				grade = float(raw_input())
				arr.append([name, grade])

		second_highest = list(sorted(set([grade for name, grade in arr])))[1]
		print('\n'.join(sorted([student for student, grade in arr if grade == second_highest])))