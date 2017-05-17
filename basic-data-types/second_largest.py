
if __name__ == '__main__':
		n = int(raw_input())
		arr = map(int, raw_input().split())
		print(list(sorted(set(arr)))[-2])