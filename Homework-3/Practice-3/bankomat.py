# -----Банкомат выдаёт сумму максимально возможными купюрами-----

kup1 = 20  # купюра 1
kup2 = 50
kup3 = 100
kup4 = 200
kup5 = 500
kup6 = 1000
sum = int(input('Введите сумму, которую хотите снять: '))

while sum >= kup1:  # пока сумма больше или равно 20 грн
    if sum >= kup6:
        print(kup6)
        sum -= kup6
    elif (sum < kup6) and (sum >= kup5):
        print(kup5)
        sum -= kup5
    elif (sum < kup5) and (sum >= kup4):
        print(kup4)
        sum -= kup4
    elif (sum < kup4) and (sum >= kup3):
        print(kup3)
        sum -= kup3
    elif (sum < kup3) and (sum >= kup2):
        print(kup2)
        sum -= kup2
    elif (sum < kup2) and (sum >= 40):
        print(kup1)
        sum -= kup1
    elif (sum < 40) and (sum >= 20):
        print(kup1)
        sum -= kup1
        print('Остаток от суммы для снятия равен ' + str(sum) + ' грн. Эта сумма останется на карте')
    else:
        break
