# ТИПИ ДАНИХ

str = "Mariia" # строка

#  типи колекцій:
# Списки (Lists)
# Кортежі (Tuples)
# Словники (Dictionaries)
# Множини (Sets)
# Заморожені множини (Frozen Sets)


#=================================================== Списки (Lists)
# my_list = list()
# empty_list = []
# my_list = [1, 2, 3, 4, 5]
# my_list = [1, "Hello", 3.14]
# my_list.append(4)
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

# ========================  

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
