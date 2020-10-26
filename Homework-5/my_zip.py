# Разбираемся, что делает функция zip, и пробуем написать свой собственный zip.

import random

names = ['Stanislav', 'Andrey', 'Ilya', 'Oleg']
ages = []
ages.append(random.randint(20, 30))
ages.append(random.randint(30, 40))
ages.append(random.randint(40, 50))
ages.append(random.randint(50, 60))
print('Имя и возраст: ')
print(dict(zip(names, ages)))

