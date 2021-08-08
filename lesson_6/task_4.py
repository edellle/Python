# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__ (self, car_name, car_color, current_speed):
        self.name = car_name
        self.color = car_color
        self.speed = current_speed

    def go (self):
        print (f'{self.name} started to go')

    def stop (self):
        print (f'{self.name} stopped')

    def turn (self, direction = None):
        if direction is not None:
            print (f'{self.name} turn {direction}')
        else:
            print ('The car go straight')

    def show_speed (self):
        print (f'{self.name} speed is {self.speed}')


class TownCar (Car):
    def show_speed (self):
        print (f'{self.name} speed is {self.speed}')
        if self.speed > 60:
            print ('Your speed is too fast')

class SportCar (Car):
    pass


class WorkCar (Car):
    def show_speed(self):
        print(f'Speed is {self.speed}')
        if self.speed > 40:
            print('Your speed is too fast')


class PoliceCar (Car):
    is_police = True


nissan = TownCar ('Nissan', 'blue', 62)
nissan.go()
nissan.turn('left')
nissan.show_speed()
nissan.stop()

print ('\n')

renault = TownCar ('Renault', 'red', 59)
renault.go()
renault.turn()
renault.show_speed()
renault.stop()
print (renault.is_police)

print ('\n')

ferrari = SportCar ('Ferrari', 'orange', 180)
ferrari.go()
ferrari.turn('right')
ferrari.show_speed()
ferrari.stop()
print (ferrari.is_police)

print ('\n')

bus = WorkCar ('Bus', 'white', 38)
bus.go()
bus.turn('right')
bus.show_speed()
print (bus.is_police)

print ('\n')

ambulance = WorkCar ('Ambulance', 'white', 68)
ambulance.go()
ambulance.turn()
ambulance.show_speed()
print (ambulance.is_police)

print ('\n')

police = PoliceCar ('Police', 'white', 80)
police.go()
police.turn('right')
police.show_speed()
police.stop()
print (police.is_police)