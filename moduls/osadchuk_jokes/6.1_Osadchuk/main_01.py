class Item:
    def calculate_total_price(self, price, quantity):
        return price * quantity

item = Item()
item.name = 'Test name'
item.price = 1000
item.quantity = 90

# print(item.name)
print(item.__dict__)

print(item.calculate_total_price(item.price, item.quantity))

item2 = Item()
# item2.name = 'Test name2'
item2.price = 500
item2.quantity = 45

# print(item2.name)
#
# print(item2.calculate_total_price(item2.price, item.quantity))

print(item2.__dict__)