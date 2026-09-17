#!/usr/bin/env python3

#todo: Дана сторона квадрата a. Найти его площадь S = a²
# Примечание: сторону квадрата получаем через функцию input().

msg = """
	The side of a square must be a non-negative number.
	Try again
	"""

while (True):
	input_str = input("Side of square: ")
	try:
		a = float(input_str)
		if (a >= 0.0):
			break
		else:
			print(msg)
	except:
		print(msg)

s = a**2
print(f"Area of the square: {s}")