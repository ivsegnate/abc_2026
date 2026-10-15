class User:
    def __init__(self, email, password):
        if '@' not in email:
            raise ValueError(f"Invalid email: {email}")
        self._email = email
        self._password = hash(password)

    @property
    def password(self):
        raise AttributeError("password cannot be read")

    @property
    def email(self):
        return self._email  

    @email.setter
    def email(self, email):
        if '@' not in email:
            raise ValueError(f"Invalid email: {email}")
        self._email = email

    @password.setter
    def password(self, password):
        self._password = hash(password)

    def check_password(self, password):
        return hash(password) == self._password

user = User("test@example.com", "secret")
print(user.email)  # test@example.com
# print(user.password) # AttributeError
print(user.check_password("secret"))  # True
print(user.check_password("wrong"))   # False