'''
Напишіть програму, яка приймає від користувача рядок, і відображає цей рядок у верхньому і нижньому регістрах.

Вхідні дані:

My favourite language is Python
Вихідні дані:

MY FAVOURITE LANGUAGE IS PYTHON
my favourite language is python
'''

# string = 'My favourite language is Python'

# print(string.upper())
# print(string.lower())


# 2

'''
Скласти програму, яка запитує назву баскетбольної команди і повторює її на екрані зі словами: This is a champion!.

Вхідні дані:

Atlanta Hawks
Вихідні дані:

Atlanta Hawks! This is a champion!

'''

# name_team = input('Enter your favourite bassketball team: ')

# print(f'{name_team}! This is a champion!')

# 3
'''
Напишіть програму, яка виводить на екран рядок з 5-ти копій останніх двох символів введеного користувачем рядка (довжина введеного рядка повинна бути не менше 2).

Вхідні дані:

emu
lion
Вихідні дані:

mumumumumu
ononononon
'''

# def repeat_last():
#     while True:
#         input_str = input("Enter: ")

#         if len(input_str) < 3:
#             print('Please enter a string with at least 3 characters.')
#         else: 
#             last_two = input_str[-2: ]
#             result = ''
#             count = 0
#             while count < 5:
#                 result += last_two
#                 count += 1
#             return result

# print(repeat_last())

# 4. 


'''Дано натуральне число. Знайти число, утворене з вхідного приписуванням до нього такого ж числа.

Вхідні дані:

125
6
1
Вихідні дані:

125125
66
11'''

# def get_number(numbers):
#    change_firts = str(numbers)
#    change_second = change_firts * 2
#    result = int(change_second)
#    return result


# print(get_number(125))
# print(get_number(23))
# print(get_number(1))
      



