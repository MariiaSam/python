from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, broken_phones: int, quantity=0):
        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones

    def info(self):
        return f"Phone( name:{self.get_name()}, price:{self.price}, " \
               f"quantity:{self.quantity}, broken_phones: {self.broken_phones} )"
