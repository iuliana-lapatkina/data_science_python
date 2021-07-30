def pay():
    time = float(input('Выработка в часах: '))
    hour = float(input('Ставка в час: '))
    bonus = float(input('Премия: '))
    return time * hour + bonus

print(f'Заработная плата сотрудника {pay()}')
