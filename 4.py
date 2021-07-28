def my_func(x, y):
    if y < 0:
        return 1 / (x ** abs(y))
    else:
        print("Число y должно быть отрицательным")

print(f'Первое число в степени второго: {my_func(x = float(input("Введите действительное положительное число x: ")), y = int(input("Введите целое отрицательное число y: ")))}')

def my_fun(x, y):
    if y < 0:
        for i in range(abs(y) - 1):
            x *= x
        return 1 / x
    else:
        print("Число y должно быть отрицательным")

print(f'Первое число в степени второго: {my_fun(x = float(input("Введите действительное положительное число x: ")), y = int(input("Введите целое отрицательное число y: ")))}')
