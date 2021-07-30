my_list = [33, 2, 41, 123, 0, 3, 11]
new_list = []

for i in range(len(my_list)-1):
    if my_list[i] < my_list[i+1]:
        new_list.append(my_list[i+1])

print(f'Cписок чисел: {my_list}')
print(f'Элементы исходного списка, значения которых больше предыдущего элемента: {new_list}')
