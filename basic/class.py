class Dog:
    # Атрибут класу
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Атрибути екземпляру
        self.name = name
        self.age = age

# ===================================
# class Car:
#     vehicle_type = "Automobile"

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

        # ===================================


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

# ==============================================
# length = input(float("length: "))
# area_l = float(length)

# width = input("width: ")
# area_w = float(width)

# area = area_l * area_w

# print(area)

# is_next = None
# num = int(input("Enter the number of points: "))
# if num >= 83:
#     is_next = True
# else:
#     is_next = False


# num = int(input("Enter a number: "))

# if num > 0:
#     if num % 2 == 1:
#         result = "Positive odd number"
#     else:
#         result = "Positive even number"
# elif num < 0:
#     result = "Negative number"
# else:
#     result = "It is zero"


numbers = [10, 4, 201, 21, 12, 2, 132, 7, 1, 18, 3, 12, 6, 15, 4, 27]
sum_num = 0

for num in numbers:
    if num % 3 == 0:
        sum_num += num

print(sum_num)


num = int(input("Enter the integer (0 to 100): "))
sum = 0

while num > 0:
    sum += num
num -= 1


def greeting():
    print('Hello world!')

def invite_to_event(username):
    return f"Dear {username}, we have the honour to invite you to our event"

username1 = "Mariia"
username2 = "Stepan"

print(invite_to_event(username1))
print(invite_to_event(username2))
