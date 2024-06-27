# from pathlib import Path

# parent_folder_path = Path('.')

# def parse_folder(path):
#     for element in path.iterdir(): # шнтерактивно проходим по директорії
#         if element.is_dir(): # якщо елемент є папкою
#             print(f"Parse folder: This is folder - {element.name}")
#             # parse_folder(element)
#         if element.is_file():
#             print(f"Parse folder: This is file - {element.name}")

# parse_folder(parent_folder_path)
#=========================================

# from pathlib import Path

# file_name = Path('./Temp')

# try:
#     file = open(file_name / 'jokes.txt', 'r', encoding='utf-8')
#     try:
#         while True:
#             line = file.readline()
#             if not line:
#                 break
#             print(line, end='')
#     except OSError:
#         print('Error while reading file')
#     finally:
#         file.close()
# except OSError:
#     print('OSError')

#=========================================
# from pathlib import Path

# file_name = Path('./Temp')

# try:
#     with open(file_name / 'jokes.txt', 'r', encoding='utf-8') as file:
#         for line in file:
#             print(line, end='')

# except Exception as e:
#     print(f'{e} with file')

#=========================================


# from pathlib import Path

# file_name = Path('.')

# for elem in file_name.glob('*.py'):
#     print(elem)

# for elem in file_name.glob('*.txt'):
#     print(elem)

# for elem in file_name.glob('*txt*'):
#     print(elem)

# for elem in file_name.glob('*/'):
#     print(elem)

# for elem in file_name.glob('test*'):
#     print(elem)
#========================================= Видалення

# from pathlib import Path

# file_name = Path('./Temp/jokes.txt')

# try:
#     file_name.unlink()
# except FileNotFoundError:
#     pass

# file_name.unlink(missing_ok=True)

#========================================= Створення директорії

from pathlib import Path

new_dir = Path('ABC')

if not new_dir.exists():
    new_dir.mkdir()

new_dir.mkdir(exist_ok=True)
#========================================= 

#========================================= 

#========================================= 


#========================================= 