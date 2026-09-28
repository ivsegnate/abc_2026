#!/usr/bin/env python3

# todo: Шифр Цезаря
# Описание шифра.
# В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
# является одним из самых простых и широко известных методов шифрования.
# Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
# фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
# E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.

# Задача.
# Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
# В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.


def encrypt_char(char, shift):
    # А = 1040, Я = 1071
    if 1040 <= ord(char) <= 1071:
        return chr((ord(char) - 1040 - shift) % 32 + 1040)

    # а = 1072, я = 1103
    elif 1072 <= ord(char) <= 1103:
        return chr((ord(char) - 1072 - shift) % 32 + 1072)

    # Отдельная обработка буквы Ё
    elif ord(char) == 1025 or ord(char) == 1105:
        return char

    return char

def encrypt_line(line, shift):
	new_line = ""
	for char in line:
		new_line += encrypt_char(char, shift)
	return new_line

in_filename = "message.txt";
out_filename = "encrypted_message.txt";
in_file = open(in_filename, "r")
out_file = open(out_filename, "w")

lines = in_file.readlines()
print(lines)

for line_num, line in enumerate(lines):
    encrypted_line = encrypt_line(line, line_num + 1)
    print(encrypted_line)
    out_file.write(encrypted_line)

in_file.close()
out_file.close()

