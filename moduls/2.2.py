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

#=====================================


