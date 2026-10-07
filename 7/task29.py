#!/usr/bin/env python3

#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.


# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

def encrypt_char(char, shift):
    start = ord('a')
    if char.isalpha():
        return chr(start + (ord(char) - start - shift) % 26)
    return char

def encrypt_line(line, shift):
	new_line = ""
	for char in line:
		new_line += encrypt_char(char, shift)
	return new_line

msg = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

for shift in range(1, 26):
	decript_attempt = encrypt_line(msg, shift)
	print(f"{shift}: {decript_attempt}")

