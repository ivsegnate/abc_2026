# Инкапсуляция и property
# todo: Класс "Пользователь" (Валидация email)
# Создайте класс User. У него должны быть свойства email и password.
# При установке email проверяйте, что строка содержит символ @ (простая валидация).
# При установке пароля, храните не сам пароль, а его хеш (для простоты можно использовать hash()).
# Сделайте метод check_password(password), который проверяет, соответствует ли хеш переданного
# пароля сохраненному хешу.

class User:
    def __init__(self, email, password):
        if '@' not in email:
            raise ValueError(f"Invalid email: {email}")
        self.email = email
        self.password = password

    @property
    def password(self):
        raise AttributeError("password cannot be read")

    @password.setter
    def password(self, in_password):
        self._password_hash = hash(in_password)

    def check_password(self, in_password):
        return hash(in_password) == self._password_hash

user = User("test@example.com", "secret")
print(user.email)  # test@example.com
# print(user.password) # AttributeError
print(user.check_password("secret"))  # True
print(user.check_password("wrong"))   # False