class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Объединение двух клеток: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Вычитание двух клеток: {sub}'

    def __mul__(self, other):
        mul = self.quantity * other.quantity
        return f'Создается общая клетка из двух при умножении: {mul}'

    def __truediv__(self, other):
        truediv = self.quantity // other.quantity
        return f'Создается общая клетка из двух при делении: {truediv}'

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result

cell = Cell(4)
cell2 = Cell(1)
print(cell + cell2)
print(cell - cell2)
print(cell * cell2)
print(cell / cell2)
print(cell.make_order(7))
print(cell2.make_order(7))
