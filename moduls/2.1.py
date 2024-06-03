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

a = False or False
print(a)  # False


# ==============================    тернарні оператори
is_nice = True
state = "nice" if is_nice else "not nice"


# ==============================
some_data = None
msg = some_data or "Не було повернено даних"
print(msg)  # Не було повернено даних

some_data = None
if some_data:
    msg = some_data
else:
    msg = "Не було повернено даних"

# ==============================        Оператор match

fruit = "apple"

match fruit:
    case "apple":
        print("This is an apple.")
    case "banana":
        print("This is a banana.")
    case "orange":
        print("This is an orange.")
    case _:
        print("Unknown fruit.")


# ==============================
point = (1, 0)

match point:
    case (0, 0):
        print("Точка в центрі координат")
    case (0, y):
        print(f"Точка лежить на осі Y: y={y}")
    case (x, 0):
        print(f"Точка лежить на осі X: x={x}")
    case (x, y):
        print(f"Точка має координати:  x={x}, y={y}")
    case _:
        print("Це не точка")

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
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    print(i, end=" ")  # a b c d e f g h i j k l m n o p q r s t u v w x y z
  # ==============================

odd_numbers = [1, 3, 5, 7, 9]
for i in odd_numbers:
    print(int(i ** 0.6))

# 1
# 2
# 3
# 3

# ============================== Цикл WHILE


k = 0
while k < 10:
    k = k + 1
    print(k)
#===============================
a = 0
while True:
    print(a)
    if a >= 20:
        break
    a = a + 1

#===============================

while True:
    user_input = input()
    print(user_input)
    if user_input == "exit":
        break

#===============================
a = 0
while a < 6:
    a = a + 1
    if not a % 2:
        continue
    print(a)
