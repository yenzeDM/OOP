class Cart():
    goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        del self.goods[indx]

    def get_list(self):
        tmp = []
        for product in self.goods:
            tmp.append(f"{product.name}: {product.price}")
        return tmp


class Table():

    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV():

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook():

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup():

    def __init__(self, name, price):
        self.name = name
        self.price = price

tv1 = TV('LG', 11000)
tv2 = TV('SAMSUNG', 15000)
table = Table('Brown table', 5000)
note1 = Notebook('Asus', 55000)
note2 = Notebook('Samsung', 45000)
cup = Cup('Cup', 500)

products = [tv1, tv2, table, note1, note2, cup]

cart = Cart()

for product in products:
    cart.add(product)