Mnths = {12:"winter", 1:"winter", 2:"winter",
      3:"spring", 4:"spring", 5:"spring",
      6:"summer", 7:"summer", 8:"summer",
      9:"autumn", 10:"autumn", 11:"autumn"}

mnth = int(input("Введите номер месяца: "))

if mnth > 1 and mnth < 12:
    print(Mnths.get(mnth))
else:
    print("Incorrect number")
