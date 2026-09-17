#!/usr/bin/env python3

# todo: 10.1 Дано целое число A. Проверить истинность высказывания: «Число A является четным».
# todo: 10.2 Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».
# Примечание: В задании  требуется вывести логическое значение True, если выражение
# для введеных исходных данных является истинным, и значение False в противном случае.

def ReadNumber(str):
	msg = """
	Need an integer. Try again
	"""
	while (True):
		input_str = input(f"{str}: ")
		try:
			value = int(input_str)
			return value
		except:
			print(msg)


A = ReadNumber("Enter A")

is_even = A % 2 == 0

print(f"10.1 (Число {A} является четным): {is_even}")
print(f"10.2 (Число {A} является нечетным): {not is_even}")		
