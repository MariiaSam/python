# import csv

# # Відкриваємо CSV файл
# with open("data.csv", newline="", encoding="utf-8") as csvfile:
#     # Створюємо об'єкт reader
#     reader = csv.reader(csvfile, delimiter=",")
#     # Проходимося по кожному рядку у файлі
#     for row in reader:
#         print(", ".join(row))

#===============================================
# import csv

# # Дані для запису
# rows = [
#     ["name", "age", "specialty"],
#     ["Василь Гупало", 30, "Математика"],
#     ["Марія Петренко", 22, "Фізика"],
#     ["Олександр Коваленко", 20, "Інформатика"],
# ]

# # Відкриваємо файл для запису
# with open("data2.csv", "w", newline="", encoding="utf-8") as csvfile:
#     # Створюємо об'єкт writer
#     writer = csv.writer(csvfile, delimiter=",")
#     # Записуємо рядки даних
#     writer.writerows(rows)

#===============================================

import csv

FILENAME = "users.csv"

users = [
    {"name": "Микола", "age": 22, "gender": "male"},
    {"name": "Марія", "age": 22, "gender": "female"},
    {"name": "Назар", "age": 22, "gender": "male"},
]

with open(FILENAME, "w", encoding="utf-8", newline="") as f:
    columns = users[0].keys()
    writer = csv.DictWriter(f, delimiter=",", fieldnames=columns)
    writer.writeheader()
    for row in users:
        writer.writerow(row)

with open(FILENAME, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)
