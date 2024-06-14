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

# print(combined_datetime)  # "2023-12-14 12:30:15"

# ==================================================

# import datetime

# # Створення об'єкта datetime з конкретною датою
# specific_date = datetime.datetime(year=2024, month=1, day=7)

# print(specific_date)  #  "2024-01-07 00:00:00"

# ==================================================
# import datetime

# # Створення об'єкта datetime з конкретною датою і часом
# specific_datetime = datetime.datetime(2025, 1, 7, 14, 30, 15)

# print(specific_datetime)  #  "2025-01-07 14:30:15"

# ================================================== Метод weekday()
# from datetime import datetime

# # Створення об'єкта datetime
# now = datetime.now()

# # Отримання номера дня тижня
# day_of_week = now.weekday()

# # Поверне число від 0 (понеділок) до 6 (неділя)
# print(f"Сьогодні: {day_of_week}")   # 2

# ==================================================

# from datetime import datetime

# # datetime1 = datetime(2024, 6, 12, 22, 14)
# # datetime2 = datetime(2024, 6, 12, 23, 14)

# # print(datetime1 == datetime2) # False
# # print(datetime1 > datetime2) # False
# # print(datetime1 < datetime2) # True
# # print(datetime1 != datetime2) # True

# # ================================================== Ключові аспекти: методи роботи з датами і часом


# # ================================================== Робота з часовими проміжками timedelta
# from datetime import timedelta
# delta = timedelta(
#     days=10,
#     seconds=23,
#     microseconds=9,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )
# print(delta) # 24 days, 8:05:52.000009

# # Об'єкти timedelta можна створювати, щоб отримати дату/час віддалену від початкової.

# from datetime import datetime, timedelta

# now = datetime.now()
# future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
# print(future_date) # 2024-06-23 12:05:27.201545

# ================================================== Або від якоїсь конкретної дати.

# from datetime import datetime, timedelta

# seventh_day_2023 = datetime(year=2023, month=1, day=2, hour=14)
# four_weeks_interval = timedelta(weeks=4)

# print(seventh_day_2023 + four_weeks_interval)  # 2023-01-30 14:00:00
# print(seventh_day_2023 - four_weeks_interval)  # 2022-12-05 14:00:00



# ================================================== послідовность дат, наприклад, для визначення кількості днів між двома датами. toordinal()

# from datetime import datetime

# # Створення об'єкта datetime
# date = datetime(year=2024, month=12, day=18)

# # Отримання порядкового номера
# ordinal_number = date.toordinal()
# print(f"Порядковий номер дати {date} становить {ordinal_number}")

# Порядковий номер дати 2024-12-18 00:00:00 становить 739238

# ==================================================Робота з timestamp  для вказівки конкретного моменту в часі

# from datetime import datetime

# # Поточний час
# now = datetime.now()
# print(now) # 2024-06-13 12:46:32.147911

# # Конвертація datetime в timestamp
# timestamp = datetime.timestamp(now)
# print(timestamp)  # Виведе timestamp поточного часу 1718271992.147911

# ================================================== Парсинг дати із рядка
# datetime_object.strftime(format)

# format
# %Y - рік з чотирма цифрами (наприклад, 2023).
# %y - рік з двома цифрами (наприклад, 23).
# %m - місяць як номер (наприклад, 03 для березня).
# %d - день місяця як номер (наприклад, 14).
# %H - година (24-годинний формат) (наприклад, 15).
# %I - година (12-годинний формат) (наприклад, 03).
# %M - хвилини (наприклад, 05).
# %S - секунди (наприклад, 09).
# %A - повна назва дня тижня (наприклад, Tuesday).
# %a - скорочена назва дня тижня (наприклад, Tue).
# %B - повна назва місяця (наприклад, March).
# %b або %h - скорочена назва місяця (наприклад, Mar).
# %p - AM або PM для 12-годинного формату.

# from datetime import datetime

# now = datetime.now()

# # Форматування дати і часу
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S") 
# print(formatted_date) # 2024-06-13 13:01:29

# # Форматування лише дати
# formatted_date_only = now.strftime("%A, %d %B %Y")
# print(formatted_date_only) # Thursday, 13 June 2024

# # Форматування лише часу
# formatted_time_only = now.strftime("%I:%M %p")
# print(formatted_time_only) # 01:01 PM

# # Форматування лише дати
# formatted_date_only = now.strftime("%d.%m.%Y")
# print(formatted_date_only) # 13.06.2024

# ============================================= Метод strptime в Python використовується для перетворення рядків у об'єкти datetime.

# datetime_object = datetime.strptime(string, format)

# from datetime import datetime

# date_str = '2024.06.13'

# datetime_obj = datetime.strptime(date_str, "%Y.%m.%d")
# print(datetime_obj)

# 2024-06-13 00:00:00

# ============================================== Робота з ISO форматом дати

# Формат дати в ISO 8601 виглядає як "YYYY-MM-DD", де:

# YYYY - це рік (наприклад, 2023),
# MM - місяць (наприклад, 01 для січня),
# DD - день (наприклад, 31).

# Формат часу в ISO 8601 виглядає як "HH:MM:SS", де:



# HH - години (від 00 до 23),
# MM - хвилини (від 00 до 59),
# SS - секунди (від 00 до 59, іноді з додатковими десятковими частинами для мікросекунд).

# from datetime import datetime

# now = datetime.now()

# iso_format = now.isoformat()
# print(iso_format) # 2024-06-13T19:00:44.039331

# =============================================
# from datetime import datetime

# iso_date_string = "2023-03-14T12:39:29.992996"

# # Конвертація з ISO формату
# date_from_iso = datetime.fromisoformat(iso_date_string)
# print(date_from_iso) # 2023-03-14 12:39:29.992996

# =============================================
#isoweekday() - день тижня


# =============================================
#isocalendar() - д(ISO_рік, ISO_тиждень, ISO_день_тижня),

# from datetime import datetime

# # Створення об'єкта datetime
# now = datetime.now()

# # Отримання ISO календаря
# iso_calendar = now.isocalendar()

# print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")
# ISO рік: 2024, ISO тиждень: 24, ISO день тижня: 4

# ============================================= часові зони
# from datetime import datetime, timezone

# local_now = datetime.now()
# utc_now = datetime.now(timezone.utc)

# print(local_now) # 2024-06-13 19:10:34.288404
# print(utc_now)  # Виведе поточний час в UTC 2024-06-13 16:10:34.288408+00:00

a = int(input("Input 'a':  "))
b = int(input("Input 'b':  "))

print(-b / a)

