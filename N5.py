spisok = [43, 43, 34, 11, 11, 11, 8, 4]
print(spisok)
new = int(input('Введите новый элемент рейтинга: '))

for element in spisok:
    if new == element:
        ind = spisok.index(new)
        col = spisok.count(new)
        spisok.insert(ind + col, new)
        break
    else:
        if new > element:
            ind1 = spisok.index(element)
            spisok.insert(ind1, new)
            break

if new < element:
    spisok.append(new)

print(spisok)
