# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


worker_income = {'wage': 5000, 'bonus': 1000}

class Worker:
    def __init__ (self, w_name, w_surname, w_position):
        self.name = w_name
        self.surname = w_surname
        self.position = w_position
        self.__income__ = worker_income

class Position (Worker):
    def get_full_name (self):
        print (self.name + ' ' + self.surname)

    def get_total_income (self):
        total = self.__income__.get('wage') + self.__income__.get('bonus')
        print (total)


driver = Position ('Ivan', 'Ivanov', 'driver')
driver.get_full_name()
driver.get_total_income()

artist = Position ('Petr', 'Petrov', 'artist')
artist.get_full_name()
artist.get_total_income()