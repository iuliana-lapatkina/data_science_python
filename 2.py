class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def asphalt_mas(self):
        asphalt_mass = self._length * self._width * self.weight * self.height / 1000
        print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна: {round(asphalt_mass)}')

r = Road(5000, 20)
r.asphalt_mas()
