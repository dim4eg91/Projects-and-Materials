import os
import subprocess

print()
print('Введи путь до папки, где нужно собрать имена скриптов:')
dirr = input()
dirrectory = dirr

# Пример пути
# D:\Дима учеба\Python\Полигон\SQL

sql_files = os.listdir(dirrectory)
sql = [] # пустой список для имен скриптов без расширения .sql

# Создание списка имен скриптов без расширений .sql
for i in range(len(sql_files)):
    sql.append('.'.join(sql_files[i].split('.')[:-1]))
print('Список имен скриптов:', *sql, sep='\n')

# Создание xml
mc = open('D:\Дима учеба\Python\Импровизированный_гит\master_changelog.xml', 'w', encoding='utf-8')
mc.write('<databaseChangeLog\n')
mc.write('...\n')

for i in range(len(sql)):
    mc.write('<id=')
    mc.write(sql[i])
    mc.write('>\n')

mc.write('/<databaseChangeLog')

mc.close()
print()
print('master_changelog.xml создан')

subprocess.Popen('explorer "D:\Дима учеба\Python\Импровизированный_гит"')





