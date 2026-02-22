import os
import csv
import json
from datetime import date

full_name = input('Enter the full name of the patient separated by space (Ivanov Ivan Ivanovich): ')

# Делаем каждое слово с большой буквы
capitalize = '_'.join([name.capitalize() for name in full_name.split()])

if os.path.isdir(f'patients/{capitalize}'):

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
    g = True
    while g:
        while True:
            choice = input(f"""{50 * "-"}
Enter:
 - 1, if you want to see the list of dates of previous visits;
 - 2, if you want to see the recording of the previous visit;
 - 3, if you want to start recording in the current visit;
 - 4, if you want to finish the appointment and complete the program.
{50 * "-"}
""")
            if choice.isdigit(): break

        match int(choice):
            case 1:
                try:
                    visits = f'patients/{capitalize}/visits'
                    if os.listdir(visits):
                        print('Previous doctor appointments:')
                        for i in os.listdir(visits):
                            print(i[:-4])
                    else:
                        print('This is the first appointment with the doctor!')


                except FileNotFoundError:
                    print('This is the first appointment with the doctor!')

            case 2:
                # Проверка на наличие папки visits
                try:
                    visits = f'patients/{capitalize}/visits'
                    if os.listdir(visits):
                        print('Previous doctor appointments:')
                        for i in os.listdir(visits):
                            print(i[:-4])
                    else:
                        print('This is the first appointment with the doctor!')
                        exit()  # выход из программы
                except FileNotFoundError:
                    print('This is the first appointment with the doctor!')
                    exit()

                date_of_app = input('Enter the date of the appointment you want to see: ')
                try:
                    f = open(f'patients/{capitalize}/visits/{date_of_app}.txt', 'r', encoding='utf-8')
                    print(f.read())
                    f.close()
                except FileNotFoundError:
                    print('There was no such appointment with the doctor!')

            case 3:
                print('Enter records for the current appointment (to finish press Enter twice): ')
                lines = []
                empty_line = 0
                while True:
                    line = input()
                    if not line:
                        empty_line += 1
                        lines.append('\n')
                        if empty_line == 2:
                            break
                    else:
                        empty_line = 0
                        lines.append('\n')
                    lines.append(line)
                now = date.today()
                print(lines)
                f = open(f'patients/{capitalize}/{now}.txt', 'w', encoding='utf-8')
                for i in lines[:-1][1:]:
                    f.write(i)
                f.close()
            case 4:
                temp_file = 'schedule_temp.csv'
                found = False
                try:
                    with open('schedule.csv', 'r', encoding='utf-8') as infile, \
                            open(temp_file, 'w', encoding='utf-8', newline='') as outfile:

                        reader = csv.DictReader(infile)
                        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)

                        writer.writeheader()

                        for row in reader:
                            if full_name.lower() in row['Patient'].lower():
                                row['Did the patient visit the doctor'] = 'Yes'
                                found = True

                            writer.writerow(row)

                    if found:
                        os.replace(temp_file, 'schedule.csv')
                    else:
                        os.remove(temp_file)

                # except FileNotFoundError:
                #     print("File not found")
                except Exception as e:
                    print(f"Error: {e}")
                    if os.path.exists(temp_file):
                        os.remove(temp_file)
                break
    # # Проверка на наличие папки visits
    # try:
    #     visits = f'patients/{capitalize}/visits'
    #     if os.listdir(visits):
    #         print('Previous doctor appointments:')
    #         for i in os.listdir(visits):
    #             print(i[:-4])
    #     else:
    #         print('This is the first appointment with the doctor!')
    #         exit() # выход из программы
    # except FileNotFoundError:
    #     print('This is the first appointment with the doctor!')
    #     exit()


else:
    print('There is no such patient!')
    #exit() # по условию жирным шрифтом было написано ЗАВЕРШИТЬ ПРОГРАММУ

# Ivanov ivan ivanovich
# 2024-09-05
# Sidorova Svetlana Sergeevna