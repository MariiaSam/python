#======================================= Функція як об'єкт першого класу

def my_function():
    print("Hello, world!")

f = my_function
f() # Hello, world!


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
 