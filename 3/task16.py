#!/usr/bin/env python3

# todo: База данных пользователя.
# Задан массив объектов пользователя

users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.

#Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе

# тип сортировки: 1

#Затем сообщение для ввода
# Ввидите критерии поиска: 16

# Результат:
#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"


print("""
Выберите тип фильтрации:"
    1. По возрасту (вывести тех, кто старше указанного)"
    2. По первой букве логина"
    3. По группе
""")

filter_type = input("Тип сортировки: ").strip()
criterion = input("Введите критерий поиска: ").strip()

filtered_users = []

if filter_type == '1':
    target_age = int(criterion)
    filtered_users = [u for u in users if u['age'] > target_age]

elif filter_type == '2':
    target_letter = criterion.lower()
    filtered_users = [u for u in users if u['login'].lower().startswith(target_letter)]

elif filter_type == '3':
    filtered_users = [u for u in users if u['group'].lower() == criterion.lower()]

filtered_users.sort(key=lambda u: u['age'])

print("Результат:")
if filtered_users:
    for u in filtered_users:
        age = u['age']
        if 11 <= age % 100 <= 14:
            age_word = "лет"
        elif age % 10 == 1:
            age_word = "год"
        elif age % 10 in [2, 3, 4]:
            age_word = "года"
        else:
            age_word = "лет"
            
        print(f"Пользователь: '{u['login']}' возраст {u['age']} {age_word} , группа \"{u['group']}\"")
else:
    print("Пользователи не найдены.")


