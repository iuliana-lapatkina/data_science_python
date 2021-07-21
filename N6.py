N = 0
all_prod = []
name1 = []
price1= []
count1 = []
ed1 = []

while N < 3:
    N += 1
    name = input('Введите название товара: ')
    price = input('Введите цену товара: ')
    count = input('Введите количество товара: ')
    ed = input('Введите единицы измерения товара: ')
    slovar1 = dict({'название' : name, 'цена' : price, 'количество' : count, 'ед.' : ed})
    prod = (N, slovar1)
    all_prod.append(prod)
    name1.append(name)
    price1.append(price)
    count1.append(count)
    ed1.append(ed)
    slovar2 = dict({'название': list(set(name1)), 'цена': list(set(price1)), 'количество': list(set(count1)), 'ед.': list(set(ed1))})

print(all_prod)
print(slovar2)
