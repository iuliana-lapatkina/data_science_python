my_list = list(range(20, 240))
new_list = [el for el in my_list if el % 20 == 0 or el % 21 == 0]
print(f"Числа от 20 до 240, кратные 20 или 21:\n{new_list}")
