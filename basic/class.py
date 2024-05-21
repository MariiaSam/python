class Dog:
    # Атрибут класу
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Атрибути екземпляру
        self.name = name
        self.age = age

#===================================
# class Car:
#     vehicle_type = "Automobile"

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
        
        #===================================

class Car:
    vehicle_type = "Automobile"

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}, Type: {Car.vehicle_type}"


car_ford = Car("Ford", "Mustang", 2022)
car_toyota = Car("Toyota", "Corolla", 2021)

print(car_ford.get_info())
print(car_toyota.get_info())

#==============================================
length = input(float("length: "))
area_l = float(length)

width = input("width: ")
area_w = float(width)

area = area_l * area_w

print(area)

is_next = None
num = int(input("Enter the number of points: "))
if num >= 83:
    is_next = True
else:
    is_next = False
    