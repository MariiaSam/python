
def print_text():
    print('Hello')

print_text()

class Product:
    def __init__(self, value_one, value_two):
        self.value_one = value_one
        self.value_two = value_two

    def __call__(self):
        return self.value_one * self.value_two

product = Product(6, 6)

print(product())

#===========================================

class FileWriter:
    def __init__(self, filename):
        self.file = None
        self.opened = None
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        self.opened = True
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.opened:
            self.file.close()
        if exc_val is not None:
            print('Oh No!!!')


with FileWriter('new_file.txt') as file:
    file.write('Hello \n Bye')

    ''''
    Створення власних менеджерів контексту
    '''