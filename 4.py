# -*- coding: UTF-8 -*-
replace_values = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}

def multiple_replace(line, replace_values):
    for i, j in replace_values.items():
        line = line.replace(i, j)
    return line

with open("text4.txt") as file_in:
    while True:
        line = file_in.readline()
        line = multiple_replace(line, replace_values)
        with open("text4b.txt", "a") as file_out:
            file_out.write(line)
        if not line:
            break
        print(line.strip())
