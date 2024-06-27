# import math

# sin_pi = math.sin(math.pi)
# print(sin_pi) # 1.2246467991473532e-16

# ====================================

# from math import pi, sin

# sin_pi = sin(pi)


# ====================================
# def say_hello(name):
#     print(f'Hello, {name}')

# print("You imported hello.py")
# say_hello('user')


# import sys

# for arg in sys.argv:
#     print(arg)

# ====================================
# def is_palindrome(s: str) -> bool:
#     new_s = ""
#     for char in s:
#             if char.isalnum(): #  перевіряє, чи є символ буквою або цифрою. Якщо так, він додається до new_s у нижньому регістрі (char.lower()).
#                 new_s += char.lower()
#     s = new_s
#     length = len(s)
#     for i in range(length // 2):
#         if s[i] != s[length - i - 1]:
#             return False
#     return True


# # Використання функції
# print(is_palindrome("Козак з казок"))  # Виведе: True

'''
Ця функція приймає рядок s як вхідний параметр і повертає True, якщо цей рядок є паліндромом (тобто читається однаково зліва направо і справа наліво, ігноруючи пробіли, великі літери та небуквено-цифрові символи), і False в іншому випадку.
'''

# def is_palindrome(s: str) -> bool:
#     new_s = ""
#     for char in s:
#         if char.isalnum():
#             new_s += char.lower()

#     s = new_s
#     return s == s[::-1]

# # Використання функції
# print(is_palindrome("Козак з казок"))  # Виведе: True