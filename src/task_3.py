import os

full_name = input('Enter the full name of the patient separated by space (Ivanov Ivan Ivanovich): ')

# Делаем каждое слово с большой буквы
capitalize = '_'.join([name.capitalize() for name in full_name.split()])

try:
    # file = open(f'patients/{capitalize}', 'r', encoding='utf-8')
    # file.close()

    # Многострочный ввод
    print('Enter records for the current appointment (to finish press Enter twice): ')
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)

except FileNotFoundError:
    print('There is no such patient!')
    exit()





# Ivanov ivan ivanovich
# 2024-09-05
# Sidorova Svetlana Sergeevna