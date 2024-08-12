from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'
class Shop:
    def __init__(self):
        self._file_name = 'products.txt'
    def get_products(self):
        file = open(self._file_name, 'r')
        return file.read()
        file.close()
    def add(self, *products):
        self.products = [*products]
        for x in self.products:
            list_product = self.get_products()
            if list_product.find(str(getattr(x, 'name'))) == -1:
                file_product = open(self._file_name, 'a')
                file_product.write(f'{x}\n')
                file_product.close()
            else:
                print(f'Продукт {getattr(x, 'name')} уже есть в магазине')





s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
