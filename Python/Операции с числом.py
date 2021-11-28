a = int(input('Введите число: '))
count = 0
total = 0
p = 1
last = a % 10
f = a
while a != 0:
    l = a % 10 # определяем последюю цифру числа
    count += 1
    total += l
    p *= l
    a = a // 10 # из числа удаляем его последнюю цифру
first = f // (10 ** (count - 1))
print()
print('Сумма всех цифр числа:', total)
print('Количество цифр в числе:', count)
print('Произведение всех цифр:', p)
print('Среднее арифметическое всех цифр:', total / count)
print('Первая цифра:', first)
print('Сумма первой и последней цифр:', first + last)
