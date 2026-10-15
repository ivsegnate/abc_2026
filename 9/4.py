class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            self._price = 0
        else:
            self._price = value      


product = Product('Book', 10)
print(product.price)  # 10
product.price = -5
print(product.price)  # 0