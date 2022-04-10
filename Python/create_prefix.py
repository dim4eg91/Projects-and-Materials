import os
import datetime

data = datetime.datetime.now()


#  Проблема с датой
# -------------------------------------------
# Функция замены пробелов на _ в имени файла.
# На вход подается строка
# На выходе возвращается строка
def replace_space(s):
    list_s = s.split()
    string_without_space = '_'.join(list_s)
    return string_without_space


# -------------------------------------------
directory = input('Введите полный путь до директории:\n')
list_of_files = os.listdir(directory)
for i in range(len(list_of_files)):
    a = replace_space(list_of_files[i])
    os.rename(f'{directory}\{list_of_files[i]}', f'{directory}\{a}')


list_of_files = os.listdir(directory)
choose_1 = input(f'\n1. Создать собственный префикс\n2. Подствить текущую дату [{data}]\n')
if choose_1 == '1':
    prefix = input('\nВведите префикс:\n')
    for i in range(len(list_of_files)):
        os.rename(f'{directory}\{list_of_files[i]}', f'{directory}\{prefix}_{list_of_files[i]}')
# elif choose_1 == '2':
#     for i in range(len(list_of_files)):
#         os.rename(f'{directory}\{list_of_files[i]}', f'{directory}\{data}_{list_of_files[i]}')
else:
    print()