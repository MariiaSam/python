# 1
'''
Напишіть клас з назвою Circle для обчислення площі круга за введеним радіусом. Клас Circle має містити метод, який обчислює площу круга.

Вхідні дані:

3
Вихідні дані:

28.26
'''

# class Circle:
'''
      Клас для обчислення площі круга.
    '''
    # def __init__(self, radius):
    #     self.radius = radius
'''
    _init__ Ініціалізує об'єкт Circle. Цей метод приймає один аргумент, radius, який є радіусом круга. Він зберігає це значення в атрибуті self.radius
    '''

    # def calc_area(self):
    #    area_circle = 3.14 * self.radius * self.radius
    #    return area_circle
'''
    
    Обчислює площу круга.

    Returns:
      Площа круга
    '''
    
 # Введення радіуса
# radius_input = float(input("Enter radius: "))

# Створення об'єкта Circle
# circle = Circle(radius_input)

# Обчислення та виведення площі
# area = circle.calc_area()
# print(f'{area:.2f}')

# 28.26

#=============================================
# 2 

'''
Напишіть клас під назвою Rectangle для визначення площі прямокутника за введеними довжиною та шириною сторін. Клас прямокутника має містити метод, який обчислює площу прямокутника.

Вхідні дані:

2
3
Вихідні дані:

6

'''

# class Rectangle:

#     def __init__(self, height, width) -> None:
#         self.height = height
#         self.width = width

#     def calc_area_rect(self):
#         area_rect = self.height * self.width
#         return area_rect
    
# height_rect = int(input("Enter height: "))
# width_rect = int(input("Enter width: "))


# rectangle = Rectangle(height_rect, width_rect)

# area_rect = rectangle.calc_area_rect()
# print(area_rect)

#=============================================

# 3
'''
Напишіть клас з назвою Circle, який містить два методи: для обчислення площі круга та довжину кола за введеним радіусом.

Вхідні дані:

8
Площа круга – S = πr2, де π = 3,14, r – радіус круга.
довжина кола за введеним радіусом = 2 * π * радіус

Вихідні дані:

200.96
50.24
'''

# class Circle:
    
#     def __init__(self, radius):
#         self.radius = radius
 

#     def calc_area_radius(self):
#        area_circle = 3.14 * self.radius * self.radius
#        return area_circle
 
#     def length_circle(self):
#         length_circle = 2 * 3.14 * self.radius
#         return length_circle

    
# radius_input = float(input("Enter radius: "))

# circle = Circle(radius_input)

# area = circle.calc_area_radius()
# print(f'Площа кола {area:.2f}')

# length = circle.length_circle()
# print(f'Довжина кола {length:.2f}')

'''
Площа кола 200.96
Довжина кола 50.24
'''
#=============================================

# 4

'''
Напишіть клас, який має як мінімум два методи: перший - отримати рядок з вводу консолі, другий - друкувати рядок у верхньому регістрі.

Вхідні дані:

python
Вихідні дані:

PYTHON
'''

# class Get:

#     def __init__(self, string):
#         self.string = string

#     def get_str(self):
#         input_get_str = input(self.string)
#         return input_get_str


#     def print_str_upper(self, stringUpper):
#         print(stringUpper.upper())

# get_string_object = Get("Enter string: ")

# get_str_obj = get_string_object.get_str()

# get_string_object.print_str_upper(get_str_obj)

# PYTHON


#=============================================

# 5

'''

Змоделюйте роботу онлайн-магазину.

Напишіть клас з ім’ям Shop(). Метод __init__() класу Shop() повинен містити два атрибути: shop_name і store_type. Створіть метод describe_shop(), який виводить два атрибути, і метод open_shop(), який виводить повідомлення про те, що онлайн-магазин відкритий. Створіть на основі класу екземпляр з ім’ям store. Виведіть два атрибути окремо, потім викличте обидва методи.

Створіть ще один екземпляр класу, викличте для нього метод describe_shop().

Додайте атрибут number_of_units зі значенням за замовчуванням 0; він представляє кількість видів товару у магазині. Виведіть значення number_of_units, а потім змініть number_of_units і виведіть знову для store.

Додайте метод з ім’ям set_number_of_units(), що дозволяє задати кількість видів товару. Викличте метод з новим числом, знову виведіть значення. Додайте метод з ім’ям increment_number_of_units(), який збільшує кількість видів товару на задану величину. Викличте цей метод для store.

Напишіть клас Discount(), що успадковує від класу Shop(). Додайте атрибут з ім’ям discount_products для зберігання списку товарів, на які встановлена знижка. Напишіть метод get_discounts_ptoducts, який виводить цей список. Створіть екземпляр store_discount і викличте цей метод.

Додатково. Збережіть код класу Shop() у модулі. Створіть окремий файл, що імпортує клас Shop(). Створіть екземпляр all_store і викличте один з методів Shop(), щоб перевірити, що команда import працює вірно.

У вихідних даних наведений можливий варіант результатів виконання завдань.

Вхідні дані:

Немає
Вихідні дані:

a)
Rozetka
ishop
Rozetka
ishop
3000000
The store is open.
b)
ITbox
ishop
20000
c)
3000000
3000001
d)
Rozetka
ishop
3900000
Rozetka
ishop
3901200
e)
motherboards
solid state drives
monitors

'''

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

class Discount(Shop):

    def __init__(self, shop_name, store_type, new_number_of_unit=0, discount_products=[]):
        super().__init__(shop_name, store_type, new_number_of_unit)       
        self.discount_products = discount_products

    def get_discounts_ptoducts(self):
        print(f'{self.discount_products}')

    
    def get_discount_products(self):
        if not self.discount_products:
            print(f"There are currently no discount products in {self.shop_name}.")
        else:
            print(f"Discount Products in {self.shop_name}:")
            for product in self.discount_products:
                print(f"- {product}")

first_store = Shop("Rozetka", "ishop")
second_store = Shop('ITbox', 'electronics', 5000)


first_store.describe_shop()

first_store.open_shop()

second_store.describe_shop()

first_store.set_number_of_units(10000)
print(f'quantity of goods in {first_store.shop_name}: {first_store.number_of_units}')

first_store.increment_number_of_units(20000)
print(f'Update quantity of goods in {first_store.shop_name}: {first_store.number_of_units}')


discount_store = Discount("Technogrand", "electronics", 3000, ["Laptops", "Smartphones"])

discount_store.describe_shop()
discount_store.open_shop()
discount_store.get_discount_products()