# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


from abc import abstractmethod

class Clothes:
    @abstractmethod
    def fabric (self):
        pass


class Coat (Clothes):
    def __init__(self, size, name = None):
        self.size = size
        self.name = name

    @property
    def fabric (self):
        return self.size / 6.5 + 0.5


class Suit (Clothes):
    def __init__(self, height, name = None):
        self.height = height
        self.name = name

    @property
    def fabric (self):
        return 2 * self.height + 0.3


black_coat = Coat (46)
print (f'Ткани для пальто {black_coat.fabric:.2f} м')

white_coat = Coat (40)
print (f'Ткани для пальто {white_coat.fabric:.2f} м')

blue_suit = Suit (1.68)
print (f'Ткани для костюма {blue_suit.fabric:.2f} м')

red_suit = Suit (1.8)
print (f'Ткани для костюма {red_suit.fabric:.2f} м')

print (f'Всего ткани {black_coat.fabric + white_coat.fabric + blue_suit.fabric + red_suit.fabric :.2f} м')