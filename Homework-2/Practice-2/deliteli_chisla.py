# Ввести число, вывести все его делители

chislo = int(input('Введите целое число: '))

i = 1  # i - делители введённого числа
print('Делители числа ' + str(chislo) + ':')
while i != chislo:
    if chislo % i == 0:
        print(i, end=' ')
        i += 1
    else:
        i += 1
