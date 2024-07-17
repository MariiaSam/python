class Human:

    def __init__(self, name, age = 0):
        self.name = name
        self.age = age
        self.is_adult = self.__check_adult()

        print(f'Привіт, мене звати {self.name}, мені {self.age} років. Чи я повнолітня {self.is_adult}')

    def say_hello(self):
            return(f'Всім привітики, я {self.name}')
    
    def __check_adult(self) -> bool:
         if self.age >= 18:
              print(f'мені {self.age} років, отже я повнолітня')
              return True
         return False

 
mariia = Human("Mariia")
mariia.say_hello()
print('1', mariia.say_hello() ) # 1 Всім привітики, я Mariia
print('2', f'вік: {mariia.age}, Дорослий {mariia.is_adult}') # 2 вік: 0, Дорослий False

jill = Human('Jill', 20)
print("3", jill.say_hello()) # 3 Всім привітики, я Jill
print('4', f"Вік: {jill.age}, Дорослий: {jill.is_adult}") # 4 Вік: 20, Дорослий: True

# ======================================================

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f"Point(x={self.x}, y={self.y})"

# point = Point(2, 3)
# print(repr(point))  # Виводить: Point(x=2, y=3)

# ======================================================

class Point:
    def __init__(self, x, y) -> None:
          self.x = x
          self.y = y
    
    def __repr__(self) -> str:
         return f'Point (x={self.x}, y={self.y})'
    
original_point = Point(3, 9)
print(repr(original_point)) # Point (x=3, y=9)

new_point = eval(repr(original_point))
print(new_point) # Point (x=3, y=9)

#===================================================

class SimpleDict:
    def __init__(self) -> None:
            self.__data = {}

    def __getitem__(self, key): # дозволяє отримати значення за ключем
        return self.__data.get(key, "Key not found")
    
    def __setitem__(self, key, value): #  встановити нове значення для ключа.
        self.__data[key] = value

# Використання класу
simple_dict = SimpleDict()
simple_dict['name'] = 'Boris'
print(simple_dict['name'])  
print(simple_dict['age'])  


'''
Boris
Key not found
'''

class BoundedList:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value
        self.__data = []

    def __getitem__(self, index: int):
        return self.__data[index]

    def __setitem__(self, index: int, value: int):
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(f"Value {value} must be between {self.min_value} and {self.max_value}")
        if index >= len(self.__data):
            # Додати новий елемент, якщо індекс виходить за межі
            self.__data.append(value)
        else:
            # Замінити існуючий елемент
            self.__data[index] = value

    def __repr__(self):
        return f"BoundedList({self.max_value}, {self.min_value})"

    def __str__(self):
        return str(self.__data)

if __name__ == '__main__':
    temperatures = BoundedList(18, 26)

    for i, el in enumerate([20, 22, 25, 27]):
        try:
            temperatures[i] = el
        except ValueError as e:
            print(e)

    print(temperatures)
