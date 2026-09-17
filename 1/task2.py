# todo: Преобразуйте переменную age и foo в число
age = "23"
foo = "23abc"
age_int = int(age)
foo_digits = "";
for k in foo:
	if k.isdigit():
		foo_digits += k
foo_int = int(foo_digits)

print("age_int: ", age_int, type(age_int))
print("foo_int: ", foo_int, type(foo_int))

# Преобразуйте переменную age в Boolean
age = "123abc"
age_bool = bool(age)
print("age_bool: ", age_bool, type(age_bool))

# Преобразуйте переменную flag в Boolean
flag = 1
flag_bool = bool(flag)
print("flag_bool: ", flag_bool, type(flag_bool))

# Преобразуйте значение в Boolean
str_one = "Privet"
str_two = ""
str_one_bool = bool(str_one)
str_two_bool = bool(str_two)
print("str_one_bool: ", str_one_bool, type(str_one_bool))
print("str_two_bool: ", str_two_bool, type(str_two_bool))


# Преобразуйте значение 0 и 1 в Boolean
bool_0 = bool(0)
bool_1 = bool(1)
print("bool_0: ", bool_0, type(bool_0))
print("bool_1: ", bool_1, type(bool_1))


# Преобразуйте False в строку
str_false = str(False)
print("str_false: ", str_false, type(str_false))
