class Item:
    pay_rate = 0.8 # Сума після знижки в 20%
    all_class_instance = list()
    class_instances = dict()

    def __init__(self, name: str, price: float, quantity=0):

        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all_class_instance.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def info(self):
        return f"Item( name:{self.name}, price:{self.price}, quantity:{self.quantity} )"
    @classmethod
    def all_items_info(cls):
        return [item.info() for item in cls.all_class_instance]

    @classmethod
    def load_data_from_csv(cls):
        with open('items.csv', 'r') as file:
            next(file)
            for line in file:
                name, price, quantity = line.strip().split(',')
                # cls(
                Item(
                    name=name.strip('"'),
                    price=float(price),
                    quantity=int(quantity)
                    )
                # item = Item(
                #     name=name.strip('"'),
                #     price=float(price),
                #     quantity=int(quantity)
                #     )
                # Item.class_instances[name.strip('"')] = item

# item1 = Item('Phone', 100, 1)
# item2 = Item("Laptop", 1000, 5)
#
# print(item1.info())
# print(item2.info())
#
# print(Item.all_class_instance)
# print(Item.all_items_info())
item = Item("Keyboard", 150, 7)
item.load_data_from_csv()
print(item.info())
print(Item.all_items_info())

# print(Item.class_instances)
# print(Item.class_instances['Mouse'].price)