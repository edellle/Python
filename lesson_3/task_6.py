# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def int_func_2 (str):
    first = str[0].upper()
    return first + str[1:]


my_str = 'lorem ipsum dolor sit amet, consectetur adipiscing elit'
print (f"Исходная строка: {my_str}")
my_list = my_str.split (" ")


new_list = []
for i in my_list:
    new_list.append (int_func_2(i))
my_str = ' '.join (new_list)
print (f"Преобразованная строка: {my_str}")





