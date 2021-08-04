my_file = open("text5.txt", 'a')

line = input('Введите ряд чисел, разделенных пробелами: ')
my_file.write(line)
numbers = line.split()
print(sum(map(int, numbers)))

my_file.close
