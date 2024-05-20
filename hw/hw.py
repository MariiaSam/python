# length = 2.75
# width = 1.75
# area = length * width
# show = f"With width {width} and length {length} of the room, its area is equal to {area}"

# print(show)
#====================================

# length = input(float(10))
# width = input(float(10))
# area = length * width
# print(area)

# my_list = []
# my_list[0] = 2024
# my_list[1] = 'Python'
# my_list[2] = 3.12

# print(my_list)

#===================================
fruits = ['apple', 'cherry']

cars = ['Volvo']

fruits.extend(cars)

print(fruits) # ['apple', 'cherry', 'Volvo']


fruits.insert(1, 'Volvo')

print(fruits) # ['apple', 'Volvo', 'cherry', 'Volvo']

fruits.reverse()
print(fruits) # ['Volvo', 'cherry', 'Volvo', 'apple']

#===================================
cat = {"nick": "Simon", "age": 7, "characteristics": ["лагідний", "кусається"] }
info = {"status": "vaccinated", "breed": True}
age = cat.get('age')
cat.update(info)

print(cat)