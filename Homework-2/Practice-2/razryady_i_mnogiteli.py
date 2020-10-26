# Ввести число, вывести его разряды и их множители

chislo = int(input('Введите целое число: '))

print('Ваше число ---> ' + str(chislo))
a = str(chislo)  # в строку для списка
list = []
list.extend(a)  # число в список

print('Разряды вашего числа и их множител:')
while list:
    if len(list) > 1:
        len(list) - 1
        print(list[0] + ' * 10^' + str(len(list)))
        del(list[0])
    else:
        print(list[0])
        break
