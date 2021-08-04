dict = {}

with open("text6.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        for x, y in ("(л)", ""), ("(лаб)", ""), ("(пр)", ""), (",", ""):
            line = line.replace(x, y)
        key, value = line.rstrip("\n").split(":")
        dict[key] = value
        summ = sum(map(int, ''.join([i for i in value]).split()))
        dict[key] = summ
    print(f"{dict}")
