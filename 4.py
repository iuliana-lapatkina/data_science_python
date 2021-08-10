class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'едет'

    def stop(self):
        return f'остановился'

    def turn_r(self):
        return f'повернул направо'

    def turn_l(self):
        return f'повернул налево'

    def show_speed(self):
        return self.speed

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'превысил скорость'
        else:
            return self.speed

class SportCar(Car):
    def sport_car(self):
        return f'- sport car.'

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'превысил скорость'
        else:
            return self.speed

class PoliceCar(Car):
    def ispolice(self):
        if self.is_police is True:
            return "- полицейская машина"

town = TownCar('Audi', 99, 'blue', False)
print(town.name + " " + town.go(), town.show_speed(), town.stop())

sport = SportCar('Mazda', 133, 'red', False)
print(sport.name + " " + sport.go(), sport.show_speed(), sport.turn_l(), sport.stop())

work = WorkCar('Kamaz', 45, 'red', False)
print(work.name + " " + work.go(), work.show_speed(), work.turn_r(), work.stop())

police = PoliceCar('Lada', 85, 'yellow', True)
print(police.name + " " + police.ispolice() + police.go(), police.show_speed(), police.turn_l(), police.stop())
