# Продолжаем идеализировать fizzbuzz, теперь применяем функции и map везде, где можно и нельзя!

fizz = int(input("Enter first number: "))
buzz = int(input("Enter second number: "))
third_ = int(input("Enter third number: "))


def fizzbuzz(third_):
    numbers = []

    for i in range(1, third_ + 1):
        if (i % fizz == 0) and (i % buzz == 0):
            numbers.append('FB')
        elif i % fizz == 0:
            numbers.append('F')
        elif i % buzz == 0:
            numbers.append('B')
        else:
            numbers.append(i)
    result = (' , '.join(map(str, numbers)))
    print(result)


fizzbuzz(third_)
