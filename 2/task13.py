#!/usr/bin/env python3

# В восточном календаре принят 60-летний цикл, состоящий из 12- летних подциклов,
# обозначаемых названиями цвета: зеленый, красный, желтый, белый и черный.
# В каждом подцикле годы носят названия животных: крысы, коровы, тигра, зайца, дракона,
# змеи, лошади, овцы, обезьяны, курицы, собаки и свиньи. По номеру года вывести его название,
# если 1984 год был началом цикла — годом зеленой крысы.

def ReadYear(str):
	msg = """
	Need an integer year from 1900 to 2043. Try again
	"""
	while (True):
		input_str = input(f"{str}: ")
		try:
			value = int(input_str)
			if value >= 1900 and value <= 2043:
				return value	
			else:
				print(msg)
		except:
			print(msg)


year = ReadYear("Enter year: ")

colors = ["Зеленый", "Красный", "Желтый", "Белый", "Черный"]
animals = ["Крыса", "Корова", "Тигр", "Заяц", "Дракон", "Змея", 
"Лошадь", "Овца", "Обезьяна", "Курица", "Собака", "Свинья"]
base_year = 1984

diff = year - base_year
color_index = (diff // 2) % len(colors)
animal_index = diff % len(animals)

color = colors[color_index]
animal = animals[animal_index]

print(f"{color}, {animal}")