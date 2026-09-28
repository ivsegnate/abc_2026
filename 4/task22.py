#!/usr/bin/env python3

#todo: Модифицировать программу таким образом чтобы она выводила
# приветствие "Hello", которое только что записали в файл text.txt

f = open("text.txt", "w+t")
f.write("Hello\n")
f.flush()
f.seek(0)

line = f.readline()
print(f"Hello from file: {line.strip()}")

f.close()