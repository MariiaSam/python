# 1 TASK

'''
У Харкові відкривають у бомбосховищі школу для молодших школярів.
Треба  обладнати три кімнати партами. Парта  - на дві людини.
Програмі подається на вхід три числа (трьома input)  - кількість учнів в кожному
класі. Програма має порахувати необхідну кількість парт загалом.
20 21 22  -> 32
26 20 16 -> 31
25 21 23 -> 36
17 19 18 -> 28
'''


# pupil_1 = int(input("Введіть кількість учнів в 1 класі: "))
# pupil_2 = int(input("Введіть кількість учнів в 2 класі: "))
# pupil_3 = int(input("Введіть кількість учнів в 3 класі: "))

# total_1 = (pupil_1 // 2) + pupil_1 % 2
# total_2 = (pupil_2 // 2) + pupil_2 % 2
# total_3 = (pupil_3 // 2) + pupil_3 % 2

# total = total_1 + total_2 + total_3
# print(total_1)

# 2 TASK
'''
З початку доби пройшло n хвилин. Програма приймає це число input-ом.
Який час буде показувати електроне табло годинника ?
Програма має вивести два числа - години (від 0 до 23), та
хвилини (від 0 до 59).
150 -> 2 30
1441 -> 0 1
444 -> 7 24
180 -> 3 0
1439 -> 23 59
1400 -> 0 0
'''

# minuts = int(input("Кількість хв з початку доби: "))

# hours = minuts // 60 % 24
# print(hours)

# hours_min = minuts % 60
# print(hours_min)

# 3 TASK
'''
дано дійсне число. Виведіть його першу цифру після крапки.
'''
# number = float(input("Дійсне число: "))

# first_part = number - int(number)
# first_digit = int(first_part * 10)
# print(first_digit)

# 4 Task
'''
Плюсиками намалювати  такий трикутник
  +
  +++
  +++++
  +++++++
  +++++++++
'''

# for i in range(1, 6):
#     print((i * 2 - 1) * "+")

# 5 Task
'''
          +
        +++
      +++++
    +++++++
  +++++++++
'''
# for i in range(1, 6):
#     print(' ' * (9 - i * 2 + 1) + (i * 2 - 1) * "+")

# 6 Task

# list = [1, [3,  5], 7, 29]

# def suma(list):
#     count = 0
#     for el in list:
#         if isinstance(el, int):
#             count += el        
#         else:
#             count += sum(el)
#     return count
# print(suma(list))
# 45

# list = [1, [3,  5, [6, 1]], 7, 29]

# def suma(list):
#     count = 0
#     for el in list:
#         if isinstance(el, int):
#             count += el
#         else:
#             count += suma(el)
#     return count
# print(suma(list))
 
