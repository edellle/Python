# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.


from itertools import count, cycle


def script_1 ():
    start = 3
    print ("Script 1: ")
    for i in count (start):
        if i > 10:
            break
        print (i, end = ' ')


def script_2 ():
    print ("\nScript 2: ")
    part = 'Hello '
    counter = 1
    for a in cycle (part):
        counter += 1
        if counter >= 10:
            break
        print (a, end = '')


script_1()
script_2()