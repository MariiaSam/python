# ТИПИ ДАНИХ


# Числові типи
# Логічний тип (Boolean).
# Текстовий тип або рядки.
# Тип None

#=================================================== ЧИСЛА


int = 1 # ціле число
float = 3.14 # Дійсні числа 
 

complex_number = 3.3 + 2j # Комплексні числа 
print(complex_number)

#=================================================== Логічний тип


is_active = True
is_delete = False

#===================================================  Рядки
# str = "Mariia" # Рядки

s1 = "Hello"
s2 = "world!"
joined_string = s1 + " " + s2
print(joined_string) # Hello world!

name = "Oleg"
hello_string = f"Hello, {name}!"

print(hello_string) #Hello, Oleg!


#===================================================  Тип None
connect_to_database = None


#===================================================  Колекції

#  типи колекцій:
# Списки (Lists)
# Кортежі (Tuples)
# Словники (Dictionaries)
# Множини (Sets)
# Заморожені множини (Frozen Sets)


#=================================================== Списки   Lists(), list=[]
# my_list = list()
# empty_list = []
# my_list = [1, 2, 3, 4, 5]
# my_list = [1, "Hello", 3.14]

#====================================      append ДОДАТИ

# my_list.append(4)

#====================================      remove ВИДАЛИТИ

# my_list.remove("Hello")

# some_iterable = ["a", "b", "c"]
# print(some_iterable) # ["a", "b", "c"]

# first_letter = some_iterable[0]
# print(first_letter) # a

# middle_one = some_iterable[1]
# print(middle_one) # b

# last_letter = some_iterable[2]
# print(last_letter) # c


#====================================      pop 

# chars = ['a', 'b', 'c']
# last = chars.pop(1)

# print(last) # b
# print(chars) # ['a', 'c']

#===========================                 pop

# chars = ['a', 'b', 'c']
# numbers = [1, 2]
#===========================                 extend

# chars.extend(numbers)
# print(chars) # ['a', 'b', 'c', 1, 2]

#===========================                 insert
# chars = ['a', 'b', 'c']
# chars.insert(1, "d")

# print(chars) # ['a', 'd', 'b', 'c']

#===========================                  clear
# chars.clear() # []

#===========================                   index
# chars = ['a', 'b', 'c', 'd']
# c_ind = chars.index('c')

# print(c_ind) # 2

#===========================                    count()

# my_list = [1, 2, 3, 4, 2, 2, 5, 2]
# count_2 = my_list.count(3)
# print(count_2)  # Виведе 1, оскільки число 3 зустрічається 1 раз

#===========================                     length

# my_list = [1, 2, 3, 4, 5]                      
# print(len(my_list)) # 5

# #===========================                     sort
# nums = [3, 1, 4, 1, 5, 9, 2]
# nums.sort()
# print(nums)  #  [1, 1, 2, 3, 4, 5, 9]


# nums.sort(reverse=True)
# print(nums)  #  [9, 5, 4, 3, 2, 1, 1]


# words = ["banana", "apple", "cherry"]
# words.sort(key=len)
# print(words)  # ['apple', 'banana', 'cherry']


# =========================                     sorted

# nums = [3, 1, 4, 1, 5, 9, 2]
# sorted_nums = sorted(nums)
# print(sorted_nums)  #  [1, 1, 2, 3, 4, 5, 9]

# sorted_nums_desc = sorted(nums, reverse=True)
# print(sorted_nums_desc)  # [9, 5, 4, 3, 2, 1, 1]

# words = ["banana", "apple", "cherry"]
# sorted_words = sorted(words, key=len)
# print(sorted_words)  #  ['apple', 'banana', 'cherry']

# #==========================                     copy

# chars =  ['a', 'b']
# chars_copy = chars.copy()

# ========================                  reverse()

chars = ["banana", "apple", "cherry"]
chars.reverse()

print(chars) # ['cherry', 'apple', 'banana']

# ========================            Словники      dict = {}


my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict["name"])  #  'Alice'

my_dict["age"] = 26 
print(my_dict) # {'name': 'Alice', 'age': 26, 'city': 'New York'}

my_dict['email'] = 'qwerty@wwe.qww'
print(my_dict) #  {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'qwerty@wwe.qww'}

del my_dict['email']
print(my_dict) # {'name': 'Alice', 'age': 26, 'city': 'New York'}

print("name" in my_dict) # True

# ========================  Методи словників
# pop
# update()
# clear()
# copy()
# get() 

my_dict = {"name": "Alice", "age": 25}
age = my_dict.get("age")  #  25
gender = my_dict.get("gender")  #  None, оскільки "gender" немає в словнику



# ========================  Множини


empty_set = set() # щоб створити
a = set('hello')
b = {1, 2, 3, 4, 5}


# numbers = {1, 2, 3, 1, 2, 3, 7}
# print(numbers)
# print(numbers) # {1, 2, 3}

# set_numbers = set(numbers)
# print(set_numbers) # {1, 2, 3}


# numbers = {1, 2, 3}
# numbers.add(4)
# print(numbers)  # {1, 2, 3, 4}

# numbers = {1, 2, 3}
# numbers.remove(3)
# print(numbers)  # {1, 2}

numbers = {1, 2, 3}
numbers.discard(3)
print(numbers)  # {1, 2}


#===========================        Кортежі

my_tuple = tuple() # або
my_tuple = ()

my_tuple = (1, 2, 3)

#n========================
"123".isdigit()  # True
"hello".isalpha()  # True
" ".isspace()  # True


#n======================== Slice

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = numbers[0:1:1]
print(odd_numbers)

odd_numbers = numbers[0:10:2]
print(odd_numbers)#[1, 3, 5, 7, 9]

print(numbers)

print(odd_numbers)#[1, 3, 5, 7, 9]




# message = "Hello world!"

# print(message[0])
#===========================

# name = "Oleg"
# hello_string = f"Hello, {name}!"
# print(hello_string)
#===========================

# side_a = 10
# side_b = 5

# hypotenuse = (side_a**2 + side_b**2)**0.5
# print(hypotenuse) # 11.180339887498949

# S = side_a * side_b / 2
# print(S) #25.0

#===========================
# n = 5000

# hours = n // (60 * 60)
# minutes = (n - hours * 60 * 60) // 60
# seconds = n - hours * 60 * 60 - minutes * 60

# print(hours) # 1
# print(minutes) # 23
# print(seconds) # 20


#+==========================

# x = 12
# print(f"Значення x: {x}") # Значення x: 12

# a = input("Рядок запрошення: ")

# age = input("How old are you? ")
# age = int(age)

# pi = float('3.14')

#==========================================
# a = float(input("Введіть сторону квадрата a: "))
# P = 4 * a
# print(f"Периметр квадрата дорівнює {P}")


#==========================================

# Встановлюємо ціни на продукти
# price_per_croissant = 1.04
# price_per_glass = 0.34
# price_per_coffee_pack = 4.42

# Кількість кожного продукту
# num_croissants = int(input("Введіть кількість круасанів: "))
# num_glasses = int(input("Введіть кількість склянок: "))
# num_coffee_packs = int(input("Введіть кількість упаковок кави: "))

# Обчислення загальної вартості
# total_cost = num_croissants * price_per_croissant + num_glasses * price_per_glass + num_coffee_packs * price_per_coffee_pack

# Визначаємо кількість повних доларів і центів
# total_dollars = int(total_cost)
# total_cents = int(total_cost * 100)

# Вивід результату
# print(f"Загальна вартість у повних доларах: {total_dollars} доларів")
# print(f"Загальна вартість у центах: {total_cents} центів")

#==========================================

# names = ['Anna', "Mariia", "Oleg"]
# names.append("Igor")
# print(names)

# first_name = names[0]
# print(first_name)

# names[0] = "Lev"
# print(names)