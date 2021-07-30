n = int(input("Введите число: "))

def my_func(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        yield fact

for x in my_func(n):
    print(x)
