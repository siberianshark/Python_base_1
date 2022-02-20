
class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def calculate(self):
        calculate = self._length * self._width * self.weight * self.height / 1000

if __name__ == '__main__':
    road = Road(5000, 20)
    road.calculate()
    print(f'Для изготовления покрытия дороги нужно {road.calculate()} тонн.')