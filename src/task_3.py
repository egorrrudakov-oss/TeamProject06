import os
from datetime import date

full_name = input('Enter the full name of the patient separated by space (Ivanov Ivan Ivanovich): ')

# Делаем каждое слово с большой буквы
capitalize = '_'.join([name.capitalize() for name in full_name.split()])

try:
    # file = open(f'patients/{capitalize}', 'r', encoding='utf-8')
    # file.close()

    # Многострочный ввод
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

except FileNotFoundError:
    print('There is no such patient!')
    exit()





# Ivanov ivan ivanovich
# 2024-09-05
# Sidorova Svetlana Sergeevna