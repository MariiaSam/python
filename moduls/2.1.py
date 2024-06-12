# =============================         Умовне виконання коду

# if <умова>:
#     <тіло if-блоку>
# else:
#     <тіло else-блоку>

# else If

# Mariia = 34

# if Mariia > 33:
#     print ('Mariia вже за 33')
# else:
#     print('Mariia ще немає 33')

# Mariia вже за 33

# ================================


# x = int(input('Input number: '))

# if x % 2 == 0:
#     print("The number is even ")
# else:
#     print("The number is not even ")

# ================================

# a = input('Input number: ')
# a = int(a)
# if a > 0:
#     print('The number is positive')
# elif a < 0:
#     print('The number is negative')
# else:
#     print('This number is zero')


# ================================      Логічні вирази

# money = 0
# if money:
#     print(f"You have {money} on your bank account")
# else:
#         print(f"You have no money on your bank account")

# ===============================
# result = None
# if result:
#     print(result)
# else:
#     print("Result is None, do something")
# Result is None, do something


# ===============================
# user_name = input("Enter your name: ")

# if user_name:
#     print(f"Hello {user_name}")
# else:
#     print("Hi Anonym!")

# ===============================           Оператор is (вказуює на одну і ту ж область пам'яті)
# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]

# print(a is b)  # True
# print(a is c)  # False

# ===============================          Булева алгебра

# name = "Mariia"
# age = 34
# has_driver_licence = True

# if name and age >= 18 and has_driver_licence:
#     print(f"User {name} can rent a car")


# ======= not, and, or - оператори булвої алгебри

# num = int(input("Введіть число: "))

# length = len(str(num))

# if length == 2 and num % 2 == 0:
#     print("Парне двозначне число")
# else:
#     print("Ні")

# ==================

# a = False or False
# print(a)  # False


# ==============================    тернарні оператори
# is_nice = True
# state = "nice" if is_nice else "not nice"


# ==============================
# some_data = None
# msg = some_data or "Не було повернено даних"
# print(msg)  # Не було повернено даних

# some_data = None
# if some_data:
#     msg = some_data
# else:
#     msg = "Не було повернено даних"

# ==============================        Оператор match

# fruit = "apple"

# match fruit:
#     case "apple":
#         print("This is an apple.")
#     case "banana":
#         print("This is a banana.")
#     case "orange":
#         print("This is an orange.")
#     case _:
#         print("Unknown fruit.")

# This is an apple.

# ==============================
# point = (1, 0)

# match point:
#     case (0, 0):
#         print("Точка в центрі координат")
#     case (0, y):
#         print(f"Точка лежить на осі Y: y={y}")
#     case (x, 0):
#         print(f"Точка лежить на осі X: x={x}")
#     case (x, y):
#         print(f"Точка має координати:  x={x}, y={y}")
#     case _:
#         print("Це не точка")

# Точка лежить на осі X: x=1
# ==============================       Цикли
# fruit = 'apple'
# for i in fruit:
#     print(i)

# a
# p
# p
# l
# e

# ==============================
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for i in alphabet:
#     print(i, end=" ")  # a b c d e f g h i j k l m n o p q r s t u v w x y z
  # ==============================

# odd_numbers = [1, 3, 5, 7, 9]
# for i in odd_numbers:
#     print(int(i ** 0.6))

# 1
# 2
# 3
# 3

# ============================== Цикл WHILE


# k = 0
# while k < 10:
#     k = k + 1
#     print(k)
#===============================
# a = 0
# while True:
#     print(a)
#     if a >= 20:
#         break
#     a = a + 1

#===============================

# while True:
#     user_input = input()
#     print(user_input)
#     if user_input == "exit":
#         break

#===============================
# a = 0
# while a < 6:
#     a = a + 1
#     if not a % 2:
#         continue
#     print(a)

#=============================== Розширення можливостей циклу for range, enumerate та zip.


#=============================== Range
# for i in range(5): 
#     print(i) # послідовність чисел від 0 до 4
    # 0
    # 1
    # 2
    # 3
    # 4
#=============================== 

# for i in range(2, 12):
#     print(i) 
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9
    # 10
    # 11
#=============================== 
# for i in range(0, 10, 2):
#     print(i)
    # 0
    # 2
    # 4
    # 6
    # 8

#=============================== Enumerate
# some_list = ["apple", "banana", "cherry"]
# for i, value in enumerate(some_list):
#     print(i, value)
# 0 apple
# 1 banana
# 2 cherry

#=============================== Zip
# list1 = ["зелене", "стигла", "червоний"]
# list2 = ["яблуко", "вишня", "томат"]
# for number, letter in zip(list1, list2):
#     print(number, letter)

# зелене яблуко
# стигла вишня
# червоний томат

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c', 'd', 'e']

# for number, letter in zip(list1, list2):
#     print(number, letter)

# 1 a
# 2 b
# 3 c

#=============================== Цикли та словники

# numbers = {
#     1: "one",
#     2: "two",
#     3: "three"
# }


# for i in numbers:
#     print(i)

# 1
# 2
# 3

#=============================== 

# for i in numbers.keys():
#     print(i)
# 1
# 2
# 3

#=============================== 

# for i in numbers.values():
#     print(i)

# one
# two
# three

#=============================== 
# for i in numbers.items():
#     print(i)

# (1, 'one')
# (2, 'two')
# (3, 'three')

# for key, value in numbers.items():
#     print(key, value)
# 1 one
# 2 two
# 3 three


# ==================================
# val = 'a'
# try:
#     val = int(val)
# except ValueError:
#     print(f"val {val} is not a number")
# else:
#     print(val > 0)
# finally:
#     print("This will be printed anyway")

# ===========================================
# money = 0
# if money:
#     print(f"You have {money} on your bank account")
# else:
#     print("You have no money and no debts")

# You have no money and no debts
# ===========================================

# print(False and False) # False
 # ===========================================

# is_nice = True
# state = "nice" if is_nice else "not nice"
# print(state) # nice
 # ===========================================

# some_data = None
# msg = some_data or "Не було повернено даних"
# print(msg) # Не було повернено даних

 # ===========================================

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for char in alphabet:
#     print(char, end=" ") # a b c d e f g h i j k l m n o p q r s t u v w x y z

# a = 0
# while True:
#     print(a)
#     if a >= 20:
#         break
#     a = a + 1

def print_max(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально') 

print_max(3, 4)  # 4 максимально

x = 5
y = 7
print_max(x, y)  # передача змінних у якості аргументів

a = 10
ф = a
print(id(a))
print(id(ф))
ф = 9
print(id(ф))

