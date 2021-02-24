class Catalogue:
    products = []
    def __init__(self, name):
        self.name = name

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, letter):
        self.letter = letter
        return [s for s in self.products if s[0] == self.letter]

    def __repr__(self):
        self.products = '\n'.join(sorted(self.products))
        return f'Items in the {self.name} catalogue:\n{self.products}'

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)