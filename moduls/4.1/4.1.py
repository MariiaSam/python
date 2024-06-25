# fh = open('test.txt', 'w')
# symbols_written = fh.write('hello!')
# print(symbols_written) # 6
# fh.close()

# ====================================
# fh = open('test.txt', 'w+')
# fh.write('hello!')
# fh.seek(0)

# first_two_symbols = fh.read(2)
# print(first_two_symbols)  # 'he'

# fh.close()

# # ====================================

# fh = open('test.txt', 'w')
# fh.write('hello!')
# fh.close()

# fh = open('test.txt', 'r')
# while True:
#     symbol = fh.read(1)
#     if len(symbol) == 0:
#         break
#     print(symbol)

# fh.close()

# h
# e
# l
# l
# o
# !

# # ====================================
# fh = open('test.txt', 'w')
# fh.write('first line\nsecond line\nthird line')
# fh.close()

# fh = open('test.txt', 'r')
# while True:
#     line = fh.readline()
#     if not line:
#         break
#     print(line)

# fh.close()
# # # ====================================
# fh = open('test.txt', 'w')
# fh.write('first line\nsecond line\nthird line')
# fh.close()

# fh = open('test.txt', 'r')
# lines = fh.readlines()
# print(lines) # ['first line\n', 'second line\n', 'third line']

# fh.close()

# ====================================

# fh = open('test.txt', 'w+')
# fh.write('hello!')

# fh.seek(1) # кількість символів, на які потрібно змістити курсор у файлі:

# second = fh.read(1-3)
# print(second)  # 'ello!' 

# fh.close()

# ====================================

# fh = open("test.txt", "w+")
# fh.write("hello!")

# position = fh.tell() #  положення курсора в цей момент
# print(position)  # 6
'''
 отримує поточну позицію курсора у файлі. У цьому випадку курсор знаходиться в кінці рядка "hello!", оскільки саме туди було записано дані. Функція tell() повертає 6, що відповідає кількості байтів у рядку "hello!"
'''


# fh.seek(1)
# position = fh.tell()
# print(position)  # 1

'''
fh.seek(1) переміщує курсор на одну позицію вперед від поточної. Це означає, що курсор буде знаходитися після першого символу рядка "hello!".
position = fh.tell() знову отримує поточну позицію курсора. Зараз вона 1, оскільки курсор знаходиться після першого символу.
'''

# fh.read(2)
# position = fh.tell()
# print(position)  # 3
'''
fh.read(2) читає два символи з файлу, починаючи з поточної позиції курсора. У цьому випадку курсор знаходиться після першого символу, тому читаються наступні два символи: "el".
position = fh.tell() знову отримує поточну позицію курсора. Зараз вона 3, оскільки курсор перемістився на два символи вперед.
'''

# fh.close()

# ===============================================

# with open("test.txt", "w") as fh:
#     fh.write("first line\nsecond line\nthird line") # \n представляють символи нового рядка, тому текст буде записано на окремих рядках у файлі.

# with open("test.txt", "r") as fh:
#     lines = [el.strip() for el in fh.readlines()] # el.strip() видаляє будь-які пробіли на початку або в кінці поточного рядка (el). Це забезпечує більш чисту обробку рядків.

# print(lines)


# =============================================== Pобота з не текстовими файлами у Python

# with open('raw_data.bin', 'wb') as fh:
#     fh.write(b'Hello world!')

# s = b'Hello!'
# print(s[1])  # Виведе: 101 (це ASCII-код символу 'e')


# byte_string = b'Hello world!'
# print(byte_string)

# byte_str = 'some text'.encode()
# print(byte_str) # b'some text'.


# Перетворення списку чисел у байт-рядок
# numbers = [0, 128, 255]
# byte_numbers = bytes(numbers)
# print(byte_numbers)  # b'\x00\x80\xff'


# from pathlib import Path

# # Створення об'єкту Path для файлу
# file_path = Path("test.txt")

# # Запис тексту у файл
# file_path.write_text("Привіт світ!", encoding="utf-8")

# text = file_path.read_text(encoding="utf-8")
# print(text) # Привіт світ!

# ===============================================
from pathlib import Path

# Створення об'єкту Path для бінарного файлу
file_path = Path("example.bin")

# Бінарні дані для запису
data = b"Python is great!"

# Запис байтів у файл
file_path.write_bytes(data)
