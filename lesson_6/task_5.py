# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = ''

    def __init__ (self, st_title):
        self.title = st_title

    def draw (self):
        print ('Запуск отрисовки')


class Pen (Stationery):
    def draw (self):
        print ('Ручкой нужно писать в тетради')


class Pencil (Stationery):
    def draw (self):
        print ('Карандашом можно рисовать на бумаге')


class Handle (Stationery):
    def draw (self):
        print ('Пишите маркером на специальной доске')


my_pen = Pen ('Синяя ручка')
my_pen.draw()

my_pencil = Pencil ('Простой карандаш')
my_pencil.draw()

my_handle = Handle ('Красный маркер')
my_handle.draw()

something = Stationery ('Что-то')
something.draw()