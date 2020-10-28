# ---2--- Создать структуру данных для студентов из имен и фамилий, можно случайных.
# Придумать структуру данных, чтобы указывать, в какой группе учится студент
# (Группы Python, FrontEnd, FullStack, Java). Студент может учиться в нескольких группах. Затем вывести:
# - студентов, которые учатся в двух и более группах
# - студентов, которые не учатся на фронтенде
# - студентов, которые изучают Python или Java

students = {
    'messi': ['Python', 'FrontEnd', 'FullStack', 'Java'],
    'ronaldo': ['FrontEnd'],
    'neymar': ['Python', 'FullStack'],
    'zidane': ['Java', 'FullStack', 'Python'],
    'pogba': ['FrontEnd'],
    'elshaarawy': ['Python', 'Java']
}

# студентов, которые учатся в двух и более группах
print('-------------------------')
for i in students:
    if len(students[i]) >= 2:
        print(str(i) + ' в ' + str(len(students[i])) + ' группах')

# студентов, которые не учатся на фронтенде
print('-------------------------')
for i in students:
    if 'FrontEnd' in students[i]:
        continue
    else:
        print(str(i) + ' не учится на FrontEnd')

# студентов, которые изучают Python или Java
print('-------------------------')
print('Учит Python или Java: ')
for i in students:
    if 'Python' in students[i]:
        print(i)
    elif 'Java' in students[i]:
        print(i)
    else:
        continue
