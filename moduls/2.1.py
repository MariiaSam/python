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

#==================

a = False or False 
print(a) # False


# ==============================    тернарні оператори
is_nice = True
state = "nice" if is_nice else "not nice"


# ==============================
some_data = None
msg = some_data or "Не було повернено даних"
print(msg)# Не було повернено даних

some_data = None
if some_data:
    msg = some_data
else:
    msg = "Не було повернено даних"

