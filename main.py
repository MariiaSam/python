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


# int_num = 5
# float_num = 4.5

# # print(int_num + float_num)
# # 9.5

# print(float_num + int_num)
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

# =======================

# int_num = 5
# float_num = 4.5

# print(int_num + float_num)
# # 9.5

# print(int_num.__add__(float_num))
# #NotImplemented 
# # магічні методи класу int

# print(float_num.__radd__(int_num))
# # 9.5
# # магічні методи класу float

# =======================

# int_num = 3
# float_num = 10.2
# str_v = 'vavav'

# print(int_num * float_num)
# 13.2 +
# 30.599999 *

# print(int_num * str_v)
# print(str_v * int_num)

#vavavvavavvavav

# print(int_num.__add__(float_num))

# print(float_num.__radd__(int_num))


# print(int_num.__mul__(float_num))
# NotImplemented

# print(int_num.__mul__(str_v))
# NotImplemented


# print(float_num.__rmul__(int_num))
#30.599999999999998

# print(str_v.__rmul__(int_num))
#vavavvavavvavav


# ======================МАГІЧНІ МЕТОДИ
# add__()
# __eq__()
# __and__()
# _str__()
# __neq__()
# __or__()

# print(bool)
# #<class 'bool'>

# print(dir(bool))

# print(bool.__doc__)
# # bool(x) -> bool

# print(str.__doc__)

# my_list = []

#my_list._

# print(help(my_list.__add__))


# ======================СПИСКИ LIST
empty_list = []

my_fruits = ['apple', 'banana', 'lime']

posts_ids = [1, 3, 44, 780]

users_inputs = [True, 1, 'hi', False, 6]

# ======================Довжина СПИСКу LIST

# print(len(empty_list))
# #0

# print(len(my_fruits))
# # 3

# print(len(posts_ids))
# # 4

# print(len(users_inputs))
# 5
# ======================

posts_ids = [125, 245, 3456, 76, 456, 9978, 67]

print(posts_ids[0]) # 125
print(posts_ids[1]) # 245

print(posts_ids[-1]) # 67


# ====================== змінювати індекс

posts_ids[0] = 9
posts_ids[3] = 4

print(posts_ids)
# [9, 245, 3456, 4, 456, 9978, 67]
# відбулас ь мутація обʼєкта, зміна відбулась в існуюому списку


# ====================== видалити елемент списку

user_inputs = [True, 'hi', 'ffff', 123456]
print(len(user_inputs)) # 4

del user_inputs[1]
print(user_inputs) # [True, 'ffff', 123456]
print(len(user_inputs)) # 3

del user_inputs[-1]
print(user_inputs) # [True, 'ffff']
print(len(user_inputs)) # 2