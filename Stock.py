import copy


class Stock:

    def __init__(self, products):
        self.products = copy.deepcopy(products)

    def resupply(self,product,count):
        if count <= 0:
            raise ValueError('Can resupply only tih positive count')
        #if product in self.products:
        #    self.products[product] += count
        #else:
        #    self.products[product] = count
        self.products[product] = self.products.get(product,0) +count

    def withdraw(self, product, count):
        if count <= 0:
            raise ValueError('Can withdraw only positive count.')
        if product not in self.products:
            raise ValueError('Unknown product' + product)
        if self.products[product]<count:
            raise ValueError('Insufficient number of items in stock.')
        self.products[product] -= count

    def available_items(self):
        items = {}
        for product, count in self.products.items():
            if count > 0:
                items[product] = count
        return items


stock = Stock({'chair':5, 'table':2})
stock.resupply('curtains', 4)
stock.withdraw('chair' ,1)
print(stock.products)

products = {'oragne' :2, 'lemon':3}
stock = Stock(products)
print(stock.products)
products['orange']=-500
print(stock.products)