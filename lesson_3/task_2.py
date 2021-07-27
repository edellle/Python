# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def customer (name, surname, birth, city, email, phone):
    return (f"{name}, {surname}, {birth}, {city}, {email}, {phone}")

my_name = input ("Ваше имя: ")
my_surname = input ("Ваша фамилия: ")
my_birth = input ("Дата рождения: ")
my_city = input ("Город проживания: ")
my_email = input ("Электронная почта: ")
my_phone = input ("Номер телефона: ")
print ( customer ( my_name, my_surname, my_birth, my_city, my_email, my_phone))