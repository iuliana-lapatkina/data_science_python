from functools import reduce

my_list = list(range(100, 1001))
new_list = [el for el in my_list if el % 2 == 0]

umnog = reduce(lambda a, x: a * x, new_list)
print(umnog)
