
class Shop:

    def __init__(self, shop_name, store_type, number_of_units = 0) -> None:
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units
    
    def describe_shop(self):
        print(f'Store name is {self.shop_name}')
        print(f'Store type is {self.store_type}')
        print(f'quantity of goods {self.number_of_units}')


    def open_shop(self):
        print(f'Store {self.shop_name} is open')

    
    def set_number_of_units(self, new_number_of_units):
        self.new_number_of_units = new_number_of_units
        print(f'Update quantity of goods in {self.shop_name} increment {self.new_number_of_units}')

    
    def increment_number_of_units(self, increment_value):
        self.new_number_of_units += increment_value
        print(f'quantity of goods in {self.shop_name} increment by {increment_value} to {self.increment_number_of_units}')