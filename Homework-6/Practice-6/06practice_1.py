# Задача 1. Курьер
# Вам известен номер квартиры, этажность дома и количество квартир на этаже.
# Задача: написать функцию, которая по заданным параметрам напишет вам, в какой подъезд и
# на какой этаж подняться, чтобы найти искомую квартиру.


def kurier():
    kvartira = int(input('Введите номер квартиры: '))
    floor = int(input('Введите количество этажей в доме: '))
    kol = int(input('Введите количество квартир на этаже: '))

    padik = kvartira // (floor * kol)
    print('Квартира в ' + (str(padik + 1)) + 'м подъезде.')

    while kvartira:
        if kvartira > (floor * kol):
            kvartira -= (floor * kol)
        elif kvartira < (floor * kol):
            print('Квартира на ' + (str((kvartira // kol) + 1)) + 'м этаже.')
            break
        elif kvartira == (floor * kol):
            print('Квартира на последнем этаже.')
            break
        else:
            print('Этого не может быть =)')
            break


kurier()
