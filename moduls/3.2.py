# query = ("SELECT * "
#          "FROM some_table "
#          "WHERE condition1 = True "
#          "AND condition2 = False")

# print(query)

# # SELECT * FROM some_table WHERE condition1 = True AND condition2 = False

# print("Hello\nWorld")

# # Hello
# # World

# print("Hello\tWorld")
# # Hello   World

# print("Hello\bWorld")
# # HellWorld

# print("Hello\\World")
# # Hello\World

# print('It\'s a beautiful day')
# # It's a beautiful day

# print("He said, \"Hello\"")
# # He said, "Hello"


# ============================================== Методи рядків

# ++++++++++++++++++++++++++++++++++++++++++++++ find
# s = "Hi there!"

# start = 0
# end = 7

# print(s.find("er", start, end)) # 5
# print(s.find("q")) # -1

# ++++++++++++++++++++++++++++++++++++++++++++++ find, rfind

# s = 'Some words'
# print(s.find("o")) # 1
# print(s.rfind('o')) # 6

# ++++++++++++++++++++++++++++++++++++++++++++++ join
# list_of_strings = ['Hello', 'world']
# result = '='.join(list_of_strings)
# print(result)  # 'Hello=world'


# ++++++++++++++++++++++++++++++++++++++++++++++ isdigit()

# number = "12345"
# print(number.isdigit())  # True

# text = "Number123"
# print(text.isdigit())  # False

# for char in "Hello 123":
#     if char.isdigit():
#         print(f"'{char}' - це цифра")
#     else:
#         print(f"'{char}' - не цифра")
'''
'H' - не цифра
'e' - не цифра
'l' - не цифра
'l' - не цифра
'o' - не цифра
' ' - не цифра
'1' - це цифра
'2' - це цифра
'3' - це цифра
'''

# ++++++++++++++++++++++++++++++++++++++++++++++ Translate()
# intab = "aeiou"
# outtab = "12345"
# trantab = str.maketrans(intab, outtab)

# str = "This is string example"
# print(str.translate(trantab))

# Th3s 3s str3ng 2x1mpl2

# ========================================================
from datetime import datetime


def string_to_date(date_string):
    converted_date = datetime.strptime(date_string, '%Y.%m.%d')
    return converted_date


def date_to_string(date):
    now = datetime.date()
    date_string = date.strftime(date, '%Y.%m.%d')
    return date_string