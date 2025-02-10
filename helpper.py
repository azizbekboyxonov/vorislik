class Laptops:
    def __init__(self, brand, data):
        self.brand = brand
        self.data = data

class Hp(Laptops):
    def hp_laptop(self):
        print(f"brand: {self.brand} data: {self.data}")

class Asus(Laptops):
    def asus(self):
        print(f"brand: {self.brand} data: {self.data}")

class User(Hp, Asus):
    pass
