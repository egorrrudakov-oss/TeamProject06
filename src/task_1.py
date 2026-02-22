import os

full_name = input('Enter the full name of the patient separated by space (Ivanov Ivan Ivanovich): ')
date = input('Enter the date of the appointment you want to see: ')

# Делаем каждое слово с большой буквы
capitalize = '_'.join([name.capitalize() for name in full_name.split()])

if os.path.isdir(f'patients/{capitalize}'):
    try:
        f = open(f'patients/{capitalize}/visits/{date}.txt', 'r', encoding='utf-8')
        print(f.read())
        f.close()
    except FileNotFoundError:
        print('There was no such appointment with the doctor!')

else:
    print('There is no such patient!')
    exit() # по условию жирным шрифтом было написано ЗАВЕРШИТЬ ПРОГРАММУ

# Ivanov ivan ivanovich
# 2024-09-05