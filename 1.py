arg_1 = int(input("Enter the first number: "))
arg_2 = int(input("Enter the second number: "))

def my_funct(arg_1, arg_2):
    try:
        return arg_1 / arg_2
    except ZeroDivisionError:
        return "Division by zero is not possible"

print(my_funct(arg_1, arg_2))
