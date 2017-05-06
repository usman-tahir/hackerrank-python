
def is_leap(year):
		leap = False

		div_4 = year % 4 == 0
		div_100 = year % 100 == 0
		div_400 = year % 400 == 0

		leap = (div_4 and not div_100) or (div_100 and div_400)
		return leap

year = int(raw_input())
print is_leap(year)