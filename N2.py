list_1 = []
list_2 = []

while len(list_1) < 100:
    new = input('Введите любое число для списка, если хотите закончить список, введите "Конец": ')
    list_1.append(new)
    if new == 'Конец':
        break

list_1.remove('Конец')
print(list_1)

while len(list_1) > 1:
    a = list_1[1]
    b = list_1[0]
    list_2.append(a)
    list_2.append(b)
    list_1.pop(1)
    list_1.pop(0)

if list_1 != []:
    list_2.append(list_1[0])

print(list_2)
