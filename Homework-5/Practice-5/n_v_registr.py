# -----1-----Написать 2 функции. Первая функция будет принимать строку и приводить ее к нижнему регистру.
# Вторая функция будет принимать строку и проводить ее к верхнему регистру.
# После чего с помощью map применить ваши функции к списку строк. Отдельно каждую функцию к отдельному списку строк!

# Нижний регистр
def n_registr(words):
    res = words.lower()
    print(res)


# Верхний регистр
def v_registr(words):
    res = words.upper()
    print(res)


spisok1 = ['one', 'two', 'tree']
spisok2 = ['FOUR', 'FIVE', 'SIX']

bigwords = list(map(v_registr, spisok1))
smallwords = list(map(n_registr, spisok2))
