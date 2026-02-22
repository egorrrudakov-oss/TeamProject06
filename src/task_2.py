import os

full_name = input('Enter the full name of the patient separated by space (Ivanov Ivan Ivanovich): ')

# Делаем каждое слово с большой буквы
capitalize = '_'.join([name.capitalize() for name in full_name.split()])

if os.path.isdir(f'patients/{capitalize}'):

    # Проверка на наличие папки visits
    try:
        visits = f'patients/{capitalize}/visits'
        if os.listdir(visits):
            print('Previous doctor appointments:')
            for i in os.listdir(visits):
                print(i[:-4])
        else:
            print('This is the first appointment with the doctor!')
            exit() # выход из программы
    except FileNotFoundError:
        print('This is the first appointment with the doctor!')
        exit()

    date = input('Enter the date of the appointment you want to see: ')
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
# Sidorova Svetlana Sergeevna