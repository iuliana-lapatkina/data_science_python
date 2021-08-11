class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def sum_coat(self):
        return self.size / 6.5 + 0.5

    def sum_suit(self):
        return self.height * 2 + 0.3

    @property
    def sum(self):
        return str(f'Расход ткани общий: {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.summ_coat = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Расход ткани на пальто: {self.summ_coat}'


class Suit(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.summ_suit = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Расход ткани на костюм: {self.summ_suit}'

coat = Coat(2, 4)
suit = Suit(1, 2)
print(coat)
print(suit)
print(coat.sum)
print(suit.sum)
print(coat.sum_coat())
print(suit.sum_suit())
