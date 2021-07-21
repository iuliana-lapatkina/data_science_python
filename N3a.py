winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

mnth = int(input("Введите номер месяца: "))

if mnth > 1 and mnth < 12:
    if mnth in winter:
        print('winter')
    if mnth in spring:
        print('spring')
    if mnth in summer:
        print('summer')
    if mnth in autumn:
        print('autumn')
else:
    print("Incorrect number")