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
x = 50

def func():
    global x
    print('x дорівнює', x)  # x дорівнює 50
    x = 2
    print('Змінюємо глобальне значення x на', x) # Змінюємо глобальне значення x на 2

func()
print('Значення x складає', x) # Значення x складає 2

#================ Ключові аргументи функції