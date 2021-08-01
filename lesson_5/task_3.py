# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# Текст в файле

# Иванов 12345.12
# Петров 45321.34
# Сидоров 23999.00
# Романов 19999.99
# Кириллов 20000.01
# Степанов 4943.23


my_text = open ('text_3.txt')
emp_count = 0
emp_list = {}
for line in my_text:
    emp_count += 1
    new_line = line.split(" ")
    line.strip('\n')
    emp_list.update({new_line[0] : float (new_line [1])})
print ('Работники с заработной платой меньше 20000:')
prices = 0
for e in emp_list:
    prices += emp_list.setdefault(e)
    if emp_list.setdefault(e) < 20000:
        print (e)
print ('Средний заработок сотрудников: ', round (prices / emp_count, 2))
my_text.close()