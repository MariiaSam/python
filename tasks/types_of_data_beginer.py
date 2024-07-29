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

# 4

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

# 5
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


# 6

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

# 7
'''Напишіть програму, яка зчитує довжину основи та висоту прямокутного трикутника (цілі числа), обчислює площу і друкує її значення на екрані у відформатованому вигляді (два символи після десяткової крапки). Кожен параметр вводиться на окремому рядку.

Вхідні дані:

3
4
Вихідні дані:

6.00
'''
# length_01 = int(input("Enter 1: "))
# length_02 = int(input("Enter 2: "))

# result = (length_01 * length_02) * 0.5
# print(f'{result:.2f}') # 6.00

# 8
'''
Напишіть програму, яка вітає користувача, виводячи слово Hello, введене ім’я і розділові знаки за зразком (дивитися приклади вхідних і вихідних даних). Програма повинна зчитувати в рядкову змінну значення і виводити відповідне вітання. Зверніть увагу, що після коми повинен обов’язково стояти пропуск, а перед знаком оклику пропуску немає. Операцією конкатенації (об’єднанням) рядків (+) користуватися не можна.

Вхідні дані:

Alex
Вихідні дані:

Hello, Alex!
'''

# name = input("Enter your name: ")
# print(f'Hello, {name}!')

# 9.
'''
Вводиться ціле невід’ємне число n (n ≤ 100). Виведіть 2n.

Вхідні дані:

10
12
5
Вихідні дані:

1024
4096
32
'''

# def number(n):
#     while n <=100:
#         print(2 ** n)
#         break


# result = number(10)
# result = number(12)
# result = number(5)

'''
1024
4096
32
'''

# 10.

'''
Дано двоцифрове число. Знайдіть число десятків у ньому.

Вхідні дані:

42
67
81
Вихідні дані:

4
6
8
'''

# def number(n):
#     print(n // 10)


# result = number(42)
# result = number(67)
# result = number(81)


'''
4
6
8
'''

# 11

'''
Напишіть програму для запису і розв’язування виразу (a + b) * (a + b), де a і b - натуральні цілі числа.

Вхідні дані:

4
3
Вихідні дані:

(4 + 3) * (4 + 3) = 49
'''

# a = 4
# b = 3

# print((a + b) * (a + b))

# 49

# import math

# a = 10 * 30.48

# b = 5 * 2.54
# print(math.ceil(a + b))

# 318


# 12

'''
Напишіть програму, щоб отримати ASCII значення введеного з клавіатури символа.

Вхідні дані:

G
w
+
Вихідні дані:

71
119
43
'''

# def ascii_num(numb):
#    total = ord(numb)
#    print(total)


# result = ascii_num('G')
# result = ascii_num('w')
# result = ascii_num('+')


'''
71
119
43
'''

# 13

'''

Користувач вводить значення чисел a і b з клавіатури. Напишіть програму для друку дії додавання і результату обчислення як у вихідних даних.

Вхідні дані:

30
20
Вихідні дані:

30 + 20 = 50
'''

# a = int(input('Enter 1: '))
# b = int(input('Enter 2: '))

# print(a + b) 

# 50

# 14.

'''
Напишіть програму, щоб конвертувати усі введені користувачем одиниці часу (дні, години, хвилини, секунди) в загальну кількість секунд.

Вхідні дані:

Days: 1
Hours: 16
Minutes: 25
Seconds: 50
Вихідні дані:

The amounts of seconds: 145550.
'''


# days = 1 * 24 * 60 * 60
# hours = (16 * 60) * 60
# minutes = 25 * 60
# seconds = 50

# total = days + hours + minutes + seconds
# print(total) 

# 145550

# 15.
'''
Вивести на екран три цілих числа в один рядок через пропуск у порядку, зворотному введенню чисел.

Вхідні дані:

4
12
-7
Вихідні дані:

-7 12 4'''

# a = 4
# b = 12
# c = -7

# d = f'{c} {b} {a}'
# print(d)

# -7 12 4

# def reverse_numbers(numbers):
#     if len(numbers) != 3:
#         raise ValueError("Please enter exactly 3 integers.")

#     reverse = numbers[: :-1]

#     print(*reverse, sep=' ')

# numbers = [int(input("Enter int: ")) for _ in range(3)]

# reverse_numbers(numbers)

'''
Enter int: 4
Enter int: 5
Enter int: 6
'''

'6 5 4'


# 16

'''
Напишіть програму для виведення такого повідомлення на екран: Points: 145, 67, 111. Довільні цілі числа вводить користувач з клавіатури і їх значення підставляються у повідомлення автоматично.

Вхідні дані:

145
67
111
Вихідні дані:

Points: 145, 67, 111.
'''

# def sentence_input(numbs):
#     if len(numbs) != 3:
#         raise ValueError("Please enter exactly 3 integers.")
    
#     numbs_str = [str(numb) for numb in numbs]

#     mess = "Points: " + ", ".join(numbs_str)  + '.'
#     print(mess)


# numbs = [int(input("Enter int: ")) for _ in range(3)]
# sentence_input(numbs)

'''
Enter int: 34
Enter int: 89
Enter int: 32
Points: 34, 89, 32.
'''

# 17

'''
Необхідно певну суму грошей залишити на банківському рахунку, щоб отримувати відсотки по закінченню певного часу. Наприклад, через 10 років ви хотіли б отримати 10 000 доларів США на власному рахунку. Скільки потрібно внести грошей на депозит сьогодні, щоб це сталося? Для розв’язування цієї задачі можна використовувати формулу 

p = f/(1+r)*n, де p - це поточна сума, яку потрібно внести сьогодні, 

f - майбутнє значення, яке ви хочете отримати (у нашому випадку становить 10 000 доларів США), 

r - річна відсоткова ставка, n - кількість років перебування грошей на рахунку.

Enter the desired future value: 10000
Enter the annual interest rate: 0.05
Enter the number of years the money will grow: 10

You will need to deposit this amount: 6139.13.
'''

'''def calc_initial_deposite(future_value, interest_rate, years):
    initial_deposite = future_value / (1 + interest_rate) * years
    return initial_deposite

future_value = float(input('Enter future_value: '))
interest_rate = float(input('Enter interest_rate: '))
years = int(input('Enter of years: '))


result = calc_initial_deposite(future_value, interest_rate, years)
print(f"Amount: {result:.2f}")'''

# 6139.13
# ** - піднесення до степеня Кожен рік сума збільшується на (1 + r) разів.
# n років: За n років сума збільшується на (1 + r) помножене на себе n разів, тобто (1 + r)^n.

# 18

'''
Вивести на екран три цілих числа в один рядок через пропуск у порядку, зворотному введенню чисел.

Вхідні дані:

4
12
-7
Вихідні дані:

-7 12 4

'''

# number_one = input("Enter 1 number: ")
# number_two = input("Enter 2 number: ")
# number_three = input("Enter 3 number: ")

# list_number = f'{number_three} {number_two} {number_one}'
# print(list_number) # -7 12 4

# def list_number(number_one, number_two, number_three):
#     return f'{number_three} {number_two} {number_one}'


# number_one = input("Enter 1 number: ") # 4
# number_two = input("Enter 2 number: ") # 12
# number_three = input("Enter 3 number: ") # -8

# result = list_number(number_one, number_two, number_three)
# print(result) # -8 12 4

#19

'''
Обчисліть n181 і виведіть на екран обчислене значення. Значення n - ціле число, яке вводиться з клавіатури.

Вхідні дані:

2
Вихідні дані:

3064991081731777716716694054300618367237478244367204352
'''

'''number = int(input("Enter int numb: "))

degree = number ** 181
print(degree)'''
# 3064991081731777716716694054300618367237478244367204352

# 20


'''
Цілі числа a і b вводяться користувачем. Напишіть програму для обчислення значення математичного виразу (45 + a - 11) / (b - 5)3.

Вхідні дані:

5
10
Вихідні дані:

0.312
'''

'''
def program(a, b):
    return (45 + a - 11) / (b - 5) ** 3

result = program(5, 10)
print(result)'''
# 0.312

# 21

'''
Напишіть програму, яка обчислює суму, різницю, добуток, частку двох чисел, піднесення до степеня, розділяючи результати, записані в один рядок, символом &.

Вхідні дані:

6
3
Вихідні дані:

9&3&18&2.0&216

'''

# def program(a, b):
#     add = a + b
#     minus = a - b
#     mult = a * b
#     dividing = a / b
#     degree = a ** b

#     return f'{add}&{minus}&{mult}&{dividing}&{degree}'


# result = program(6, 3)
# print(result)

# 9&3&18&2.0&216

# 21 

'''
Припускаючи, що немає затримок, відстань, яку автомобіль долає, можна розрахувати за такою формулою: Відстань = Швидкість · Час. Значення швидкості автомобіля вводиться користувачем з клавіатури (у км/год). Напишіть програму, яка виведе на екран значення відстані у кілометрах, яку пройде автомобіль через 6, 10, 15 годин відповідно.

Вхідні дані:

70
Вихідні дані:

420
700
1050
'''

'''def distances(speed, hours):
    return speed * hours 
    

result1 = distances(70, 6)
result2 = distances(70, 10)
result3 = distances(70, 15)

print(result1) # 420
print(result2) # 700
print(result3) # 1050'''

# 21

'''
Обчисліть, скільки коштуватиме певний товар в магазині, якщо діє знижка на нього. Значення ціни товару і відсоток знижки вводяться в окремих рядках користувачем з клавіатури.

Вхідні дані:

150
0.3
Вихідні дані:

105.0
'''

# def price_sale(full_price, percent):
#     return full_price * (1 - percent)

# full_price = (int(input("Enter full price: ")))
# percent = (float(input("Enter percent: ")))

# result = price_sale(full_price, percent)
# print(result)
# 150

# 21

'''
Напишіть програму, яка зчитує три цілих числа і виводить найбільше значення з них. Не можна користуватися розгалуженнями і циклами.

Вхідні дані:

12
-2
54
Вихідні дані:

54
-2
'''

'''numb1 = int(input("Enter numb 1: "))
numb2 = int(input("Enter numb 2: "))
numb3 = int(input("Enter numb 3: "))

max_numb = max(numb1, numb2, numb3)
print(max_numb)'''
# 54

# 22

'''
Сашко, зазвичай, спить вночі a годин і влаштовує собі вдень тиху годину на b хвилин. Визначте, скільки всього хвилин Сашко спить на добу.

Вхідні дані:

8
45
Вихідні дані:

525
'''

# sleep_night = 8 * 60
# sleep_day = 45

# print(sleep_night + sleep_day)
# 525

# 23

'''

'''



# def split_bill(total_bill):

#   tip = total_bill * 0.1

#   total_with_tip = total_bill + tip

#   amount_per_person = total_with_tip / 3

#   return amount_per_person

# bill = float(input("Введіть суму рахунку: "))

# result = split_bill(bill)
# print("Кожен з друзів повинен заплатити:", result)

# 24

'''
В магазині канцелярських товарів Дарина купила a олівців, b ручок та c фломастерів. Відомо, що ціна ручки на 2 гривні більша ціни на олівець і на 7 гривень менша ціни на фломастера. Так само відомо, що вартість олівця становить d гривень. Користувачем вводяться по порядку в окремих рядках кількість олівців, ручок, фломастерів і ціна одного олівця. Необхідно обчислити загальну вартість покупки.

Вхідні дані:

1
2
2
3
Вихідні дані:

37
'''

