# 1.
'''
Напишіть програму для друку дробових чисел у форматі до 2 десяткових знаків.

Вхідні дані:

3.1415926
1.4567
5.8
Вихідні дані:

3.14
1.46
5.80

'''

# def float_numbers(number):
#     value = round(number, 2)
#     print(value)

# result = float_numbers(3.1415926)
# result = float_numbers(1.4567)
# result = float_numbers(5.8)

'''
3.14
1.46
5.8
'''

# def float_numbers(number):
#     value = f"{number:.2f}"
#     print(value)

# result = float_numbers(3.1415926)
# result = float_numbers(1.4567)
# result = float_numbers(5.8)

'''
3.14
1.46
5.80
'''

# 2
'''
Напишіть програму для друку цілих чисел з нулями ліворуч, якщо введене число має у своєму записі менше 5 розрядів.

Вхідні дані:

125
20
12805
Вихідні дані:

00125
00020
12805

'''

# def print_numbers(numbers):
#     pass
#     str_numbers = str(numbers)

#     if len(str_numbers) < 5:
#         zero = "0" * (5 -len(str_numbers))
#         formatted_number = zero + str_numbers
#     else:
#         formatted_number = str_numbers

#     print(formatted_number)


# result = print_numbers(125)
# result = print_numbers(20)
# result = print_numbers(12805)

# 3

'''
Напишіть програму, щоб надрукувати цілі числа із ∗ справа, якщо введене число має у своєму записі менше 7 розрядів.

Вхідні дані:

23
1400231
-16
Вихідні дані:

23*****
1400231
-16****
'''

# def add_stars(numbers):
#     str_numbers = str(numbers)

#     if len(str_numbers) < 7:
#         star = "*" * (7 - len(str_numbers))
#         formatted_number = str_numbers + star
#     else:
#         formatted_number = str_numbers
#     print(formatted_number)

# result =  add_stars(23)
# result =  add_stars(1400231)
# result =  add_stars(-16)

'''
23*****
1400231
-16****
'''

# 3

'''
Напишіть програму для форматування числа з відсотком.
Вхідні дані:

0.05
0.245
1
Вихідні дані:

5.00%
24.50%
100.00%
'''

# def format_percent(number):
#     numb = number * 100
#     formatted_number = f'{numb:.2f}'
#     formatted_number += '%'
    
#     print(formatted_number)


# result = format_percent(0.05)
# result = format_percent(0.245)
# result = format_percent(1)


'''
5.00%
24.50%
100.00%
'''

# 4 
'''
Обчисліть n181 і виведіть на екран обчислене значення. Значення n - ціле число, яке вводиться з клавіатури.

Вхідні дані:

2
Вихідні дані:

3064991081731777716716694054300618367237478244367204352
'''

# number = int(input("Enter number: "))
# pow_number = number ** 181
# print(pow_number)

# 3064991081731777716716694054300618367237478244367204352

# import math
# number2 = int(input("Enter number: "))

# pow_number2 = math.pow(number2, 181)
# print(int(pow_number2))

# 3.064991081731778e+54, якщо не перевести в int

# 3064991081731777716716694054300618367237478244367204352


# 5

'''
Дано два цілих додатних числа a і b, які не перевищують 1000. Обчисліть і виведіть гіпотенузу трикутника із заданими катетами.

Вхідні дані:

10
18
Вихідні дані:

20.591260281974
'''

# import math

# pow_1 = int(input("Enter first numb: "))
# pow_2 = int(input("Enter second numb: "))


# c_pow = math.pow(pow_1, 2) + math.pow(pow_2, 2)
# print(c_pow)
# c_sqrt = math.sqrt(c_pow)
# print(c_sqrt)

# '20.591260281974'

# 5
# Напишіть програму, яка зчитує довжину основи та висоту прямокутного трикутника (цілі числа), обчислює площу і друкує її значення на екрані у відформатованому вигляді (два символи після десяткової крапки). Кожен параметр вводиться на окремому рядку.

# Вхідні дані:

# 3
# 4
# Вихідні дані:

# 6.00

length_01 = int(input("Enter 1: "))
length_02 = int(input("Enter 2: "))

result = (length_01 * length_02) * 0.5
print(f'{result:.2f}') # 6.00

