# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names = {}
for student in students:
    if student['first_name'] not in names.keys():
        names[student['first_name']] = 1
    else:
        names[student['first_name']] += 1

for name, value in names.items():
    print(f'{name}: {value}')
# ???


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

names = dict()

for student in students:
    if student['first_name'] not in names.keys():
        names[student['first_name']] = 1
    else:
        names[student['first_name']] += 1
for name, value in names.items():
    if value == max(names.values()):
        print(f'Самое частое имя среди учеников: {name}')    
# ???


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

school_class = list()
i = 0

for school_class in school_students:
    school_class = school_students[i]
    
    names_1 = dict()
    i += 1
    
    for student in school_class:
        if student['first_name'] not in names_1.keys():
            names_1[student['first_name']] = 1
        else:
            names_1[student['first_name']] += 1
    
    for name, value in names_1.items():
        if value == max(names_1.values()):
            print(f'Самое частое имя в классе {i}: {name}')
    
# ???


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

j = 0

for class_gender in school:
    names_students = [m['first_name'] for m in school[j]['students']]
    
   
    for student_gen in names_students:
        
        list_girls = []
        list_boys = list()
        
        number_of_boys = 0
        number_of_girls = 0
        n = 0
        
        for i in range(len(school[j]['students'])):

            if is_male.get(names_students[n]) == False:
                list_girls.append(names_students[n])
                number_of_girls = len(list_girls) 
            else:
                list_boys.append(names_students[n])    
                number_of_boys = len(list_boys)
            n += 1
    a = school[j]['class']    
    print(f"В классе {a}: девочек {number_of_girls}, мальчиков {number_of_boys}")
    j += 1            
    
# ???


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
j = 0

for class_gender in school:
    names_students = [m['first_name'] for m in school[j]['students']]
    
   
    for student_gen in names_students:
        
        list_girls = []
        list_boys = list()
        
        number_of_boys = 0
        number_of_girls = 0
        n = 0
        
        for i in range(len(school[j]['students'])):

            if is_male.get(names_students[n]) == False:
                list_girls.append(names_students[n])
                number_of_girls = len(list_girls) 
            else:
                list_boys.append(names_students[n])    
                number_of_boys = len(list_boys)
            n += 1
    if number_of_boys > number_of_girls:
        print(f"Больше всего мальчиков в классе {school[j]['class']}")
    else:
        print(f"Больше всего девочек в классе {school[j]['class']}")

    j += 1            
    
# ???

