#!/usr/bin/env python3

#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.

# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

def nums_to_letters(text):
    result = []
    for item in text.split():
        if item.isdigit():
            num = int(item)
            if num == 0:
                result.append(' ')
            elif 1 <= num <= 26:
                result.append(chr(num + 96))
            else:
                result.append(item)
        else:
            result.append(item)
            
    return ''.join(result)


print(nums_to_letters("8 5 12 12 15")) # hello
print(nums_to_letters("8 5 12 12 15 , 0 23 15 18 12 4 !")) # hello, world!
