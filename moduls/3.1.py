# Модулі datetime та time.

# import datetime
# now = datetime.datetime.now()
# print(now)

# 2024-06-12 18:26:16.204737

# from datetime import datetime

# current_datetime = datetime.now()

# print(current_datetime.year) # 2024
# print(current_datetime.month) # 6
# print(current_datetime.day) # 12
# print(current_datetime.hour) # 18
# print(current_datetime.minute) # 30
# print(current_datetime.second) # 12
# print(current_datetime.microsecond) # 276813
# print(current_datetime.tzinfo)

# print(current_datetime.now()) # 2024-06-12 18:57:19.673477

# print(current_datetime.date()) # 2024-06-12

# print(current_datetime.time()) # 20:33:59.388548

# datetime.datetime.combine(date_object, time_object)

# ==================================================
# import datetime

# # Створення об'єктів date і time
# date_part = datetime.date(2023, 12, 14)
# time_part = datetime.time(12, 30, 15)

# # Комбінування дати і часу в один об'єкт datetime
# combined_datetime = datetime.datetime.combine(date_part, time_part)

# print(combined_datetime)  # Виведе "2023-12-14 12:30:15"

# ==================================================

import datetime

# Створення об'єкта datetime з конкретною датою
specific_date = datetime.datetime(year=2020, month=1, day=7)

print(specific_date)  # Виведе "2020-01-07 00:00:00"
