#!/usr/bin/env python3

#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().

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


A = ReadNumber("Point A")
B = ReadNumber("Point B")
C = ReadNumber("Point C")


ac_len = abs(C - A)
bc_len = abs(B - C)
sum_len = ac_len + bc_len

print(f"AC: {ac_len}, BC: {bc_len}, Sum: {sum_len}")
