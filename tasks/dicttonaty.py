'''Створіть словник, у якому ключі - імена відомих програмістів, а значення - їхні дати народження у форматі dd/mm/yyyy. Напишіть програму, яка за введеним ім’ям відомого інформатика друкує його дату народження або у відсутності такого - відповідне повідомлення як у вихідних даних.

Вхідні дані:

Ada Lovelace
Jack Dorsey
Вихідні дані:

Ada Lovelace's birthday is 10/12/1815.
Sadly, we don't have Jack Dorsey's birthday.
'''

programmers = {
    "Ada Lovelace": "10/12/1815",
    "Alan Turing": "23/06/1912",
    "Grace Hopper": "09/12/1906",
}


def find_birthday(name):

    if name in programmers:
        return f"{name}'s birthday is {programmers[name]}."
    else:
        return f"Sadly, we don't have {name}'s birthday."


name = input("Enter the name of a famous programmer: ")

print(find_birthday(name))  # Ada Lovelace's birthday is 10/12/1815
