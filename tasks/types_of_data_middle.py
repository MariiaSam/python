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


# import math

# def divide_apples(students, apples, round_down=True):
#     if apples == 0:
#         return "There are no apples, no one will get anything."
#     if students == 0:
#        return "No students to distribute apples to."
    
#     apples_per_student = apples // students
#     balance = apples % students

#     if round_down:
#         if students == 1:
#             return f'We have only one student, and he will have all apples'
#         elif balance == 0:  
#             return f'Each of {students} students will receive {apples_per_student} apples, nothing will remain in the basket'
#         elif apples >= students:
#             return f'Each of students will receive {apples_per_student} apples, and there will be {balance} apples in the basket'
#         else:
#             return f'There are too few apples for all students, there is nothing to share, all apples in the amount of {apples} pieces in the basket'
#     else:
#         apples_per_student = math.ceil(apples / students)
#         balance = apples - apples_per_student * students
#         return f"Each of {students} students will receive {apples_per_student} apples, and the basket will have {balance} apples."


# while True:
#     try:
#         students = int(input("Enter the number of students: "))
#         if students < 0:
#             print("The number of students cannot be negative. Try again")
#             continue
#         break 
#     except ValueError:
#         print("You have entered a number that is not a number. Try again.")

# while True:
#     try:
#         apples = int(input("How many apples are available: "))
#         if apples < 0:
#             print("The number of apples cannot be negative. Try again.")
#             continue
#         break
#     except ValueError:
#         print("You have entered a number that is not a number. Try again.")

# result = divide_apples(students, apples)
# print(result)

#=================================================

from math import floor

def distribute_apples_beetween_student(students: int, apples: int) -> tuple[int, int]:
    if students <= 0:
        raise ValueError("Students cannot be negative or 0")
    
    if apples <= 0:
        raise ValueError("Apples cannot be negative or 0")
    
    apples_per_student: int = floor(apples / students)
    leftover_apples: int = apples - (apples_per_student * students)

    return apples_per_student, leftover_apples

if __name__ == '__main__':
    def _test_distribute_and_print_result(students: int, apples: int) -> None:
        try:
            apples_per_student, leftover_apples = distribute_apples_beetween_student(students, apples)

            print(f'students: {students}, apples: {apples}, apples_per_student: {apples_per_student}, leftover_apples: {leftover_apples}')
        except ValueError as value_error:
            print(f'students: {students}, apples: {apples}, error: {value_error}')

    _test_distribute_and_print_result(3, 10)
    _test_distribute_and_print_result(3, 1)
    _test_distribute_and_print_result(3, 0)
    _test_distribute_and_print_result(0, 3)
    _test_distribute_and_print_result(6, 50)
    _test_distribute_and_print_result(-1, 50)
    _test_distribute_and_print_result(3, -50)