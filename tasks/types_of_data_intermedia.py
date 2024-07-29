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
    
    apples_per_student = apples // students
    balance = apples % students

    if round_down:
        if students == 1:
            return f'У нас тільки один студент, всі яблука залишиться у нього'
        elif balance == 0:  
            return f'Кожен з {students} студентів отримає по {apples_per_student} яблук(у), в кошику нічого не залишиться'
        elif apples >= students:
            return f'Кожен студент отримає по {apples_per_student} яблук(у), в кошику залишиться {balance} яблук(а/о)'
        else:
            return f'Занадто мало яблук для всіх студентів, немає що ділити, всі яблука в кількості {apples} штук в кошик'
    else:
        apples_per_student = math.ceil(apples / students)
        balance = apples - apples_per_student * students
        return f"Кожен з {students} студентів отримає {apples_per_student} яблук, в кошику залишиться {balance} яблук(а/о)."



students = int(input("Введіть кількість студентів: "))
apples = int(input("Скільки яблук є внаявності: "))

result = divide_apples(students, apples)
print(result)

