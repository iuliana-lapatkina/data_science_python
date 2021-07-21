name = input ("Как Вас зовут? ")
print ("Хотите узнать свой индекс массы тела," + name + "?")

weight = int(input("Введите Ваш вес: "))
height = int(input("Введите Ваш рост: "))

IMT = round((weight / (height / 100) ** 2), 1)

print("Ваш ИМТ составляет: " + str(IMT))