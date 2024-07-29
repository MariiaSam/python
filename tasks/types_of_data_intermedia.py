# 1
'''
n студентів беруть k яблук і розподіляють між собою порівну. Решта фруктів залишається в кошику. Скільки яблук отримає кожен студент? Скільки яблук залишиться в кошику? Програма зчитує числа n і k і друкує на екрані дві відповіді на поставлені вище запитання.

Вхідні дані:

6
50
Вихідні дані:

8
2
Розділ: ЗМІННІ І ТИПИ ДАНИХ | Рівень складності: СЕРЕДНІЙ
'''


import math

def divide_apples(students, apples, round_down=True):
    if apples == 0:
        return "Яблук немає, ніхто нічого не отримає."
    if students == 0:
       return "Немає студентів, кому роздати яблука."
    
    # apple_per_student = apples // students
    balance = apples % students

    if round_down:
        if students == 1:
            return f'У нас тільки один студент, всі яблука, тобто {apples} штук, залишиться у нього'
        else:
            return f'У нас меньше яблук, які можна порівну поділити між студентами, в кошику залишиться всі {balance} яблук(а/о)'
    else:
        apples_per_student = math.ceil(apples / students)
        balance = apples - apples_per_student * students
        return f"Кожен з {students} студентів отримає {apples_per_student} яблук, в кошику залишиться {balance} яблук(а/о)."



students = int(input("Введіть кількість студентів: "))
apples = int(input("Скільки яблук є внаявності: "))

result = divide_apples(students, apples)
print(result)

