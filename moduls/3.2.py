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
# ========================================================
# exemples = 0.437444
# print(f'{exemples:.1%}') # 43.7%
# print(f'{exemples:.10%}')# 43.7444000000%
# print(f'{exemples:.5%}') # 43.74440%
# print(f'{exemples:.2%}') # 43.74%
# print(f'{exemples:1%}') # 43.744400%

string = 'apple,banana,orange'
print(string, end=',' )
'''
   *objects — об’єкт для виводу. * вказує, що об’єктів може бути декілька;

   sep (не обов’язково) — вказує, як розділяти об’єкти, якщо їх декілька. За замовчуванням використовується ' ';

   end (не обов’язково) — вказує, що виводити в кінці. За замовчуванням використовується '\n';

   file (не обов’язково) — об’єкт із методом запису. За замовчуванням використовується sys.stdout;

   flush (не обов’язково) — логічне значення, як

'''





# ++++++++++++++++++++++++++++++++++++++++++++++ Translate()
# intab = "aeiou"
# outtab = "12345"
# trantab = str.maketrans(intab, outtab)

# str = "This is string example"
# print(str.translate(trantab))

# Th3s 3s str3ng 2x1mpl2

# ========================================================
# 1.
# from datetime import datetime


# def string_to_date(date_string):
#     converted_date = datetime.strptime(date_string, '%Y.%m.%d')
#     conv = datetime.date(converted_date)
#     return conv

# def date_to_string(date):
#     date_string = date.strftime('%Y.%m.%d')
#     return date_string

# print(string_to_date("2024.01.01"))
# print(date_to_string(2024-01-01))

# ========================================================
# 2.
# from datetime import datetime


# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()


# def prepare_user_list(user_data):
#     prepared_list = []
#     for user in user_data:
#         name = user["name"]
#         birthday_str = user["birthday"]
#         birthday_date = string_to_date(birthday_str)
#         prepared_list.append({"name": name, "birthday": birthday_date})
#     return prepared_list


# users = [
#     {"name": "Bill Gates", "birthday": "1955.3.25"},
#     {"name": "Steve Jobs", "birthday": "1955.3.21"},
#     {"name": "Jinny Lee", "birthday": "1956.3.22"},
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"}
# ]

# prepared_users = prepare_user_list(users)
# print(prepared_users)

# ========================================================
# 3.
# from datetime import datetime, timedelta

# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()

# def find_next_weekday(start_date, weekday):
#     days_ahead = weekday - start_date.weekday()
#     if days_ahead <= 0: 
#         days_ahead += 7
#     return start_date + timedelta(days=days_ahead)

# ========================================================
# def fnc(n):
#     if n == 3:
#         return 3
#     return fnc(n-1) + n

# result = fnc(5)
# print(result)

# ========================================================
# d = {'k': 3}
# print(list(d.keys()))

def f(n):
    return n * f(n-1)

# re = f(3)
re = f(0)