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

class Circle:
    
    def __init__(self, radius):
        self.radius = radius
 

    def calc_area_radius(self):
       area_circle = 3.14 * self.radius * self.radius
       return area_circle
 
    def length_circle(self):
        length_circle = 2 * 3.14 * self.radius
        return length_circle

    
radius_input = float(input("Enter radius: "))

circle = Circle(radius_input)

area = circle.calc_area_radius()
print(f'Площа кола {area:.2f}')

length = circle.length_circle()
print(f'Довжина кола {length:.2f}')

'''
Площа кола 200.96
Довжина кола 50.24
'''