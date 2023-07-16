# Задание 2.
# Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
# length (длина в метрах), width (ширина в метрах).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
# метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
# Массу и толщину сделать публичными атрибутами.

class Road:
    m = 25
    depth = 0.05

    def __init__(self, width, length):
        self._width = width
        self._length = length

    def weigth(self):
        print(f'{int(self._width * self._length * self.m * self.depth)} кг')

res = Road(width=20, length=5000)
res.weigth()


