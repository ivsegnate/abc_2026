#!/usr/bin/env python3

# todo: Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
# Примечание: коэффициенты получаем через функцию input().

def ReadNumber(str):
	msg = """
	Need a number. Try again
	"""
	while (True):
		input_str = input(f"{str}: ")
		try:
			value = float(input_str)
			return value
		except:
			print(msg)


msg = """
	The number must be non-zero.
	"""
eps = 1e-12
while (True):
	A = ReadNumber("Enter A")
	if abs(A) < eps:
		print(msg)
	else:		
		break

B = ReadNumber("Enter B")

x = -B / A
print(f"X = {x}")