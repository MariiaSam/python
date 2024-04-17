# def sum_nums(a, b):
#     sum = a - b
#     return sum


# first_sum = sum_nums(5, 4)
# print(first_sum)


# print(input("Enter your name: "))

# ================
# import datetime

# print(datetime.MAXYEAR)

# ================ STATEMENTS
# def sum_nums(a, b):
#     sum = a - b
#     return sum


# result = sum_nums(5, 3)
# print(result)

# my_number = 10
# print(my_number)
# кожне число - це ексз класу int

# цілі числа, строки, логічні типи, списки, словники

# my_number = 34
# print(my_number)
# цілі числа,

# my_string = 'Mariia'
# print(my_string)
# строки

# my_type = False
# print(my_type)
# логічні типи,

# my_list = [1, "Mariia", True]
# print(my_list)
# списки

# my_dictionary = {"name": 'Mariia', "son": "Lev"}
# print(my_dictionary)
# словники

# =======================
# динамічна типізація


# def print_name(name):
#     print(name)


# print_name("Mariia")


# print_name = 34

# print_name('Mariia')

# =======================

# my_number = 34

# print(id(my_number))

# my_string = 'Leo'
# print(id(my_string))

# my_string = my_number
# print(id(my_string))

# =======================
# greeting = 'Hello from Python'
# print(greeting)

# print(type(greeting))

# print(id(greeting))
# =======================

# info_msg = """Це показує, яку частину змісту курсу ви пройшли. Зверніть увагу, що деякі матеріали можуть бути ще не опубліковані."""

# print(info_msg)
# =======================

# long_str = """qwertyuiop"""

# print(long_str)

# print(type(long_str))
# print(id(long_str))

# =======================Вбудовані функції рядків

# print(len(long_str))
# #10

# print(long_str[0])
# #q

# print(long_str[3:6])
#rty


# =======================Методи рядків

# my_comment = 'This, is my shot comment'

# print(len(my_comment))

# print(my_comment.replace('shot', 'long'))

# print(my_comment.count(' '))

# print(my_comment[-1])

# =======================ЦІЛІ ЧИСЛА. Class int
# any_num = input('Enter any name: ')

# print(any_num)

# print(type(any_num))

# =======================

# user_input = input('Enter your number: ')
# any_num = int(user_input) # значення рядка буде конвертоване в ціле число int

# print(any_num)

# print(type(any_num))

# ======================= Як конвертувати результат input в число
# any_num = int(input('Enter your: '))

# print(any_num)

# print(type(any_num))


# ======================= піднесення до степеню

# base = 5
# power = 3

# print(pow(base, power))

# ===================
# one = 24

# two = 3

# print(pow(one, two))

# print(type(pow))

# ======================= довгі числа

# one_million = 1_000_000

# print(one_million)

# my_number = 3_427

# print(my_number)

# =======================

# input_str = input("Enter any number:   ")
# input_int = int(input_str)

# print(input_int)

# print(type(input_int))

# =======================

# long_int = 1_0_00_000_000

# print(long_int)

# ======================= числа з десятковою частиною FLOAT 
 
# average_price = 17.25

# print(average_price)

# print(type(average_price))

# ======================= 
# rounded_price = round(average_price)
# print(rounded_price)

# ======================= 
# abs_price = abs(average_price)
# print(abs_price)

# ======================= 

# average_price = 28.48
# price = int(average_price)

# print(price)
# print(type(price))

# str_temperature = '14.5'
# temperature = float(str_temperature)

# print(temperature)
# print(type(temperature))

# ======================= 

# rate = 12.65

# print(round(rate))

# rate_min = 12.43

# print(round(rate_min))

# ======================= ЧИСЛА COMPLEX, використовуються для різноманітних математичних рівнянь а також при опрацюванні даних 

# complex_a = 3 + 5j
# complex_b = 8 + 6j

# sum = complex_a + complex_b

# print(sum)
# #(11+11j)

# print(type(sum))
# <class 'complex'>

# ======================= 

# complex_a = 7 + 10j
# complex_b = 5 + 6j

# print(complex_a + complex_b)
# # (12+16j)

# print(complex_a * complex_b)

# # (7 + 10j) * (5 + 6j) = 35 + 42j + 50j - 60 = -25 + 92j
# # для комплексних чисел j в кв. - це мінус 60j^2

# ======================= Логічні значення BOOL
#  True | False

# ======================= ПЕРЕВІРКА
# is_authorized = True

# print(is_authorized)

# print(type(is_authorized))
# # True
# # <class 'bool'>

# print(100 > 35)
# #True

# print(3 > 35)
# # False

# print('Long str' > 'Long')
# #True

# print([1, 2, 3 ] == [1, 2, 3])
#True

# ======================= КОНВЕРТАЦІЯ В ЛОГІЧНЕ ЗНАЧЕННЯ

# print(bool(10)) 
# # True

# print(bool([]))
# #False

# print(bool('aaa'))
# # True

# print(bool([1, 2, 3]))
# # True

# print(bool(None))
# #False

# print(100 > 10)
# # True

# print("Long str" > "Short")
# #False, відбувається посимвольне порівняння

# print("Long str" > "Long")
# true

# print([] == [])
# # True

# print({'a': 3 } == {'a': 8})
# False

# print({'a': 6 } == {'a': 6})
# # True


# ======================= КОНВЕРТАЦІЯ ТИПІВ
# Python не виконує неявну конвертацію типів значень

# str_count = '10' + '5'
# print(str_count)
# 105



# str_count = '10' + 5
# print(str_count)
#TypeError: can only concatenate str (not "int") to str


# str_count = 10 + '5'
# print(str_count)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# ======================= кон=ректне складання різних типів

# str_count = 5 + int('10')
# 15


int_num = 5
float_num = 4.5

# print(int_num + float_num)
# 9.5

print(float_num + int_num)
# 9.5 

# bool_val = True
# int_val = 9

# print(bool_val + int_val)
#10


# =======================

# bool_val = False
# int_val = 9

# print( int_val - bool_val )
#9

# print( bool_val - bool_val)
#0

