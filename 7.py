import json

profits = {}
damages = {}
average_profit = {}
result_list = []

with open("text7.txt", "r") as file1:
    lines = file1.readlines()
    for line in lines:
        name, type, profit, damage = line.split()
        result = int(profit) - int(damage)
        if result >= 0:
            key = name
            value = result
            profits[key] = value
        if result < 0:
            key = name
            value = result
            damages[key] = value
    list_profits = list(profits.values())
    average_profits = round(sum(list_profits) / len(list_profits), 1)
    key = "average_profit"
    value = average_profits
    average_profit[key] = value

result_list.append(profits)
result_list.append(damages)
result_list.append(average_profit)
print(result_list)

with open("text7.json", "w") as file2:
    json.dump(result_list, file2)
