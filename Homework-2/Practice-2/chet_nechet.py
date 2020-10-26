# Проверить, является ли введеное число четным

chislo = int(input('Введите целое число: '))
if chislo % 2 == 0:
    print(str(chislo) + ' - это чётное число')
elif chislo % 2 != 0:
    print(str(chislo) + ' - это НЕчётное число')
else:
    print('ERROR')
