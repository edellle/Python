# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

# реализовала первым способом, который пришел в голову
def my_func (v_1, v_2, v_3):
    if v_1 < v_2:
        if v_1 < v_3:
            return v_2 + v_3
        else:
            return v_1 + v_2
    else:
        if v_2 > v_3:
            return v_1 + v_2
        else:
            return v_1 + v_3

# сделала более оптимальным способом, подсказанным на уроке
# решила создание списка не включать в функцию, чтобы сделать ее более универсальной
def my_new_func (numbers):
    numbers.sort()
    return numbers [len(numbers) - 1] + numbers [len(numbers) - 2]

one = int (input ("Введите первое число: "))
two = int (input ("Введите второе число: "))
three = int (input ("Введите третье число: "))
numbers = []
numbers.append(one)
numbers.append(two)
numbers.append(three)
print (f"Сумма двух наибольших чисел: {my_func (one, two, three)}")
print (f"Сумма двух наибольших чисел: {my_new_func (numbers)}")