# 1.Напишіть програму, яка отримує три цілих числа, введені з клавіатури (кожне число вводиться на окремому рядку), і друкує на екрані їх суму, добуток, результат піднесення першого числа до степеня різниці другого і третього чисел.

# Вхідні дані:

# 2
# 3
# 6


# Вихідні дані:

# 11
# 36
# 0.125

# first_numb = int(2)
# second_numb = int(3)
# third_numb = int(6)

# print(first_numb)
# print(second_numb)
# print(third_numb)

# total_sum = first_numb + second_numb + third_numb

# print(total_sum) # 11

# total_mult = first_numb * second_numb * third_numb
# print(total_mult) # 36

# diff = (second_numb - third_numb)
# total_diff = first_numb ** diff
# print(total_diff)

# ==================================================

# 2. Напишіть програму, яка приймає ціле число n і обчислює значення виразу n + nn + nnn.

# Вхідні дані:

# 5
# 3
# 1

# Вихідні дані:

# 615
# 369
# 123

# first_numb = int(5)
# second_numb = int(3)
# third_numb = int(1)

# 5 + 55 + 555 = 615

# nn_numb = str(first_numb)+str(first_numb)
# nnn_numb = str(first_numb)+str(first_numb) + str(first_numb)
# print(nn_numb) # 55
# print(nnn_numb) #555

# result = first_numb + int(nn_numb) + int(nnn_numb)
# print(result) # 615

# ==================================================

# 3. Напишіть програму, яка отримує такі дані: ім’я, вік, хобі, введені з клавіатури (вводяться на окремих рядках), і друкує на екрані одним повідомленням повну інформацію на основі введених даних.

# Вхідні дані:

# Lord Voldemort
# 72
# Magic
# Вихідні дані:

# My name is Lord Voldemort. I am 72 and my hobby is Magic.

# name = "Lord Voldemort"
# age = 72
# hobby = "Magic"

# str = "My name is " + name + ". I am " + str(int(age)) + " and my " + "hobby is " + hobby
# print(str)

# ==================================================


# 4. Напишіть програму, яка зчитує довжину основи та висоту прямокутного трикутника (цілі числа), обчислює площу і друкує її значення на екрані у відформатованому вигляді (два символи після десяткової крапки). Кожен параметр вводиться на окремому рядку.

# Вхідні дані:

# 3
# 4
# Вихідні дані:

# 6.00

# length = int(3)
# print(length)

# heigth = int(4)
# print(heigth)

# total = 0.50 * length * heigth
# print(f"{total:.2f}")

# ==================================================


# Встановлюємо ціни на продукти
# price_per_croissant = 1.04
# price_per_glass = 0.34
# price_per_coffee_pack = 4.42

# Кількість кожного продукту
# num_croissants = int(input("Введіть кількість круасанів: "))
# num_glasses = int(input("Введіть кількість склянок: "))
# num_coffee_packs = int(input("Введіть кількість упаковок кави: "))

# Обчислення загальної вартості
# total_cost = num_croissants * price_per_croissant + \
#              num_glasses * price_per_glass + \
#              num_coffee_packs * price_per_coffee_pack

# Визначаємо кількість повних доларів і центів
# total_dollars = int(total_cost)
# total_cents = int(total_cost * 100)

# Вивід результату
# print(f"Загальна вартість у повних доларах: {total_dollars} доларів")
# print(f"Загальна вартість у центах: {total_cents} центів")


# ==================================================
# 5. Напишіть програму, яка зчитує ціле число, і друкує попереднє та наступне числа відносно введеного.

# Вхідні дані:

# 179
# Вихідні дані:

# The next number for the number 179 is 180.
# The previous number for the number 179 is 178.

# num = 179
# print(type(num))

# print(f"The next number for the number {num} is {num + 1}.") # The next number for the number 179 is 180.
# print(f"The previous number for the number {num} is {num - 1}.") # The previous number for the number 179 is 178.

# ==================================================
# 6. Вводиться ціле додатне число. Надрукуйте останню цифру числа.

# Вхідні дані:

# 179
# 40
# 101
# Вихідні дані:

# 9
# 0
# 1

# def last_digit(n):
#     return n % 10

# print(last_digit(179))  # 9
# print(last_digit(40))   # 0
# print(last_digit(101))  # 1


# ==================================================
# 7.1. Виконай попереднє завдання за допомогою метода format.
# Зразок виконання:

# f_name = input('Введіть ім\'я: ')

# s_name = input('Введіть прізвище: ')

# print('Мене звуть {} {}. Я з України.'.format(f_name, s_name))

# f_name = input('Введіть ім\'я: ')

# s_name = input('Введіть прізвище: ')

# print(f'Мене звуть {f_name} {s_name}. Я з України.')

# ==================================================
# 7.2. Перетвори речення у багаторядкову стрічку та виведи його:
# "Інформатика — теоретична та прикладна дисципліна, що вивчає структуру і загальні властивості інформації, а також методи і (технічні) засоби її створення, перетворення, зберігання, передачі та використання в різних галузях людської діяльності. "

# sentence = '''Інформатика — теоретична та прикладна дисципліна, що вивчає структуру і загальні властивості інформації, а також методи і (технічні) засоби її створення, перетворення, зберігання, передачі та використання в різних галузях людської діяльності.'''
# print(sentence)

# ==================================================
# 7.3. Склади програму, яка виводить на екран словосполучення "Computer Science" 10 разів.

# print('Computer Science'  * 10)

# ==================================================
# 7.4. Використовуючи функцію split, розбий стрічку "Computer Science" через пробіли. В результаті повинен вийти список слів.

# sentence = 'Computer Sciense'

# print(sentence.split(" "))

# ==================================================
# 8.1 Ввести з клавіатури слово. Перетворити його в список.
# a = input("Введи слово: ")

# print(list(a)) # ['M', 'a', 'r', 'i', 'i', 'a']

# word_list = [a]
# print(word_list) # ['Mariia']

# ==================================================
# 8.2. Склади список улюблених хобі і дай йому назву змінної hobbies. Склади список своїх улюблених страв і назви цю змінну food. Об’єднай два списки й назви результат favourite. Виведи цю змінну.

# hobbies = ['read', 'code', 'swim']
# food = ['water', 'avocado', 'meat']

# favourite = hobbies + food

# print(favourite) # ['read', 'code', 'swim', 'water', 'avocado', 'meat']

# ==================================================
# 8.3. 3. Створи список, що складається з усіх цифр у порядку зростання. Використай функцію, що змінює порядок елементів списку на зворотній та виведи отриманий список. Обчисли кількість елементів у списку.

# num_list = [1, 2, 3, 4, 7, 9, 13, 14, 16]
# num_list.reverse()
# print(num_list) # [16, 14, 13, 9, 7, 4, 3, 2, 1]

# print(len(num_list)) # 9

# ==================================================
# 8.4. Склади список із букв українського алфавіту. За допомогою функції del видали усі голосні літери.
# alphabet = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л',
#             'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ',  'ь',  'ю', 'я']

# vowels = ['а', 'е', 'є', 'и', 'і', 'ї', 'о', 'у', 'ю', 'я']

# for vowel in vowels:
#     while vowel in alphabet:
#         del alphabet[alphabet.index(vowel)]

# print(alphabet) # ['б', 'в', 'г', 'ґ', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь']

# ==================================================
# 8.5. Створи список із п'яти випадкових чисел з діапазону від 0 до 100. Для цього скористайся функцією sample з модуля random.

# import random

# print(random.sample(range(100), 5))  # [56, 54, 26, 90, 66]

# ================================================== Словники Dictionary
# 9.1.1 Створи словник, у якому ключами є країни, а елементами – міста, що належать відповідній країні. 
# 2 Виведи міста другої по рахунку країни у словнику.
# 3 Виведи усі країни.
# 4 Створи словник з ключем "Данія" і значенням "Копенгаген" та додай його до попереднього словника.


# # 1.
# country = {'Ukrine': "Kyiv",'Italy': ['Roma', 'Milan', 'Neapol' ], 'Spain': 'Madrid'}

# print(type(country)) # <class 'dict'>
# print(country) # {'Ukrine': 'Kyiv', 'Italy': 'Roma', 'Spain': 'Madrid'}

# # 2.
# print(country["Italy"]) # ['Roma', 'Milan', 'Neapol']

# # 3
# print(country.keys()) # (['Ukrine', 'Italy', 'Spain'])

# new_country = {"Denmark": "Copenhagen"}

# country.update(new_country)
# print(country) # {'Ukrine': 'Kyiv', 'Italy': ['Roma', 'Milan', 'Neapol'], 'Spain': 'Madrid', 'Denmark': 'Copenhagen'}

# ==================================================
# 9.2 Створити словник, де ключ – прізвище учня, а значення ключа – список з його оцінок. В учнів може бути різна кількість оцінок. 
# Виведи тільки прізвища учнів. 
# Порахуй середній бал для кожного учня.
# Створи словник з прізвищами учнів та їх середніми балами і виведи його на екран.

# marks = {"Lev": [10, 11, 12], "Anna": [9, 8, 6], "Oleg": [10, 12, 6]}
# print(marks.keys()) # (['Lev', 'Anna', 'Oleg'])

# mark_Lev = sum(marks["Lev"]) // len(marks["Lev"])  # 11
# print(mark_Lev)

# mark_Anna = sum(marks["Anna"]) // len(marks["Anna"])  # 7
# print(mark_Anna)

# mark_Oleg = sum(marks["Oleg"]) // len(marks["Oleg"])  # 9
# print(mark_Oleg)

# average_marks = {}
# for student, grades in marks.items():
#     average_marks[student] = sum(grades) // len(grades)
# print(average_marks)  # {'Lev': 11, 'Anna': 7, 'Oleg': 9}

# OR 2 var
# average_students = {"Lev": mark_Lev, "Anna": mark_Anna, "Oleg": mark_Oleg }
# print(average_students) #{'Lev': 11, 'Anna': 7, 'Oleg': 9}


# text = 'Hello World'
# shift = 3
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# index = alphabet.find(text[0].lower()) #  шукає індекс символу 'h' у рядку alphabet.
# print(index)
# shifted = alphabet[index] # знаходить символ в alphabet за індексом index.
# print(shifted)


# ==============================
# 9.

# Виводить "Fizz", якщо число кратне якомусь певному числу (наприклад, 3);
# Виводить "Buzz", якщо число кратне іншому певному числу (наприклад, 5);
# Виводить "FizzBuzz", якщо число кратне обом цим числам;
# В іншому випадку виводить саме число.



# ==============================
# 10.

# Розглянемо наступну задачу. Користувач вводить рядок. Треба порахувати скільки символів в рядку та скільки пробілів в рядку. Як ми можемо написати код?# # Зчитування рядка від користувача


# user_input = input("Введіть рядок: ")

# # Ініціалізація змінних для підрахунку символів та пробілів
# total_chars = len(user_input)  # загальна кількість символів у рядку
# space_count = 0  # кількість пробілів

# Підрахунок кількості пробілів
# for char in user_input:
#     if char == " ":
#         space_count += 1

# Виведення результатів
# print(f"Загальна кількість символів у рядку: {total_chars}")
# print(f"Кількість пробілів у рядку: {space_count}")


# ==============================    FUNCTION
# 11. конвертувати кожен символ у рядку в його відповідний код ASCII.

# def string_to_codes(string: str) -> dict:
#     codes = {}
#     for ch in string:
#         if ch not in codes:
#             codes[ch] = ord(ch)
#     return codes

# result = string_to_codes("Hello world!")
# print(result)
# {'H': 72, 'e': 101, 'l': 108, 'o': 111, ' ': 32, 'w': 119, 'r': 114, 'd': 100, '!': 33}

# ==============================    
 # 12. Необхідно створити функцію для розрахунку вартості товарів з урахуванням можливої знижки.
# Для розрахунку реальної ціни з врахуванням дисконту створимо функцію real_cost. Функція real_cost повинна приймати два аргументи: базову ціну товару base та розмір знижки discount, який за замовчуванням будемо вважати 0. Вона повинна повертати вартість товару після застосування знижки.

# def real_cost(base, discount: float = 0) -> float:
#     return base * (1 - discount) # Якщо знижка відсутня, то використовується лише базова ціна

# price_bread = 15 # завжди без знижки
# price_butter = 50 # застосовуємо знижки 5%
# price_sugar = 60 # застосовуємо знижки 7%

# current_price_bread = real_cost(price_bread)
# current_price_butter = real_cost(price_butter, 0.05)
# current_price_sugar = real_cost(price_sugar, 0.07)

# print(f'Нова вартість хліба: {current_price_bread}') # 15
# print(f'Нова вартість масла: {current_price_butter}') # 47.5
# print(f'Нова вартість цукру: {current_price_sugar}') # 55.8

# =================================
# Ми проводимо розіграш призів серед перших 50 підписників ютуб-каналу. Ми маємо 7 призів для розіграшу. Може виникнути питання, скільки різних списків переможців ми можемо отримати під час розіграшу? Для цього ми будемо використовувати формулу сполучень без повторень

# Cnk = n! / ((n - k)! · k!)

# де n — це загальна кількість людей (випадків), а k — кількість людей, які отримали призи.

# Напишіть функцію number_of_groups, яка приймає параметри n та k, і за допомогою функції factorial повертає нам скільки різних списків переможців ми можемо отримати при розіграші

# Задачі:

# Створіть функцію number_of_groups, яка приймає два аргументи: n - загальна кількість людей та k - кількість переможців.
# У функції number_of_groups, використовуйте функцію factorial для обчислення факторіалів відповідно до формули сполучень: Cnk = n! / ((n - k)! · k!).
# Обчислення здійснюється шляхом виклику функції factorial для отримання факторіалів n, n - k та k.
# Поверніть результат цього обчислення.
# Очікуваний результат:

# Функція number_of_groups повертає кількість можливих різних списків переможців.

# Зверніть увагу на те, які великі значення ми отримуємо для факторіала. Рекурсивні висловлювання треба завжди застосовувати з обережністю при обчисленнях, щоб не отримати переповнення пам'яті.

# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n - 1)


# def number_of_groups(n, k):
#     return factorial(n) // (factorial(n - k) * factorial(k))

    
# 13.  скільки пройшло повних днів, коли Наполеон спалив Москву, а це відбулося 14 вересня 1812 року   
    
# from datetime import datetime

# # Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
# napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# # Поточна дата
# current_date = datetime.now()

# # Розрахунок кількості днів
# days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
# print(days_since)

# 77339

# [================================================] Osadchuk

# Скласти програму обчислення суми модулів трьох дійсних чисел

# value_one = 5
# value_two = 7
# value_three = -19

# """
# 57 -> 57
# -99 -> 99
# """

# summary = 0
# summary += abs(value_one)
# print(summary) # 5
# summary += abs(value_two)
# print(summary) # 12
# summary += abs(value_three)
# print(summary) # 31

#№[================================================] Osadchuk
# Скласти програму визначення номера під'їзду та поверху квартири за заданим номером квартири. У будинку 5 поверхів і 4 квартири на поверсі.
 
# FLOOR = 5
# APARTMENTS_PER_FLOOR = 4

# apartent_number = int(input('Введіть номер квартири: '))
# apartents_per_entrance = FLOOR * APARTMENTS_PER_FLOOR # кіл-сть кв в підʼїзді
# entrance_number = (apartent_number - 1) // apartents_per_entrance + 1 # який підʼїзд
# print(entrance_number)
# floor_number = ((apartent_number - 1) % apartents_per_entrance) // APARTMENTS_PER_FLOOR + 1 
# print(floor_number)

#№[================================================] M. Chernyshov
# Зчитати числа із консолі через кому, вивесту суму

# numbers_str = input("Enter numbers: ")
# numbers_list = numbers_str.split(",")
# numbers_int = list(map(int, numbers_list))

# print("numbers_str", numbers_str)
# print("numbers_list", numbers_list)
# print("numbers_int", numbers_int)
# print(type(numbers_int)) # <class 'list'>
# print(type(sum(numbers_int))) # <class 'int'>

##№[================================================] Osadchuk 
# Перевірка паролю для пропуску на сайт

# entry = input("Enter password: ")

# if entry is 'test2024':
#     print('Access Granted')
# else:
#     print('Access Denied') # IS !!!!! не однакові комірки памʼяті

# if entry == 'test2024':
#     print('Access Granted')
# else:
#     print('Access Denied')
##№[================================================] Osadchuk 

# Перевірка балансу для здійснення покупки

balance = 0.7 + 0.6
print(balance)
if round(balance, 1) == 1.3:
    print('Enough')
else:
    print('Not Enough')
print(round(balance, 1))