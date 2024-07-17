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

    