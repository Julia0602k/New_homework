# 1. Напишите программу, которая принимает целое число x
# и определяет, принадлежит ли данное число указанному промежутку:
# (-1, 17)

num1 = int(input('Введите целое число: '))
if -1 < num1 < 17:
    print('Введенное число принадлежит промежутку (-1; 17)')
else:
    print('Введенное число не принадлежит промежутку (-1; 17)')