# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.


# Текст в файле:

# Тра-та-та
# Тра-та-та
# Мы везем с собой кота,
# Чижика, собаку,
# Кошку-забияку,
# Обезьяну, попугая...

#Слова, в которых встречается дефис, считаем за одно слово (например, "Тра-та-та")


my_text = open ('text_2.txt')
rows = 0
for line in my_text:
    rows += 1
    print (f"Слов в строке {rows}: {line.count(' ') + 1}")
print (f"Всего строк в файле — {rows}")
my_text.close()