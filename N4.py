phrase = input("введите несколько слов, разделенных пробелами: ")

for ind, el in enumerate((phrase.split()), 1):
    print(ind, el[:9])
    
