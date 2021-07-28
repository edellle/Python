# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

count = int( input("Сколько элементов будет в списке? "))
my_list = []
i = count
while i > 0:
    my_list.append(input ("Введите элемент списка "))
    i -= 1
print ("Исходный список: ", my_list)
new_list = []
for el in my_list:
    # меняем местами четный элемент со следующим за ним
    if (my_list.index(el)) % 2 == 0 and my_list.index(el) < count - 1:
        new_list.append(my_list[my_list.index(el) + 1])
        new_list.append(my_list[my_list.index(el)])
    # добавляем последний элемент в списке с нечетной длиной
    elif my_list.index(el) == count - 1 and count % 2 != 0:
        new_list.insert(count - 1, el)
print ("Измененный список: ", new_list)