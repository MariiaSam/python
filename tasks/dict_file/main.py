
''''
Створіть словник зі списками добрих справ на сьогодні і на завтра. Надрукуйте із словника добрі справи, які плануєш зробити сьогодні і взавтра.

Вхідні дані:

Немає
Вихідні дані:

today:
Make a compliment to a friend
Call your grandparents
Embrace parents
tomorrow:
Feed the birds in the park
Give unnecessary things to those who need them
Smile

'''

import random
import json


def save_to_file(data, filename='good_deeds.json'):
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_from_file(filename='good_deeds.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


# Завантаження даних зі збереженого файлу (якщо існує)
good_works = load_from_file()

# Додавання нових добрих справ
good_works['today'] = ['Make a compliment to a friend',
                       'Call your grandparents', 'Embrace parents']
good_works['tomorrow'] = ['Feed the birds in the park',
                          'Give unnecessary things to those who need them', 'Smile']

# Вибір випадкової доброї справи на сьогодні
random_good_deed = random.choice(good_works['today'])
print(f"Сьогодні я зроблю: {random_good_deed}")

# Збереження оновлених даних
save_to_file(good_works)
