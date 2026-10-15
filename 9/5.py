class Product:
    def __init__(self, name, price = 0):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            self._price = 0
        else:
            self._price = value


class Order:
    def __init__(self):
        self._products = []

    @property
    def products(self):
        return list(self._products)

    @property
    def total_price(self):
        return sum(product.price for product in self._products)

    def add_product(self, product):
        self._products.append(product)

    def remove_product(self, product):
        if product in self._products:
            self._products.remove(product)


book = Product("Book", 10)
pen = Product("Pen", 2)
order = Order()
order.add_product(book)
order.add_product(pen)
print(f"{order.total_price}")  # 12