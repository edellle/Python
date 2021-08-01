# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division (dividend, divisor):
    if divisor == 0:
        return "Нельзя выполнить деление на 0!"
    else:
        return f"{dividend} / {divisor} = {dividend / divisor}"


dvdnt = float (input ("Делимое: "))
dvsr = float (input ("Делитель: "))
print (division (dvdnt, dvsr))
