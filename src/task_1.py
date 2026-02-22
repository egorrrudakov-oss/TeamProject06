full_name = input('Enter the full name of the patient separated by space (Ivanov Ivan Ivanovich): ')
date = input('Enter the date of the appointment you want to see: ')

# Делаем каждое слово с большой буквы
capitalize = '_'.join([name.capitalize() for name in full_name.split()])
print(capitalize)