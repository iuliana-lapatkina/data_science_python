dict = {}
with open("text3.txt") as file:
    for line in file:
        key, value = line.rstrip("\n").split(" - ")
        dict[key] = value

new_dict = {}
for key, value in dict.items():
    if int(value) <= 20000:
        new_dict[key] = value

for key in new_dict.keys():
    print(f"Работники с окладом меньше 20000: {key}")

valuesList = list(dict.values())
int_list = [int(x) for x in valuesList]
print(f"Cредняя величина дохода: {round(sum(int_list) / len(int_list), 1)}")
