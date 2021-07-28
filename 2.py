def human(name, surname, year, city, email, tel):
    print(f"{name} {surname} {year} года рождения из города {city} {email} {tel}")

human(name = input("Имя: "), surname = input("Фамилия: "),
         year = input("Год рождения: "), city = input("Город проживания: "),
         email = input("Электронная почта: "), tel = input("Телефон: "))
