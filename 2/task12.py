#!/usr/bin/env python3

# todo: Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм,
#  4 — тонна, 5 — центнер. Дан номер единицы массы и масса тела M в этих единицах (вещественное число).
#  Вывести массу данного тела в килограммах

def ReadNumber(str):
	msg = """
	Need an integer from 1 to 5. Try again
	"""
	while (True):
		input_str = input(f"{str}: ")
		try:
			value = int(input_str)
			if value >= 1 and value <= 5:
				return value
			else:
				print(msg)	
		except:
			print(msg)

def ReadFloat(str):
	msg = """
	Need a real non negative value. Try again
	"""
	while (True):
		input_str = input(f"{str}: ")
		try:
			value = float(input_str)
			if value >= 0:
				return value
			else:
				print(msg)	
		except:
			print(msg)


num = ReadNumber("Enter number: 1 — килограмм, 2 — миллиграмм, 3 — грамм,  4 — тонна, 5 — центнер")
M = ReadFloat("Enter mass")

match num:
	case 1:
		M_kg = M
	case 2:
		M_kg = M * 1e-6
	case 3:
		M_kg = M * 1e-3
	case 4:
		M_kg = M * 1e3
	case 5:
		M_kg = M * 1e2

print(f"M in kg = {M_kg}")