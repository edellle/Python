# Cоздать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


rus_eng = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
my_text = open ('text_4.txt')
new_text = open('text_4_new.txt', 'w+')
line = my_text.readlines()
keys = rus_eng.keys()
for k in keys:
    for l in line:
        if l.count(k) != 0:
            new_text.write(l.replace(k, rus_eng.setdefault(k)))
            continue
my_text.close()
new_text.close()