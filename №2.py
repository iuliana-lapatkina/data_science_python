sec_time = int(input ("Введите время в секундах: "))

hours = (sec_time // 3600)
min = ((sec_time % 3600) // 60)
sec = (((sec_time % 3600) % 60) % 60)

if hours < 10:
    hours = ("0" + str(hours))

if min < 10:
    min = ("0" + str(min))

if sec < 10:
    sec = ("0" + str(sec))

print(f"Время в формате чч:мм:сс составляет {hours}:{min}:{sec}")