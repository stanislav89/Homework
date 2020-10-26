# Написать функцию которая будет простое число возводить в квардрат.
# Необходимо возвести в квадрат все простые числа в списке используя функцию map

def kvadrat(chislo):
    res = chislo*chislo
    print(res)


spisok = [1, 2, 3, 4, 5]
kv_spisok = list(map(kvadrat, spisok))
