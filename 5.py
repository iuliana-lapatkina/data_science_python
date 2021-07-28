nums = []
text = input("Введите ряд чисел, разделенных пробелами или 'стоп' для выхода из программы: ")

while text != "стоп":
    for n in text.split():
        if n == str("стоп"):
            break
        n = int(n)
        nums.append(n)
    sum(nums)
    print(sum(nums))
    if text.find("стоп") != -1:
        break
    text = input("Введите ряд чисел, разделенных пробелами или 'стоп' для выхода из программы: ")
