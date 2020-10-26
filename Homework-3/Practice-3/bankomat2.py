# -----Банкомат выдаёт сумму мелкими, но не больше 10 штук каждой мелкой купюры

kup1 = 200  # 10 купюр по 20 грн
kup2 = 500
kup3 = 1000
kup4 = 2000
kup5 = 5000
kup6 = 10000
sum = int(input('Введите сумму, которую хотите снять: '))

while sum >= 20:
    if (sum >= 20) and (kup1 >= 20):
        print('20')
        kup1 -= 20
        sum -= 20
    elif (sum >= 50) and (kup2 >= 50):
        print('50')
        kup2 -= 50
        sum -= 50
    elif (sum >= 100) and (kup3 >= 100):
        print('100')
        kup3 -= 100
        sum -= 100
    elif (sum >= 200) and (kup4 >= 200):
        print('200')
        kup4 -= 200
        sum -= 200
    elif (sum >= 500) and (kup5 >= 500):
        print('500')
        kup5 -= 500
        sum -= 500
    elif (sum >= 1000) and (kup6 >= 1000):
        print('1000')
        kup6 -= 1000
        sum -= 1000
    else:
        print('В банкомате не осталось купюр.\n' \
              'Остаток от суммы для снятия ' + str(sum) + ' грн. Эта сумма останется на карте.')
        break
