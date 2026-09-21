#!/usr/bin/env python3

#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.
# Одинаковых значение может быть два и более !
# Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]


# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.


def FindMinDistances(mass):
    last_seen = {}
    min_distances = {}

    for current_index, value in enumerate(mass):
        if value in last_seen:
            prev_index = last_seen[value]
            distance = current_index - prev_index
            if value not in min_distances or distance < min_distances[value]['dist']:
                min_distances[value] = {'dist': distance, 'indices': (prev_index, current_index)}
        last_seen[value] = current_index
    return min_distances

mass = [1, 2, 17, 54, 30, 89, 2, 1, 6, 2]
results = FindMinDistances(mass)

if results:
    for value, data in results.items():
        print(f"Число {value}: минимальное расстояние = {data['dist']}, индексы: {data['indices'][0]} и {data['indices'][1]}")
else:
    print("Повторяющиеся элементы не найдены")

