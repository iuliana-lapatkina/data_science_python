my_f = open("text.txt", "x")

while my_f.write != '':
    line = my_f.write(input("Введите текст для записи: "))
    if not line:
        break
    else:
        line = my_f.write('\n')

my_f.close
