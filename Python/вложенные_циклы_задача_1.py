a = int(input())
b = int(input())
count = 0
maxl = 0
l = []
for i in range(a, b + 1):
    for j in range(1, i + 1):
        count = 0
        print('Отрезок:', j, '-', i)
        if i % j == 0:
            count += 1
            print(j)
            if count > maxl:
                maxl = count


print()
print('Отрезок:', a, '-', b)
print(count)