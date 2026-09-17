#!/usr/bin/env python3

#  todo: Дан номер месяца (1 — январь, 2 — февраль, ...). Вывести название соответствующего
#  времени года ("зима", "весна" и т.д.).

def ReadNumber(str):
	msg = """
	Need an integer from 1 to 12. Try again
	"""
	while (True):
		input_str = input(f"{str}: ")
		try:
			value = int(input_str)
			if value >= 1 and value <= 12:
				return value
			else:
				print(msg)	
		except:
			print(msg)


month_num = ReadNumber("Enter month number")

if month_num <= 2 or month_num == 12:
	month_str = "Зима"
elif 3 <= month_num and month_num <= 5:
	month_str = "Весна"
elif 6 <= month_num and month_num <= 8:
	month_str = "Лето"
else:
	month_str = "Осень"

print(month_str)