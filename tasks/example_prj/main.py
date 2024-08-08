'''Ви працюєте з набором даних, який представляє собою температурні показники за кожен день протягом одного місяця. Дані зберігаються у текстовому файлі, де кожен рядок відповідає одному дню. Якщо температура за день не фіксувалася, відповідний рядок у файлі залишається порожнім.


Необхідно обчислити мінімальну, максимальну, середню температуру та медіану для вказаного набору даних.
'''
from data import load_data, clean_data
from processing import calculate_statistics


def main():
    filename = "temperatures.txt"
    raw_data = load_data(filename)
    temperatures = clean_data(raw_data)
    stats = calculate_statistics(temperatures)

    if stats:
        print(f"Minimum Temperature: {stats['min']}°C")
        print(f"Maximum Temperature: {stats['max']}°C")
        print(f"Average Temperature: {stats['average']:.2f}°C")
        print(f"Median Temperature: {stats['median']:.2f}°C")
    else:
        print("No temperature data available.")


if __name__ == "__main__":
    main()
