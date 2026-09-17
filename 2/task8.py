#!/usr/bin/env python3

# todo: Проверить истинность высказывания: 
# "Данное четырехзначное число читается одинаково слева направо и справа налево".

def ReadNumber(str):
	msg = """
	Need a four-digit integer. Try again
	"""
	while (True):
		input_str = input(f"{str}: ")
		try:
			value = int(input_str)
			if value >= 1e3 and value < 1e4:
				return value
			else:
				print(msg)
		except:
			print(msg)

def ObtainDiguts(value):
	digits = []
	while value > 0:
		digits.append(value % 10)
		value //= 10
	return digits			


value = ReadNumber("Enter a four-digit integer")
digits = ObtainDiguts(value)

verdict = ((digits[0] == digits[3]) and (digits[1] == digits[2]))

print(digits)
print(verdict)