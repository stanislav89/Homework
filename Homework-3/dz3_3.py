# Переделать вторую задачу так, чтобы результат писался в другой файл.

f = open('3_2.txt')
line = f.readlines()
print('В файле 20 строк из 3х чисел, для какой строки будем считать fizzbuzz? \n Строки от 0 до 19')
a = int(input('Строка номер ---> '))
print('Строка номер ' + str(a) + ' ---> ' + str(line[a]))

# Занесу числа из строки файла в список (не получилось по-другому взять цифры напрямую из строки файла :)
l = len(line[a])  # длина сроки а
mystroka = line[a]
myspisok = []  # пока что пустой
i = 0
while i < l:
    s_int = ''  # трока из файла
    a = mystroka[i]
    while '0' <= a <= '9':
        s_int += a
        i += 1
        if i < l:
            a = mystroka[i]
        else:
            break
    i += 1
    if s_int != '':
        myspisok.append(int(s_int))
# print(myspisok)


# Переделать вторую задачу так, чтобы результат писался в другой файл.
file2 = open('3_2_rezultat.txt', 'w')

# Теперь считаем fizzbuzz
print('FizzBuzz:')
fizz = myspisok[0]
buzz = myspisok[1]
third_ = myspisok[2]
schet = 0
while schet < third_:
    schet += 1
    if schet % fizz == 0 and schet % buzz == 0:
        print('FB', end=' ')
        file2.write(str('FB'))
    elif schet % fizz == 0:
        print('F', end=' ')
        file2.write(str('F'))
    elif schet % buzz == 0:
        print('B', end=' ')
        file2.write(str('B'))
    else:
        print(schet, end=' ')
        file2.write(str(schet))

f.close()
file2.close()
