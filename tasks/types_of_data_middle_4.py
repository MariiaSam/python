'''
Тетяна кожен день лягає спати рівно опівночі і нещодавно дізналась, що оптимальний час для її сну становить t хвилин. Тетяна хоче поставити собі будильник так, щоб він продзвенів рівно через t хвилин після півночі, однак для цього необхідно вказати час сигналу у форматі години і хвилини. Допоможіть Тані визначити, на який час завести будильник. Години і хвилини у виведенні програми повинні розташовуватися на різних рядках.

Вхідні дані:

450
Вихідні дані:

7
30
Розділ: ЗМІННІ І ТИПИ ДАНИХ | Рівень складності: СЕРЕДНІЙ
'''

def comfort_time(minutes: int) -> int:
     comfort_hours = minutes // 60
     comfort_minutes = minutes % 60

     return comfort_hours, comfort_minutes


if __name__ == '__main__':
    def __comfort_time_result(minutes: int) -> None:
        try:
            comfort_hours, comfort_minutes = comfort_time(minutes)

            print(f'A comfortable time to sleep for Tetiana is {comfort_hours} hours and {comfort_minutes} minutes')
            print(f'hours: {comfort_hours}')
            print(f'minutes: {comfort_minutes}')


        except ValueError as value_error:
            print(f'hours: {comfort_hours}, minutes: {comfort_minutes}, error: {value_error}')

    __comfort_time_result(450)
    __comfort_time_result(325)
    __comfort_time_result(100)
    __comfort_time_result(480)

'''
A comfortable time to sleep for Tetiana are 7 hours and 30 minutes
hours: 7
minutes: 30
A comfortable time to sleep for Tetiana are 5 hours and 25 minutes
hours: 5
minutes: 25
A comfortable time to sleep for Tetiana are 1 hours and 40 minutes
hours: 1
minutes: 40
A comfortable time to sleep for Tetiana are 8 hours and 0 minutes
hours: 8
minutes: 0
'''


# 2

'''
Книга коштує a гривень і b копійок. Визначте, скільки гривень і копійок потрібно заплатити за n книг. Значення вводяться користувачем у порядку a, b, n на окремих рядках, а сума до сплати в одному рядку через пропуск: кількість гривень і копійок відповідно.

Вхідні дані:

10
15
2
Вихідні дані:

20 30
Розділ: ЗМІННІ І ТИПИ ДАНИХ | Рівень складності: СЕРЕДНІЙ

'''

whole_bill = int(input("Enter whole_bill: "))
penny = int(input("Enter penny: "))
count_books = int(input("Enter count: "))

total_in_penny = (whole_bill * 100 + penny) * count_books

total_whole_bill = total_in_penny // 100
total_penny = total_in_penny % 100

print(total_whole_bill, total_penny)
