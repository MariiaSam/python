#======================================= Функція як об'єкт першого класу

# def my_function():
#     print("Hello, world!")

# f = my_function
# f() # Hello, world!


#===================

# from typing import Callable

# def add(a: int, b: int) -> int:
#     return a + b

# def multiply(a: int, b: int) -> int:
#     return a * b

# def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
#     return operation(a, b)

# # Використання
# result_add = apply_operation(5, 3, add)
# result_multiply = apply_operation(5, 3, multiply)

# print(result_add, result_multiply) # 8 15

#===================


# from typing import Callable

# def power(exponent: int) -> Callable[[int], int]:
#     def inner(base: int) -> int:
#         return base ** exponent
#     return inner

# # Використання
# square = power(2)
# cube = power(3)

# print(square(4)) # 16
# print(cube(4)) # 64

#======================================
# from typing import Callable, Dict

# Визначення функцій
# def add(a: int, b: int) -> int:
#     return a + b

# def multiply(a: int, b: int) -> int:
#     return a * b

# def power(exponent: int) -> Callable[[int], int]:
#     def inner(base: int) -> int:
#         return base ** exponent
#     return inner

# # Використання power для створення функцій square та cube
# square = power(2)
# cube = power(3)

# # Словник операцій
# operations: Dict[str, Callable] = {
#     'add': add,
#     'multiply': multiply,
#     'square': square,
#     'cube': cube
# }

# # Використання операцій
# result_add = operations['add'](10, 20)  # 30
# result_square = operations['square'](5)  # 25

# print(result_add)  # 30
# print(result_square)  # 25


#====================================================
# def outer_function(msg):
#     message = msg

#     def inner_function():
#         print('2', message)

#     return inner_function

# # Створення замикання
# my_func = outer_function("Hello, world!") # # Hello, world!

# my_func() # # 2 Hello, world!

# # Hello, world!
# # 2 Hello, world!''


# #====================================================

# from typing import Callable

# def counter() -> Callable[[], int]:
#     count = 0

#     def increment() -> int:
#         # використовуємо nonlocal, щоб змінити змінну в замиканні
#         nonlocal count  
#         count += 1
#         return count

#     return increment

# # Створення лічильника
# count_calls = counter()

# # Виклики лічильника
# print(count_calls())  # Виведе 1
# print(count_calls())  # Виведе 2
# print(count_calls())  # Виведе 3

#=======================================
# def add(a):
#     def add_b(b):
#         return a + b
#     return add_b

# # Використання:
# add_5 = add(5)
# result = add_5(10)
# print(result)

# 15

# ===================================

# def apply_discount(price: float, discount_percentage: int) -> float:
#     return price * (1 - discount_percentage / 100)

# # Використання
# discounted_price = apply_discount(500, 10)  # Знижка 10% на ціну 500
# print(discounted_price) # 450

# discounted_price = apply_discount(500, 20)  # Знижка 20% на ціну 500
# print(discounted_price) # 400


# ===================================
# from typing import Callable

# def discount(discount_percentage: int) -> Callable[[float], float]:
#     def apply_discount(price: float) -> float:
#         return price * (1 - discount_percentage / 100)
#     return apply_discount

# # Каррінг в дії
# ten_percent_discount = discount(10)
# twenty_percent_discount = discount(20)

# # Застосування знижок
# discounted_price = ten_percent_discount(500)  # 450.0
# print(discounted_price)

# discounted_price = twenty_percent_discount(500)  # 400.0
# print(discounted_price)

#==========================================

# from typing import Callable, Dict

# def discount(discount_percentage: int) -> Callable[[float], float]:
#     def apply_discount(price: float) -> float:
#         return price * (1 - discount_percentage / 100)
#     return apply_discount

# # Створення словника з функціями знижок
# discount_functions: Dict[str, Callable] = {
#     "10%": discount(10),
#     "20%": discount(20),
#     "30%": discount(30)
# }

# # Використання функції зі словника
# price = 500
# discount_type = "20%"

# discounted_price = discount_functions[discount_type](price)
# print(f"Ціна зі знижкою {discount_type}: {discounted_price}")

#==========================================
# def complicated(x: int, y: int) -> int:
#     return x + y

# def logger(func):
#     def inner(x: int, y: int) -> int:
#         print(f"Викликається функція: {func.__name__}: {x}, {y}")
#         result = func(x, y)
#         print(f"Функція {func.__name__} завершила виконання: {result}")
#         return result

#     return inner

# complicated = logger(complicated)
# print(complicated(2, 3))


#========================================== List Comprehensions


# [new_item for item in iterable if condition]

# sq = [x**2 for x in range(1, 6)]
# print(sq) # [1, 4, 9, 16, 25]


# even_squares = [x**2 for x in range(1, 10) if x % 2 == 0]
# print(even_squares) # [4, 16, 36, 64]
 

 #==========================================Set Comprehensions

# {new_item for item in iterable if condition}
# numbers = [1, 4, 1, 3, 2, 5, 2, 6]
# sq = {i ** 2 for i in numbers}
# print(sq)
# {1, 4, 36, 9, 16, 25}

#========================================== Dictionary Comprehensions

# {key: value for item in iterable if condition}
# sq = {x: x**2 for x in range(1, 10)}
# print(sq)

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# sq_dict = {x: x**2 for x in range(1, 10) if x > 5}
# print(sq_dict)

# {6: 36, 7: 49, 8: 64, 9: 81}

#========================================== Лямбда-функції
# lambda arguments: expression

# add = lambda x, y: x + y
# print(add(5, 3))  # Виведе 8


# nums = [1, 2, 3, 4, 5]
# nums_sorted = sorted(nums, key=lambda x: -x)
# print(nums_sorted)

# [5, 4, 3, 2, 1]

#====================#====================#====================MAP
# numbers = [1, 2, 3, 4, 5]

# squared_nums = list(map(lambda x: x ** 2, numbers))
# print(squared_nums)
# # [1, 4, 9, 16, 25]


# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# sum_nums = map(lambda x, y: x + y, nums1, nums2)

# print(list(sum_nums))
# [5, 7, 9]


#====================#====================#==================== filter
# even_nums = filter(lambda x: x % 2 == 0, range(1, 11))

# print(list(even_nums))

# [2, 4, 6, 8, 10]


#====================#==
# some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'

# new_str = ''.join(list(filter(lambda x: x.islower(), some_str)))
# print(new_str)

# идавництво

#====================# any

# nums = [0, False, 5, 0]
# result = any(nums)  
# print(result)

# True
# 
# ++++++++++++++++++++++++++++++++++++++++++ Osadchuk

# ==========================================
# - може бути передана в іншу функцію як аргумент;
# def sum(a, b):
#     return a+b

# def operation(k, m, func):
#     return func(k, m)

# print(operation(5, 3, sum))

# ========================================== Замикання

message = 'Goodbye'
def outer_func(name):
    message = 'Hello'
    def inner_func(message, name):
        return f'{message} {name}'
    return inner_func(message, name)

print(message)
print(outer_func('Oleh'))

#========================================
def factorial(n, cache={}):
    if n < 0:
        raise ValueError

    def counter(n):
        result = 1
        for value in range(1, n+1):
            if value in cache:
                result = cache[value]
            else:
                result = value * cache.get(value-1, 1)
                cache[value] = result
                print('{} not in cache {}'.format(value, result))
        return result

    return counter(n)

print(factorial(3))
print(factorial(6))
print(factorial(4))