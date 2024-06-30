# =================================    Функції, область видимості змінних (LEGB)

# =================================    Функції
# def say():
#     print('Hello')

# say()
# Hello

# ================
# def print_max(a, b):
#     if a > b:
#         print(a, "max")
#     elif a < b:
#         print(a, "min")
#     elif a == b:
#         print(a, "дорінює", b)
#     else:
#         print(b, "max")

# print_max(3, 6) # 3 min

# x = 5
# y = 7
# print_max(x, y)

# ================

# def add_numbers(num1: int, num2: int) -> int:
#     sum = num1 + num2
#     return sum

# result = add_numbers(5, 10)
# print(result)  # Виведе: 15

# ================
# def add_numbers(num1: int, num2: int) -> int:
#     sum = num1 + num2
#     return sum

# result = add_numbers(5, 10)
# print(result)  # 15

# ================

# def is_even(num: int) -> bool:
#     return num % 2 == 0

# check_even = is_even(4)
# print(check_even)  # True

# ================
# def is_even(num: int) -> int:
#     return num % 2 == 0

# check_even = is_even(4)
# print(check_even)


# =====================================

# def modify_string(original: str) -> str:
#     original = "змінено"
#     return original

# str_var = "оригінал"
# print(modify_string(str_var))  # змінено
# print(str_var)                 # оригінал

# =====================================
# def modify_list(lst: list) -> None:
#     lst.append(4)

# my_list = [1, 2, 3]
# modify_list(my_list)
# print(my_list)  # [1, 2, 3, 4]

# =====================================
# def modify_list(lst: list) -> None:
#     lst = lst.copy()
#     lst.append(8)

# my_list = [1,2,3]
# modify_list(my_list)
# print(my_list) # [1, 2, 3]

# ===================================== Області видимості (LEGB)

# ================ Local

# x = 50

# def func() -> None:
#     x = 2
#     print('Зміна локального x на', x) ## Зміна локального x на

# func()
# print('Глобальний x як і раніше', x)  # x як і раніше 50

# ================ Enclosing
# def outer_func():
#     enclosing_var = "Я змінна в функції, що охоплює"

#     def inner_func():
#         print("Всередині вкладеної функції:", enclosing_var)

#     inner_func()

# outer_func()

# ================ як змінювати функції в функії

# def func_outer():
#     x = 2

#     def func_inner():
#         nonlocal x
#         x = 5

#     func_inner()
#     return x

# result = func_outer()

# ================ Global
# x = 50

# def func():
#     global x
#     print('x дорівнює', x)  # x дорівнює 50
#     x = 2
#     print('Змінюємо глобальне значення x на', x) # Змінюємо глобальне значення x на 2

# func()
# print('Значення x складає', x) # Значення x складає 2

# ================ Ключові аргументи функції


# def func(a, b=5, c=10):
#     print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)

# func(3, 7)

# func(25, c=24)

# func(c=50, a=100)
# ================
# def say(message, times=1):
#     print(message * times)

# say('Привіт') # Привіт
# say('Світ', 5) # СвітСвітСвітСвітСвіт


# ==================================== *args
# def print_all_args(*args):
#     for arg in args:
#         print(arg)

# print_all_args(1, 'hello', True)

# 1
# hello
# True

# ==================================== **kwargs
# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# greet(name="Alice", age=25)

# name: Alice
# age: 25

# ==================================== **Рекурсія
# def factorial(n):
#     if n == 0: # базовий випадок
#         return 1
#     else:
#         return n * factorial(n-1) # рекурсивний випадок

# print(factorial(5)) # виведе 120
# 1. Визначення функції factorial
# Функція factorial визначається для обчислення факторіалу числа n.

# 2. Базовий випадок

# if n == 0: # базовий випадок
#     return 1
# Факторіал числа 0 визначається як 1. Це є базовий випадок для рекурсії. Якщо n дорівнює 0, функція повертає 1, завершуючи рекурсію.

# 3. Рекурсивний випадок

# else:
#     return n * factorial(n-1) # рекурсивний випадок
# Якщо n не дорівнює 0, функція обчислює факторіал числа n як n, помножене на факторіал числа n-1. Це створює рекурсивний виклик функції, тобто функція викликає саму себе з аргументом n-1.

# 4. Виклик функції factorial

# print(factorial(5)) # виведе 120
# Тут функція викликається з аргументом 5. Давайте розглянемо, як це працює крок за кроком:

# factorial(5) обчислюється як 5 * factorial(4)
# factorial(4) обчислюється як 4 * factorial(3)
# factorial(3) обчислюється як 3 * factorial(2)
# factorial(2) обчислюється як 2 * factorial(1)
# factorial(1) обчислюється як 1 * factorial(0)
# factorial(0) повертає 1 (базовий випадок)
# Тепер ці значення об'єднуються у зворотному порядку:

# factorial(1) = 1 * 1 = 1
# factorial(2) = 2 * 1 = 2
# factorial(3) = 3 * 2 = 6
# factorial(4) = 4 * 6 = 24
# factorial(5) = 5 * 24 = 120
# Отже, функція factorial(5) повертає 120.

# Таким чином, на екран буде виведено значення 120.

# =====================================
# Числа Фібоначчі — це послідовність чисел, у якій кожне наступне число є сумою двох попередніх. Перші два числа в цій послідовності, за визначенням, дорівнюють 0 і 1.

# def fibonacci(n):
#     if n <= 1: # базовий випадок
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2) # рекурсивний випадок

# print(fibonacci(10)) #  55

# ====================================     Стек викликів рекурсії


# def factorial(n):
#     print("Виклик функції factorial з n = ", n)
#     if n == 1:
#         print("Базовий випадок, n = 1, повернення 1")
#         return 1
#     else:
#         result = n * factorial(n-1)
#         print("Повернення результату для n = ", n, ": ", result)
#         return result

# print(factorial(5))

# Виклик функції factorial з n =  5
# Виклик функції factorial з n =  4
# Виклик функції factorial з n =  3
# Виклик функції factorial з n =  2
# Виклик функції factorial з n =  1
# Базовий випадок, n = 1, повернення 1
# Повернення результату для n =  2 :  2
# Повернення результату для n =  3 :  6
# Повернення результату для n =  4 :  24
# Повернення результату для n =  5 :  120
# 120

# ==================================== Автоперевірка
# 1.
# is_next = None
# num = int(input("Enter the number of points: "))
# if num >= 83:
#     is_next = True
# else:
#     is_next = False

# 2.
# work_experience = int(input("Enter your full work experience in years: "))
# if 1 < work_experience <= 5:
#     developer_type = "Middle"
# elif work_experience <= 1:
#     developer_type = "Junior"
# else:
#     developer_type = "Senior"


# # 3.
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

# 4.
# num = int(input("Enter the integer (0 to 100): "))
# sum = 0

# while num > 0:
#     sum += num
#     num -= 1

# 5.
# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0
# for i in message:
#     if i == search:
#         result += 1
# print(result)

# 6.
# pool = 1000
# quantity = int(input("Enter the number of mailings: "))
# try:
#     if quantity != 0:
#         chunk = int(pool / quantity)
#         print(f'Розмір пакету SMS для кожної розсилки: {chunk}')
#     else:
#         raise ZeroDivisionError # raise ZeroDivisionError означає, що програма згенерує виключення ZeroDivisionError вручну, якщо введене користувачем значення quantity дорівнює нулю. Це зроблено для того, щоб запобігти поділу на нуль, який не допустимий в математиці та програмуванні.

# except ZeroDivisionError:
#     print('Поділ на нуль неможливий!')


#     try:
#     # Код, який може згенерувати виняток
# except:
#     # Код для виконання у разі генерації винятку

# 7.
# def greeting():
#     print("Hello world!")

# greeting()

# 8.
# def invite_to_event(username):
#     return f"Dear {username}, we have the honour to invite you to our event"

# 9.

# def discount_price(price, discount):

#     def apply_discount():
#         nonlocal price
#         return price * (1 - discount)

#     apply_discount()
#     return price * (1 - discount)

# 10.
# def get_fullname(first_name, last_name, middle_name=''):
#     if  middle_name:
#        return f'{first_name} {middle_name} {last_name}'
#     else:
#         return f'{first_name} {last_name}'

# 11.
# def format_string(string, length):
#     if len(string) < length:
#         space = (length - len(string)) // 2
#         return " " * space + string
#     else:
#          return string


# 12.
# def first(size, *args):
#     return size + len(args)


# def second(size, **kwargs):
#     return size + len(kwargs)


# print(first(5, "first", "second", "third"))  # Результат: 8
# print(first(1, "Alex", "Boris"))             # Результат: 3
# print(second(3, comment_one="first", comment_two="second", comment_third="third"))  # Результат: 6
# print(second(10, comment_one="Alex", comment_two="Boris")) # Результат: 12

# 13
# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n - 1)


# def number_of_groups(n, k):
#     return factorial(n) // (factorial(n - k) * factorial(k))

#=============================================


'''
Незмінні типи в Python — це ті, що не можуть бути змінені після їх створення. Це включає типи, як-от цілі числа int, дійсні числа float, рядки str, кортежі tuple.


'''
number = 1
print(number)

print(float(number))

#========================================= Розпакування списків та словників

# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old.")

# person_info = {"name": "Alice", "age": 25}
# greet(**person_info)
#================================

# my_list = [1, 2, 3]
# a, b, c = my_list
# print(my_list)

# a, _, c = my_list
# print(my_list)

# a, *rest = my_list
# print(my_list)


#========================================= 

# text = 'Lorem ipsum is simply'
# dict_count = {}


# for char in text:
#     try:
#        count = dict_count[char] # отримуємо значення по ключу
       
#     except KeyError:
#         count = 0
#     count += 1
#     dict_count[char] = count # записуємо значення по ключу

# print(dict_count)

   # {'L': 1, 'o': 1, 'r': 1, 'e': 1, 'm': 3, ' ': 3, 'i': 3, 'p': 2, 's': 3, 'u': 1, 'l': 1, 'y': 1}

   # or

# text = 'Lorem ipsum is simply'
# dict_count = {}

# for char in text:
#        count = dict_count.get(char, 0) # отримуємо значення по ключу
#        count += 1
#        dict_count[char] = count # записуємо значення по ключу

# print(dict_count)
# # {'L': 1, 'o': 1, 'r': 1, 'e': 1, 'm': 3, ' ': 3, 'i': 3, 'p': 2, 's': 3, 'u': 1, 'l': 1, 'y': 1}