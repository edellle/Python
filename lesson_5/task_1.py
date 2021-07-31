# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


lines = ''
while True:
    temp = input ('Ваша строка: ')
    if temp != '':
        lines += temp + '\n'
    else:
        break
my_text = open ("text_1.txt", 'w')
my_text.writelines(lines)
my_text.close()