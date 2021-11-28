#Напишите программу, которая выводит на экран текст «Здравствуй, мир!» (без кавычек).
#Примечание 1. Проверяющая система будет сравнивать результат вашей программы и правильный ответ посимвольно.
#Это означает, что выводить нужно ровно такую строку, которая указана в условии задачи.
#Примечание 2. Проверяющая система пользуется стандартным выводом (stdout, команда print()).

print('Здравствуй, мир!')

#В популярном сериале «Остаться в живых» использовалась последовательность чисел 4 8 15 16 23 42, которая принесла
# героям удачу и помогла сорвать джекпот в лотерее. Напишите программу, которая выводит данную последовательность чисел
# с одним пробелом между ними.
#Примечание. Текст '4 8 15 16 23 42' не использовать. Воспользуйтесь возможностью команды print() выводить несколько
# аргументов, указанных через запятую.
print('4', '8', '15', '16', '23', '42')

#Измените предыдущую программу так, чтобы каждое число последовательности 4 8 15 16 23 42 печаталось на отдельной строке.
#Примечание. Каждая последующая команда print() выводит указанный текст, начиная с новой строки.
print('4')
print('8')
print('15')
print('16')
print('23')
print('42')

#Напишите программу, которая выводит указанный треугольник, состоящий из
#звездочек (*).
print('*')
print('**')
print('***')
print('****')
print('*****')
print('******')
print('*******')

#На вход программе подается строка текста – имя человека. Напишите программу, которая выводит на экран приветствие в виде слова «Привет» (без кавычек), после которого должна стоять запятая и пробел, а затем введенное имя.
#Формат входных данных
#На вход программе подаётся одна строка — имя человека.
#Формат выходных данных
#Программа должна вывести текст в соотвествии с условием задачи.
#Примечание. Для считывания текста используйте команду input(), для печати текста на экране используйте команду print().
name = input()
print('Привет,', name)

#На вход программе подается строка текста – название футбольной команды. Напишите программу, которая повторяет ее на экране со словами « - чемпион!» (без кавычек).
#Формат входных данных
#На вход программе подается название футбольной команды.
#Формат выходных данных
#Программа должна вывести текст согласно условиям задачи.
#Примечание. Для считывания текста используйте команду input(), для печати текста на экране используйте команду print().
team = input()
print(team, '- чемпион!')

#Напишите программу, которая считывает три строки по очереди, а затем выводит их в той же последовательности, каждую на отдельной строчке.
#Формат входных данных
#На вход программе подаются три строки, каждая на отдельной строке.
#Формат выходных данных
#Программа должна вывести введенные строки в той же последовательности, каждую на отдельной строке.
#Примечание. Для считывания текста используйте команду input(), для печати текста на экране используйте команду print().
a = input()
b = input()
c = input()
print(a)
print(b)
print(c)

#Напишите программу, которая считывает три строки по очереди, а затем выводит их в обратной последовательности, каждую на отдельной строчке.
#Формат входных данных
#На вход программе подается три строки, каждая на отдельной строке.
#Формат выходных данных
#Программа должна вывести введенные строки в обратной последовательности, каждую на отдельной строке.
#Примечание. Используйте 3 переменные для сохранения введённых строк текста.
a = input()
b = input()
c = input()
print(c)
print(b)
print(a)