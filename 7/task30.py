#!/usr/bin/env python3

#todo: Напишите лямбду функцию которая возвращает максимальное число
# из 2 переданных чисел

my_max = lambda a, b: a if a > b else b
print(my_max(15, 42))

# #todo: Для каждого значения из списка mass получите
# # список проверок(True или False) вхождений значений в диапазон от 1 до 130
mass = [122, 23, 1425, 23, 768, 4, 67, 998, 4, 6, 867]

flags = [1 <= val <= 130 for val in mass]
print(flags)


#todo: Отсортируйте список с помощью функции filter()
# и получите итоговый список только нечетных значений
list_ = [ 10, 11, 14, 25, 33, 36, 100, 101 ]
print(list(filter( lambda val:  val%2 != 0,  list_ )))


#todo: Отсортируйте список по расширению ".mp3"
files = ['file.txt', 'file2.mp3', 'file.pdf', 'file3.mp3', '.mp3le.doc']

mp3_files = list(filter(lambda filename: filename.endswith('.mp3'), files))
print(mp3_files)

