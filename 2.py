my_f = open("text2.txt", "r")
i=0

for line in my_f:
    i += 1
    print(line)
    print(f'Количество слов: {len(line.split())}')

print(f'Количество строк: {i}')

my_f.close()
