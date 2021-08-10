class Stationery:
    title: str

    def draw(self):
        return 'Запуск отрисовки'

class Pen(Stationery):
    title = 'Ручка'

    def draw(self):
        return self.title

class Pencil(Stationery):
    title = 'Карандаш'

    def draw(self):
        return self.title

class Handle(Stationery):
    title = 'Маркер'

    def draw(self):
        return self.title


p = Pen()
pc = Pencil()
h = Handle()
s = Stationery()

print(s.draw())
print(h.draw())
print(p.draw())
print(pc.draw())
