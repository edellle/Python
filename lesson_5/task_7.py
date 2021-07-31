# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.


# Текст в файле:
# firm_1 ООО 10000 500
# firm_2 ОАО 12345 987655
# firm_3 ЗАО 6547 236
# firm_4 ОАО 678 1034
# firm_5 ООО 767676 757575


import json

with open('text_7.txt') as my_text:
    my_list = my_text.readlines()
    firm_list = {}
    profit_list = []
    for list in my_list:
        list = list.replace('\n', '')
        list = list.split(' ')
        profit = (int(list[2]) - int(list[3]))
        profit_list.append(profit)
        firm_list.update({list[0]: profit})
    counter = 0
    profit_sum = 0
    for i in profit_list:
        if i > 0:
            counter += 1
            profit_sum += i
    print('Средняя прибыль составляет: ', profit_sum / counter)
    avg_profit = {'Average profit' : profit_sum / counter}
    my_json = [firm_list, avg_profit]
    with open('task_7.json', "w") as my_file:
        json.dump(my_json, my_file)
