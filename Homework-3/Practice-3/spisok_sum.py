# -----Сумма списка-----"
list = [1, 2, 3, 4, 5, 6]
thesum = 0
for i in list:
    thesum += i
print("Sum of our list =", thesum)

# -----Выводит сама себя-----
f = open('spisok_sum.py')
for line in f:
    print(line, end=' ')
f.close()

# -----Выводит сама себя задом наперёд-----
f = open('spisok_sum.py')
for line in f:
    print(line[::-1], end=' ')
f.close()
