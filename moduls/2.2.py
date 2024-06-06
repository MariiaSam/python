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


#=====================================

# def modify_string(original: str) -> str:
#     original = "змінено"
#     return original

# str_var = "оригінал"
# print(modify_string(str_var))  # змінено
# print(str_var)                 # оригінал

#=====================================
# def modify_list(lst: list) -> None:
#     lst.append(4)

# my_list = [1, 2, 3]
# modify_list(my_list)
# print(my_list)  # [1, 2, 3, 4]

#=====================================
# def modify_list(lst: list) -> None:
#     lst = lst.copy()
#     lst.append(8)

# my_list = [1,2,3]
# modify_list(my_list)
# print(my_list) # [1, 2, 3]

#===================================== Області видимості (LEGB)

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

#================ Ключові аргументи функції


# def func(a, b=5, c=10):
#     print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)

# func(3, 7)

# func(25, c=24)

# func(c=50, a=100)
#================ 
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
def factorial(n):
    if n == 0: # базовий випадок
        return 1
    else:
        return n * factorial(n-1) # рекурсивний випадок

print(factorial(5)) # виведе 120
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
