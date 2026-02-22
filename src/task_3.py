import json
import os
from datetime import date

full_name = input('Enter the full name of the patient separated by space (Ivanov Ivan Ivanovich): ')

# Делаем каждое слово с большой буквы
capitalize = '_'.join([name.capitalize() for name in full_name.split()])

if os.path.isdir(f'patients/{capitalize}'):
    try:
        date = input('Enter the date of the appointment you want to see: ')
        f = open(f'patients/{capitalize}/visits/{date}.txt', 'r', encoding='utf-8')
        print(f.read())
        f.close()

        try:
            with open(f'patients/{capitalize}/card.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
            print(json.dumps(data, indent=4, ensure_ascii=False))
        except FileNotFoundError:
            print("There is no patient card!")
            surname = input("Enter the surname of the patient: ")
            name = input("Enter the name of the patient: ")
            patronymic = input("Enter the patronymic of the patient: ")
            date_of_birth = input("Enter the date of birth of the patient (1994-01-10): ")
            sex = input("Enter the sex of the patient (M or W): ")
            new_card = {
                "Surname": surname.capitalize(),
                "Name": name.capitalize(),
                "Patronymic": patronymic.capitalize(),
                "Date of birth": date_of_birth,
                "Sex": sex.upper()
            }
            filename = "card.json"
            filepath = os.path.join(f'patients/{capitalize}/', filename)
            with open(filepath, 'w', encoding='utf-8') as json_file:
                json.dump(new_card, json_file, indent=4)
            with open(filepath, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
            print(json.dumps(data, indent=4, ensure_ascii=False))
    except FileNotFoundError:
        print('There was no such appointment with the doctor!')
else:
    print('There is no such patient!')
#    exit() # по условию жирным шрифтом было написано ЗАВЕРШИТЬ ПРОГРАММУ

# Ivanov ivan ivanovich
# 2024-09-05

# Petrov petr petrovich
# 2024-09-01


