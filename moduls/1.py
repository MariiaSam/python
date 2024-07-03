# ТИПИ ДАНИХ


# Числові типи
# Логічний тип (Boolean).
# Текстовий тип або рядки.
# Тип None

# =================================================== ЧИСЛА


# int = 1  # ціле число
# # float = 3.14  # Дійсні числа


# complex_number = 3.3 + 2j  # Комплексні числа
# print(complex_number)

# =================================================== Логічний тип


# is_active = True
# is_delete = False

# ===================================================  Рядки
# str = "Mariia" # Рядки

# s1 = "Hello"
# s2 = "world!"
# joined_string = s1 + " " + s2
# print(joined_string)  # Hello world!

# name = "Oleg"
# hello_string = f"Hello, {name}!"

# print(hello_string)  # Hello, Oleg!


# ===================================================  Тип None
# connect_to_database = None


# ===================================================  Колекції

#  типи колекцій:
# Списки (Lists)
# Кортежі (Tuples)
# Словники (Dictionaries)
# Множини (Sets)
# Заморожені множини (Frozen Sets)


# =================================================== Списки   Lists(), list=[]
# my_list = list()
# empty_list = []
# my_list = [1, 2, 3, 4, 5]
# my_list = [1, "Hello", 3.14]

# ====================================      append ДОДАТИ

# my_list.append(4)

# ====================================      remove ВИДАЛИТИ

# my_list.remove("Hello")

# some_iterable = ["a", "b", "c"]
# print(some_iterable) # ["a", "b", "c"]

# first_letter = some_iterable[0]
# print(first_letter) # a

# middle_one = some_iterable[1]
# print(middle_one) # b

# last_letter = some_iterable[2]
# print(last_letter) # c


# ====================================      pop

# chars = ['a', 'b', 'c']
# last = chars.pop(1)

# print(last) # b
# print(chars) # ['a', 'c']

# ===========================                 pop

# chars = ['a', 'b', 'c']
# numbers = [1, 2]
# ===========================                 extend

# chars.extend(numbers)
# print(chars) # ['a', 'b', 'c', 1, 2]

# ===========================                 insert
# chars = ['a', 'b', 'c']
# chars.insert(1, "d")

# print(chars) # ['a', 'd', 'b', 'c']

# ===========================                  clear
# chars.clear() # []

# ===========================                   index
# chars = ['a', 'b', 'c', 'd']
# c_ind = chars.index('c')

# print(c_ind) # 2

# ===========================                    count()

# my_list = [1, 2, 3, 4, 2, 2, 5, 2]
# count_2 = my_list.count(3)
# print(count_2)  # Виведе 1, оскільки число 3 зустрічається 1 раз

# ===========================                     length

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

# chars = ["banana", "apple", "cherry"]
# chars.reverse()

# print(chars)  # ['cherry', 'apple', 'banana']

# ========================            Словники      dict = {}


# my_dict = {"name": "Alice", "age": 25, "city": "New York"}
# print(my_dict["name"])  # 'Alice'

# my_dict["age"] = 26
# print(my_dict)  # {'name': 'Alice', 'age': 26, 'city': 'New York'}

# my_dict['email'] = 'qwerty@wwe.qww'
# # {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'qwerty@wwe.qww'}
# print(my_dict)

# del my_dict['email']
# print(my_dict)  # {'name': 'Alice', 'age': 26, 'city': 'New York'}

# print("name" in my_dict)  # True

# ========================  Методи словників
# pop
# update()
# clear()
# copy()
# get()

# my_dict = {"name": "Alice", "age": 25}
# age = my_dict.get("age")  # 25
# gender = my_dict.get("gender")  # None, оскільки "gender" немає в словнику


# ========================  Множини


# empty_set = set()  # щоб створити
# a = set('hello')
# b = {1, 2, 3, 4, 5}


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

# numbers = {1, 2, 3}
# numbers.discard(3)
# print(numbers)  # {1, 2}


# # ===========================        Кортежі

# my_tuple = tuple()  # або
# my_tuple = ()

# my_tuple = (1, 2, 3)

# n========================
# "123".isdigit()  # True
# "hello".isalpha()  # True
# " ".isspace()  # True


# n======================== Slice

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_numbers = numbers[0:1:1]
# print(odd_numbers)

# odd_numbers = numbers[0:10:2]
# print(odd_numbers)  # [1, 3, 5, 7, 9]

# print(numbers)

# print(odd_numbers)  # [1, 3, 5, 7, 9]


# message = "Hello world!"

# print(message[0])
# ===========================

# name = "Oleg"
# hello_string = f"Hello, {name}!"
# print(hello_string)
# ===========================

# side_a = 10
# side_b = 5

# hypotenuse = (side_a**2 + side_b**2)**0.5
# print(hypotenuse) # 11.180339887498949

# S = side_a * side_b / 2
# print(S) #25.0

# ===========================
# n = 5000

# hours = n // (60 * 60)
# minutes = (n - hours * 60 * 60) // 60
# seconds = n - hours * 60 * 60 - minutes * 60

# print(hours) # 1
# print(minutes) # 23
# print(seconds) # 20


# +==========================

# x = 12
# print(f"Значення x: {x}") # Значення x: 12

# a = input("Рядок запрошення: ")

# age = input("How old are you? ")
# age = int(age)

# pi = float('3.14')

# ==========================================
# a = float(input("Введіть сторону квадрата a: "))
# P = 4 * a
# print(f"Периметр квадрата дорівнює {P}")


# ==========================================

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

# ==========================================

# names = ['Anna', "Mariia", "Oleg"]
# names.append("Igor")
# print(names)

# first_name = names[0]
# print(first_name)

# names[0] = "Lev"
# print(names)

# name = input("enter your name: ")
# print(name)

# ==========================================
# apple_quantity = float(input('Введіть кількість: '))
# apple_price = float(input('Введіть ціну: '))

# pear_quantity = float(input('Введіть кількість: '))
# pear_price = float(input('Введіть ціну: '))

# buy = f"Для приготування пирога потрібно придбати яблука {apple_quantity} кг за ціною {apple_price} та груші {pear_quantity} кг за ціною {pear_price} грн. Загальна вартість складу {(apple_quantity * apple_price ) + (pear_quantity * pear_price)}"
# print(buy)

# apple_quantity = float(input('Введіть кількість яблук (кг): '))
# apple_price = float(input('Введіть ціну яблук (грн за кг): '))

# pear_quantity = float(input('Введіть кількість груш (кг): '))
# pear_price = float(input('Введіть ціну груш (грн за кг): '))

# buy = f"Для приготування пирога потрібно придбати яблука {apple_quantity} кг за ціною {apple_price} грн та груші {pear_quantity} кг за ціною {pear_price} грн. Загальна вартість складає {(apple_quantity * apple_price) + (pear_quantity * pear_price)} грн."
# print(buy)


# ==========================================
# a = list[1, 2, 3, 5]
# print(a)
# print(type(a))

# ==========================================
# pi_str = str(3.14)
# print(pi_str)
# print(type(pi_str)) # <class 'str'>

# age_str = str(29)
# print(age_str)

# ==========================================

# my_dict = {"name": "Alice", "age": 25}
# age = my_dict.pop("age")
# print(my_dict) # {'name': 'Alice'}
# print(age) # 25

# ==========================================
# print( 10 // 2) # 5
# print( 10 // 2.0) # 5.0

# ==========================================

# print(0 > 10 and 5 > 2)

# str_1 = '2'
# str_2 = '0'
# print(str_1 + str_2) # 20

# str_3 = '6'
# str_4 = '6'
# print(str_3 + str_4) # 66

# ==========================================

# num = 8941 % 931

# if num % 2 == 0:

#   print("The number num is", 'Even') # The number num is Even

# else:

#   print("The number num is", 'Odd')

'''
len(t) - returns the length of list t, or in other words, the number of items it contains;
list1 + list2 - combines two lists (both must be lists);
t * n - creates n duplicates of list t;
t.append(x) - adds a single item x to the end of list t (this alters the original list);
t.extend([x, y, ...]) - appends elements x, y, ... to the end of list t (this also modifies the original list);
t.copy() - produces a duplicate of the list t;
t.count(x) - tallies the number of occurrences of x in list t.
'''


# # Two-dimensional list
# countries_2d = [['USA', 9629091], ['Canada', 9984670], ['Germany', 357114]]

# # Pull elements
# print(countries_2d[1]) # ['Canada', 9984670]

# print(countries_2d[1][0]) # Canada

#============================================

# # Two-dimensional tuple
# two_d_countries = (('USA', 9629091, 331002651), ('Canada', 9984670, 37742154), 
#                    ('Germany', 357114, 83783942), ('Brazil', 8515767, 212559417), 
#                    ('India', 3166391, 1380004385))

# # Get information about India
# print(two_d_countries[4]) # ('India', 3166391, 1380004385)

# # Get the area of India
# print(two_d_countries[4][1]) # 3166391

#============================================

# Dictionary 
# countries_dict = {'USA': (9629091, 331002651), 'Canada': (9984670, 37742154), 
#             'Germany': (357114, 83783942)}

# # Information about Canada
# print(countries_dict["Canada"])

# (9984670, 37742154)

# ==========================================
'''

len(d) - returns the number of key:value pairs in the dictionary d;
d.copy() - creates a copy of the dictionary d;
d.items() - provides all the key, value pairs from the dictionary d;
d.keys() - lists all the keys in the dictionary d;
d.values() - provides all the values from the dictionary d.
Wondering how to add new entries to a dictionary? Dictionaries don't utilize list methods like .append() or .extend(), and they don't support concatenation like strings. Instead, since dictionaries organize data in key-value pairs, you simply assign values using keys:

d[k] = e - assigns the value e to the key k. If the key k already exists in the dictionary, its associated value will be updated.


'''
# Create variable
# i = 1

# # Initialize a while loop
# while i < 9:
#   # Print number i squared
#   print(i**i)
#   # Increment variable i by 1
#   i += 1

'''
1
4
27
256
3125
46656
823543
16777216
'''

# Create variable
# i = 1

# while i < 10:
#   print(i**2)
#   i = i + 1

# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# ==========================================


values = [1, [2, 3], 4, "code"]

for el in values:
  print(el, end = ' ') # 1 [2, 3] 4 code 
  # ==========================================

  # Initial list
values = [1, [2, 3], 4, "code"]

# Initialize a for loop over indexes
for i in range(len(values)):
  print("Index:", i)
  print("Value:", values[i])
  print("----") 

''''

Index: 0
Value: 1
----
Index: 1
Value: [2, 3]
----
Index: 2
Value: 4
----
Index: 3
Value: code
----
'''  
  # ==========================================

# Countries data
# countries = [['USA', 9629091, 331002651], ['Canada', 9984670, 37742154], 
# ['Germany', 357114, 83783942], ['Brazil', 8515767, 212559417], ['India', 3166391, 1380004385]]


# for country in countries: 
 
#     print(country, end = ' ')
#     print('\n') # Print new line after nested loop finish

'''  
['USA', 9629091, 331002651] 

['Canada', 9984670, 37742154] 

['Germany', 357114, 83783942] 

['Brazil', 8515767, 212559417] 

['India', 3166391, 1380004385] '''


# for country in countries: 
#   for j in country:
#     print(j, end = ' ')
#     print('\n') 

'''  

USA 9629091 331002651 

Canada 9984670 37742154 

Germany 357114 83783942 

Brazil 8515767 212559417 

India 3166391 1380004385
'''