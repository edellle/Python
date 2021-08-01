# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open ('text_5.txt', 'w+') as my_file:
    numbers = input ('Введите одно или несколько чисел через пробел:  ')
    my_file.write(numbers)
    my_file.seek(0)
    r_numbers = my_file.read()
    r_numbers  = r_numbers.split(' ')
    result = 0
    for n in r_numbers:
        result += int(n)
    print(f'Сумма чисел: {result}')
