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

    def save(self, file_obj):
        with open(file_obj, 'wt') as my_file:
            for key, value in self.products.items():
                line = key + ',' + str(value)+'\n'
                my_file.write(line)

    def save2(self, file_obj):
        for product, count in self.products.items():
            file_obj.write(product+','+str(count)+'\n')

    def save3(self, file_obj):
        lines=[prod+','+str(count)+'\n' for prod, count in self.products.items()]
        file_obj.writelines(lines)


    @staticmethod
    def load(file_obj):
        data={}
        for line in file_obj:
            record=line.rstrip('\r\n').split(',')
            data[record[0]]=int(record[1])
        return Stock(data)


    @staticmethod
    def foo(a):
        print('Static method called!',a)


stock = Stock({'chair':5, 'table':2})
stock.resupply('curtains', 4)
stock.withdraw('chair' ,1)
print(stock.products)

products = {'oragne' :2, 'lemon':3}

stock.save('stock.csv')

with open('magazyn.csv', 'wt') as data_file:
    stock.save2(data_file)

with open('magazyn2.csv', 'wt') as data_file:
    stock.save3(data_file)

with open('magazyn.csv', 'rt') as data_file:
    stock2=Stock.load(data_file)
    print(stock2.available_items())