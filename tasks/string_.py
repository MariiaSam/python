'''
Напишіть програму, яка приймає послідовність рядків (порожній рядок для завершення програми) як вхідний рядок і друкує рядки у верхньому регістрі.

Вхідні дані:

python
ruby
go
 
Вихідні дані:

PYTHON
RUBY
GO

'''

while True:
    text = input("Введіть рядок, порожній рядок для завершення: ")
    if not text:
        break
    print(text.upper())
