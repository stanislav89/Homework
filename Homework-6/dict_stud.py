# ---1--- Создать словарь оценок предполагаемых студентов
# (Ключ - ФИ студента, значение - список оценок студентов).
# Найти самого успешного и самого отстающего по среднему баллу.

students = {
    'messi': [12, 11, 10, 9, 8],
    'ronaldo': [11, 10, 9, 8, 7],
    'neymar': [10, 9, 8, 7, 6],
    'zidane': [9, 8, 7, 6, 5]
}
a = []  # список средних оценок студентов
for i in students:
    sr_bal = sum(students[i]) / len(students[i])  # средняя оценка
    print(i, '- средний бал -', sr_bal)
    a.append(sr_bal)

print('Худший средний бал ---> ' + str(min(a)))
print('Лучший средний бал ---> ' + str(max(a)))
