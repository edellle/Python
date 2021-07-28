# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int (input ("Укажите номер месяца: "))
print ("Решение с использованием словаря")
season_dict = {(1, 2, 12): "Зима",
               (3, 4, 5): "Весна",
               (6, 7, 8): "Лето",
               (9, 10, 11): "Осень"}
for season in season_dict.keys():
    if month in season:
        print (f"Для месяца {month} сезон {season_dict.get(season)}")
print ("Решение с использованием списков")
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
if month in winter:
    print (f"Для месяца {month} сезон зима")
elif month in spring:
    print(f"Для месяца {month} сезон весна")
elif month in summer:
    print (f"Для месяца {month} сезон лето")
else:
    print (f"Для месяца {month} сезон осень")


