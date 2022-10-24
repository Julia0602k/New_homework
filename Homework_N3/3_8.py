# 8. На числовой прямой даны два отрезка: [a1; b1] и [a2; b2]
# Напишите программу, которая находит их пересечение.
#
# Пересечением двух отрезков может быть:
# отрезок;
# точка;
# пустое множество.
#
# На вход программе подаются 4 целых числа a1, b1, a2, b2,
# каждое на отдельной строке. Гарантируется, что a1 < b1 и a2 < b2.
#
# Программа должна вывести на экран границы отрезка,
# являющегося пересечением, либо общую точку,
# либо текст «пустое множество».

a1 = int(input('Введите значение a1: '))
b1 = int(input('Введите значение b1: '))
a2 = int(input('Введите значение a2: '))
b2 = int(input('Введите значение b2: '))

if a1 >= b1 or a2 >= b2:
    print('Введите значения правильно! Условие: a1 < b1 и a2 < b2')
else:
    if a1 < b1 < a2 or a2 < b2 < a1:
        print('Пустое множество')
    elif b1 == a2:
        print('Общая точка отрезков: ', b1)
    elif b2 == a1:
        print('Общая точка отрезков: ', b2)
    elif a1 <= a2 < b1 <= b2:
        print('Границы отрезка, являющегося пересечением [', a2, ',', b1, ']', sep='')
    elif a1 <= a2 < b2 < b1:
        print('Границы отрезка, являющегося пересечением [', a2, ',', b2, ']', sep='')
    elif a2 < a1 < b2 <= b1:
        print('Границы отрезка, являющегося пересечением [', a1, ',', b2, ']', sep='')
    else:
        print('Границы отрезка, являющегося пересечением [', a1, ',', b1, ']', sep='')






    # if b1 > a2:
    #     print('Границы отрезка, являющегося пересечением [', a2, ',', b1, ']', sep='')
    # elif b1 == a2:
    #     print('Общая точка отрезков: ', b1)
    # elif b1 > b2
    # else:
    #     print('Пустое множество')

