# Задача 2. Бриллиант
# --- Входным данным является целое число. Необходимо:
# написать проверку, чтобы в работу пускать только:
# --- положительные нечетные числа
# --- для правильного числа нужно построить бриллиант из звездочек или
# любых других символов и вывести его в консоли.
# --- Для числа 1 он выглядит как одна взездочка, для числа три он выглядит как звезда,
# потом три звезды, потом опять одна, для пятерки - звезда, три, пять, три, одна...

def briliant():
    chislo = int(input('Введите целое число (положительное и нечётное) ---> '))
    if (chislo > 0) and (chislo % 2 != 0):
        s = chislo // 2  # (space) пробелы вокруг звёздочек
        z = 1            # (zvezda) звёздочки
        while z <= chislo:
            print(s * ' ' + z * '*' + s * ' ')
            z += 2
            s -= 1

        z2 = chislo - 2       # звёздочки
        s2 = chislo - z2 - 1  # продолжаем бриллиант
        while z2 >= 1:
            print(s2 * ' ' + z2 * '*' + s * ' ')
            z2 -= 2
            s2 += 1


briliant()
