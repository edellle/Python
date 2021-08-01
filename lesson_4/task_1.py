from sys import argv

script_name, hours, price, bonus = argv
print ("Salary is ", float (hours) * float (price) + float (bonus))
