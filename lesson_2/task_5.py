# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].


rating = [9, 8, 5, 4, 4, 4, 3]
print ("В этой программе нужно вводить натуральные числа. Для завершения работы введите 0")
print ("Исходный рейтинг: ", rating)
while True:
    number = int (input ("Укажите рейтинг: "))
    # нужно ли выходить
    if number == 0:
        break
    # куда подставить введенное число
    else:
        # в рейтинге уже есть такое число
        if rating.count (number) != 0:
            rating.insert (rating.index (number) + rating.count (number), number)
        # в рейтинге пока нет такого числа
        else:
            for i in rating:
                if number < i:
                    if (rating.index (i) + rating.count (i)) == len (rating):
                        rating.append (number)
                    continue
                else:
                    rating.insert (rating.index (i), number)
                    break
print ("Обновленный рейтинг: ", rating)